# Object Detection

## Default Detection Faster R-CNN Model (no seperate training, just pre-trained)
First test implementation of the Faster R-CNN model with a ResNet-50-FPN backbone. Implementation is detailed by Ivan Vasiley in his book: Advanced deep learning with Python. Inference was tested with a random image I had on my phone,at thetime, which contains two things: a person and a cute puppy dog. When using a score threshold of 0.9 the result was this
detection and classification:![alt text](https://github.com/aCStandke/FasterR-CNN/blob/main/FasterR-CNN2.png)
When using a score threshold of 0.5 the result was this detection and classification:![alt text](https://github.com/aCStandke/FasterR-CNN/blob/main/Faster%20R-CNN.png) code is found in the file: [Faster R-CNN.py](https://github.com/aCStandke/Object-Detection/blob/main/Faster%20R-CNN.py)

## Default Detection YOLOv5s Model (no seperate training, just pre-trained)
First test implementation of the YOLOv5s model.Inference was tested with a random image I had on my phone, at the time, which contains two things: a person and a cute puppy dog. When using  a confidence level of 0.25 (other default details found in the code),the result was this detection and classification:![alt text](https://github.com/aCStandke/FasterR-CNN/blob/main/YOLOv5s.png) code is found in the file: [YOLOv5s vs Faster R-CNN.ipynb](https://github.com/aCStandke/Object-Detection/blob/main/YOLOv5s%20vs%20Faster%20R-CNN.ipynb)

## Training Object Detection using Faster R-CNN Model and YOLOv5s on Racoon Dataset 


