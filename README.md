# Tag2Vec

## Contents

1. [Introduction](#introduction)
2. [Resources](#resources)
4. [How To Run](#how-to-run)
    1. [Improved Dense Trajectories(iDT)](improved_dense_trajectories(idt))
    2. [Tag2Vec](#tag2vec)


### Introduction

The project contains the resources for building the project [Tag2Vec](https://arxiv.org/abs/1612.04061)

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
