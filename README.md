# Learning to hash-tag videos with Tag2Vec

The project contains the resources for [Tag2Vec](https://arxiv.org/abs/1612.04061) project. The repository contains the link to the resources for ~3 million hashtagged vines, 3000 train-test vines with their associated hashtags. Apart from it the steps also describe how to use the Improved Dense Trajectories code to generate video descriptors. 

**Currently working on integrating zslearning and other required libraries into the docker** 

# Citing

    @inproceedings{Singh:2016:LHV:3009977.3010035,
     author = {Singh, Aditya and Saini, Saurabh and Shah, Rajvi and Narayanan, P J},
     title = {Learning to Hash-tag Videos with Tag2Vec},
     booktitle = {Proceedings of the Tenth Indian Conference on Computer Vision, Graphics and Image Processing},
     series = {ICVGIP '16},
     year = {2016},
     keywords = {Tag2Vec, hash-tag recommendation, video tagging},
    } 

## Contents

1. [Resources](#resources)
2. [How To Run](#how-to-run)
    1. [Improved Dense Trajectories(iDT)](improved_dense_trajectories(idt))
    2. [Tag2Vec](#tag2vec)

### Resources
1. [Improved Dense Trajectory](http://lear.inrialpes.fr/~wang/improved_trajectories)
2. [Zero Shot Learning](https://github.com/mganjoo/zslearning)
3. [3 Million Hashtags](https://1drv.ms/u/s!AjolE1_VpgR6ijGESpBJ8QeUkKVV?e=3kLjzy)
4. [Train-Test Videos](https://1drv.ms/u/s!AjolE1_VpgR6ijLig4Qc7Ji46uuQ?e=uIr4ff)

### How To Run
##### Improved Dense Trajectories(iDT)
It's a fairly old project and might not run with the latest version of OpenCV or Ubuntu. I have created a Docker image using Ubuntu14.04 as a base and built openCV 2.4.13 and iDT. 
1. To install Docker you can follow the instructions provided [here](https://docs.docker.com/get-started/) or any other resource on the net.

2. Execute the **run** command. `docker run -it aditya27singh/improved_dense_trajectory:success`

3. Navigate to `/home/aditya/iiit`. This will be reffered to as the `$ROOT_DIR` 

4. Following the command described on the author's [README](http://lear.inrialpes.fr/~wang/download/improved_trajectory_release/README) one can generate features for the videos.
`$ROOT_DIR/iDT/release/DenseTrackStab video_name.vob -H video_name.bb > video_name.ft`

##### Embedding Learning
The work utilized the [Zero-Shot learning](https://github.com/mganjoo/zslearning) to obtain the mapping from Video to Word descriptors

##### Tag2Vec
**Note** Requires precomputed iDTs
**Preprocessing**
1. Remove duplicate videos. Based on md5 hash one can remove duplicate video data
2. Process Hashtags and remove data which doesn't contain #CLASSNAME
3. Remove Hashtags based on TF-IDF and lowest in-class frequency
