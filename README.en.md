# Image_Classify_WebGUI_CIFAR10

✨**Intelligent Image Classification Web Applcation based on Convolutional Neural Networks and the CIFAR10 Dataset** : Image classification visualization interface, image classification front-end web page, image classification Demo display-Pywebio. AI artificial intelligence image classification-Pytorch. CIFAR10 dataset, small model. 100% pure Python code, lightweight, easy to reproduce.

[简体中文文档](./README.md)

[Personal website: www.bytesc.top](http://www.bytesc.top) includes online project demonstrations.

## Project Introduction
* 1. Use pytorch to implement intelligent classification of CIFAR10 dataset images
* 2. Use a small model, lightweight, with a 76% accuracy rate
* 3. Use pywebio as the web visualization framework, no need for front-end language, written in pure python. Lightweight, easy to reproduce, easy to deploy

Network structure used
![image](./readme_static/readme_img/net.png)

## Screenshot of the effect
![image](./readme_static/readme_img/1.png)
![image](./readme_static/readme_img/2.png)
![image](./readme_static/readme_img/3.png)

## How to use
Python version 3.9

First install dependencies
> pip install -r requirement.txt

modelDemo.py is the project entry point, run this file to start the server
> python modelDemo.py

Copy the link to the browser and open it
![image](./readme_static/readme_img/p1.png)
Click "Demo" to enter the Web interface
![image](./readme_static/readme_img/p2.png)

After that, you can also click "Upload File" and select an image file from the example_img folder to upload and test

## Project structure
```
└─Image_Classify_WebGUI_CIFAR10
    ├─data
    │  └─logs_import 
    ├─example_img
    ├─process
    │  └─logs
    └─readme_static
```
* The data folder stores some static resources, including the trained model.pth
* The process folder stores some process files, including the model training program, etc.
* readme_static stores static resources used in the readme document
* The example_img folder contains some images that can be used for testing