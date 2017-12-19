# seq_nms_yolo

#### Membres: Yunyun SUN, Yutong YAN, Sixiang XU, Heng ZHANG

---

## Introduction

![](img/index.jpg) 

This project combines **YOLOv2**([reference](https://arxiv.org/abs/1506.02640)) and **seq-nms**([reference](https://arxiv.org/abs/1602.08465)) to realise **real time video detection**.

## Steps

- Install `Tensorflow Object Detction API`([reference](https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/installation.md));
- Modify the `Makefile` file according to your environment.
```
GPU=1		# 0 if your pc donesn't support CUDA
CUDNN=1		# 0 if your pc donesn't support CUDNN
OPENCV=1	# 0 if your pc donesn't support OPENCV
```
- `make` the project;
- Download `yolo.weights` and `tiny-yolo.weights` by running:
```bash
wget https://pjreddie.com/media/files/yolo.weights
wget https://pjreddie.com/media/files/tiny-yolo-voc.weights
```
- Copy a video file to the video directory, for example, `input.mp4`;
- From the video directory, run:
```bash
python video2img.py -i input.mp4
python get_pkllist.py
```
- Return to root directory and run `python yolo_seqnms.py` to generate output images in the `video/output` directory;
- If you want to reconstruct a video from these output images, you can go to the video folder and run `python img2video.py -i output`. It will generate a video named `output.mp4` in the video folder.

## Reference

This project copies lots of code from [darknet](https://github.com/pjreddie/darknet) , [Seq-NMS](https://github.com/lrghust/Seq-NMS) and  [models](https://github.com/tensorflow/models).