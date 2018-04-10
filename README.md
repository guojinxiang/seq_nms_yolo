# seq_nms_yolo

## News

- Updated to YOLOv3! For more details, see [this](https://pjreddie.com/darknet/yolo/).

## Introduction

<p align="center">
    <img src="doc/intro1.gif", width="480">
</p>

<p align="center">
    <img src="doc/intro.gif", width="480">
</p>


This project combines **YOLOv2**([reference](https://arxiv.org/abs/1506.02640)) and **seq-nms**([reference](https://arxiv.org/abs/1602.08465)) to realise **real time video detection**.

## Steps

- Install `Tensorflow Object Detction API`([reference](https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/installation.md));
- Modify the `Makefile` file according to your environment.
```
GPU=1		# 0 if your pc doesn't support CUDA
CUDNN=1		# 0 if your pc doesn't support CUDNN
OPENCV=1	# 0 if your pc doesn't support OPENCV
```
- `make` the project;
- Download `yolov3.weights`, `yolov2.weights` and `yolov2-tiny-voc.weights` by running:
```bash
wget https://pjreddie.com/media/files/yolov3.weights
wget https://pjreddie.com/media/files/yolov2.weights
wget https://pjreddie.com/media/files/yolov2-tiny-voc.weights
```
- Copy a video file to the video directory, for example, `input.mp4`;
- From the video directory, run:
```bash
python video2img.py input.mp4
```
- Return to root directory and run: 
```
python yolo_seqnms.py
```
- **Attention: This scipt will fail if Tensorflow Object Detection API is not installed**;
- If you want a fatser detect, run:
```
python yolo_seqnms.py tiny
```
- If you want to use yolov2:
```
python yolo_seqnms.py v2
```
- If you only want to detect person, run:
```
python yolo_seqnms.py only_person
```
- If you want to reconstruct a video from these output images, you can go to the video directory and run:
```
python img2video.py output.mp4
```
- If you want to watch the video after creat it, run:
```
python img2video.py output.mp4 play
```
## Document

- [Techinque report](https://docs.google.com/document/d/1o1y1F5bB3CZMMYXZxHyTum6B9N1ZmCkvrn2fRiC9dIc/edit?usp=sharing) 
- [Presentation slide](https://docs.google.com/presentation/d/1-j3y5muOubQiPvsZzTebafMdmpVQ8yq3prrBHl2wbaA/edit?usp=sharing) 

## Results

Here’s what I got from running my model over a demo video. Clic the image to watch the video on Youtube.

[![Watch the video](img/index.jpg)](https://www.youtube.com/watch?v=XC-3qXT0NsY)

## Reference

This project copies lots of code from [darknet](https://github.com/pjreddie/darknet) , [Seq-NMS](https://github.com/lrghust/Seq-NMS) and  [models](https://github.com/tensorflow/models).

## Team membres

- [Yunyun SUN](https://github.com/syyprime) , [Yutong YAN](https://github.com/melodiepupu) , [Sixiang XU](https://github.com/soarodo) , [Heng ZHANG](https://github.com/ZHANGHeng19931123).

<p align="center">
    <img src="doc/img.jpg", width="480">
</p>
