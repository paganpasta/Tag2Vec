import argparse
import subprocess
import os
import re
from nltk.stem.snowball import SnowballStemmer
import sklearn
import pickle

def parser():
    parser = argparse.ArgumentParser(description='Preprocess data in the $root folder. Removing duplicate videos, low freq hashtags etc.')
    parser.add_argument("--video_root", required=True, help='Absolute path to the video data folder')
    parser.add_argument("--inter_class_frequency", default=3, help='Number of classes a hashtag should occur in to  be valid')
    parser.add_argument("--intra_class_frequency", default=3, help='Number of times a hashtag should occur in one class to be valid')
    # A hashtag is valid if either of the above 2 conditions are satisfied
    return parser.parse_args()


def remove_duplicate_videos(root_path):
    accepted_videos = {}
    duplicate_videos = []
    for r, dirs, files in os.walk(root_path):
        for f in files:
            if f.endswith('.mp4'):
                f = os.path.join(r, f)
                hash = subprocess.run(['md5sum', f], stdout=subprocess.PIPE)
                hash = (hash.stdout.decode('utf-8')).split(' ')[0]
                if hash in accepted_videos:
                    duplicate_videos.append(f)
                else:
                    accepted_videos[hash] = f

    accepted_videos = list(accepted_videos.values())
    return accepted_videos, duplicate_videos


def pre_process_videos_on_hashtags(videos):
    stemmer = SnowballStemmer('english')
    class_hashtags = {}
    accepted_videos = set()
    rejected_videos = []
    missing_videos = []

    stem_to_hashtag = {}

    for video in videos:
        elements = video.split('/')
        video_name, class_name, class_level_path = elements[-1], elements[-3], '/'.join(i for i in elements[:-2])
        video_tags = []
        try:
            with open(os.path.join(class_level_path, 'TAGS', video_name.split('.')[0]+'.txt')) as f:
                for word in f:
                    if word[0] != '#':  # We only consider hash-tags
                        continue
                    else:
                        word_alpha = re.sub('[^a-zA-Z]+', '', word.lower())    #Remove non-alphabets
                        if word_alpha == class_name.lower() and video not in accepted_videos:
                            accepted_videos.add(video)
                        stemmed_word = stemmer.stem(word_alpha.lower())
                        video_tags.append(stemmed_word)
                        stem_to_hashtag[word_alpha] = stemmed_word
        except:
            missing_videos.append(video)

        if video in accepted_videos:
            class_hashtags[class_name] = class_hashtags.get(class_name, {})
            for video_tag in video_tags:
                class_hashtags[class_name][video_tag] = class_hashtags[class_name].get(video_tag, 0) + 1
        elif video not in missing_videos:
            rejected_videos.append(video)

    return list(accepted_videos), rejected_videos, missing_videos, class_hashtags, stem_to_hashtag

def tf_idf(class_hashtags, inter_class_frequency=3, intra_class_frequency=3):
    valid_hashtags = {}
    buffer_hashtags = {}

    for cls, hashtags in class_hashtags.items():
        for hashtag, freq in hashtags.items():
            if freq >= intra_class_frequency:
                valid_hashtags[hashtag] = valid_hashtags.get(hashtag, 0) + freq
            else:
                buffer_hashtags[hashtag] = buffer_hashtags.get(hashtag, 0) + 1

    to_delete = []
    for hashtag, freq in buffer_hashtags.items():
        if freq > inter_class_frequency:
            valid_hashtags[hashtag] = valid_hashtags.get(hashtag, 0) + freq
            to_delete.append(hashtag)

    for i in to_delete:
        buffer_hashtags.pop(i, None)

    return valid_hashtags, buffer_hashtags


def main(args):
    accepted_videos, duplicate_videos = remove_duplicate_videos(args.video_root)

    train, test = sklearn.model_selection.train_test_split(accepted_videos, test_size=0.20, random_state=42)
    train, val = sklearn.model_selection.train_test_split(train, test_size=0.10, random_state=42)

    accepted_videos, rejected_videos_ht, missing_videos_ht, class_hashtags, stem_to_hash = pre_process_videos_on_hashtags(train)
    rejected_videos = rejected_videos_ht + missing_videos_ht
    print('Accepted train videos: {}\nTotal rejected videos: {}\nTest videos: {}\nvalidation videos: {}'
          .format(len(accepted_videos), len(rejected_videos), len(test), len(val)))

    valid_hashtags, invalid_hashtags = tf_idf(class_hashtags)

    to_save = {'valid_hashtags':valid_hashtags, 'stem2hash': stem_to_hash}

    with open('data.pkl', 'wb') as f:
        pickle.dump(to_save, f, pickle.HIGHEST_PROTOCOL)

    with open('train.pickle', 'wb') as f:
        pickle.dump(accepted_videos, f)
    with open('test.pickle', 'wb') as f:
        pickle.dump(test, f)
    with open('val.pickle', 'wb') as f:
        pickle.dump(val, f)

if __name__ == '__main__':
    args = parser()
    main(args)
