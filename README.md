# Learning to hash-tag videos with Tag2Vec

The project contains the resources for [Tag2Vec](https://arxiv.org/abs/1612.04061) project. 

# Citing

    @inproceedings{Singh:2016:LHV:3009977.3010035,
     author = {Singh, Aditya and Saini, Saurabh and Shah, Rajvi and Narayanan, P J},
     title = {Learning to Hash-tag Videos with Tag2Vec},
     booktitle = {Proceedings of the Tenth Indian Conference on Computer Vision, Graphics and Image Processing},
     series = {ICVGIP '16},
     year = {2016},
     isbn = {978-1-4503-4753-2},
     location = {Guwahati, Assam, India},
     pages = {94:1--94:8},
     articleno = {94},
     numpages = {8},
     url = {http://doi.acm.org/10.1145/3009977.3010035},
     doi = {10.1145/3009977.3010035},
     acmid = {3010035},
     publisher = {ACM},
     address = {New York, NY, USA},
     keywords = {Tag2Vec, hash-tag recommendation, video tagging},
    } 

## Contents

1. [Introduction](#introduction)
2. [Resources](#resources)
4. [How To Run](#how-to-run)
    1. [Improved Dense Trajectories(iDT)](improved_dense_trajectories(idt))
    2. [Tag2Vec](#tag2vec)


### Introduction


### Resources
1. [Improved Dense Trajectory](http://lear.inrialpes.fr/~wang/improved_trajectories)
2. [17K-HashTag Categories](https://1drv.ms/u/s!AjolE1_VpgR6ijGESpBJ8QeUkKVV?e=3kLjzy)
3. [Train Videos]()
4. [Test Videos](https://1drv.ms/u/s!AjolE1_VpgR6ijLig4Qc7Ji46uuQ?e=uIr4ff)

### How To Run
##### [Improved Dense Trajectories(iDT)]
It's a fairly old project and might not run with the latest version of OpenCV or Ubuntu. I have created a Docker image using Ubuntu14.04 as a base and built openCV 2.4.13 and iDT. 
1. To install Docker you can follow the instructions provided [here](https://docs.docker.com/get-started/) or any other resource on the net.

2. Execute the **run** command. `docker run -it aditya27singh/improved_dense_trajectory:success`

3. Navigate to `/home/aditya/iiit`. This will be reffered to as the `$ROOT_DIR` 

4. Following the command described on the author's [README](http://lear.inrialpes.fr/~wang/download/improved_trajectory_release/README) one can generate features for the videos.
`$ROOT_DIR/iDT/release/DenseTrackStab video_name.vob -H video_name.bb > video_name.ft`

##### [Tag2Vec]
**Updating soon**
