# Object Detection

## Detection using the Faster R-CNN Model (no seperate training, just pre-trained for now)
First test implementation of the Faster R-CNN model with a ResNet-50-FPN backbone. Implementation is detailed by Ivan Vasiley in his book: Advanced deep learning with Python. Inference was tested with a random image I had on my phone,at the time, which contains two things: a person (ie. Alexis) and a cute puppy dog (ie. Misha). 
![alt text](https://github.com/aCStandke/FasterR-CNN/blob/main/Faster%20R-CNN.png)
The pre-trained model was able to detect two things, but the classification was wrong (obviously!). The reason for this might be due to the model being trained on more images that contain unions rather than intersections (i.e. less complex data) and/or the ROI pooling layer(will test image using YOLOv5 model to see if this intuition is true or not! (when I get to it)). As always, code is found in the file: [Faster R-CNN.py](https://github.com/aCStandke/Object-Detection/blob/main/Faster%20R-CNN.py)

## Detection using the YOLOv5s Model (no seperate training, just pre-trained for now)
First test implementation of the YOLOv5s model. Inferece was tested with the two images provided. As always, code is found in the file: [Yolo.ipynb](https://github.com/aCStandke/Object-Detection/blob/main/Yolo.ipynb)    
![alt text](https://github.com/aCStandke/FasterR-CNN/blob/main/runs/detect/exp/zidane.jpg)
![alt text](https://github.com/aCStandke/FasterR-CNN/blob/main/runs/detect/exp/bus.jpg)

## Training Object Detection using Faster R-CNN Model and YOLOv5s on Racoon Dataset 
To do...............when I get to it! lol

