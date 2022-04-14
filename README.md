# Training Object Detection on YOLOv5s on Raccoon Dataset 

## Click image to find if the vision model can find this pesky raccoon:
[![IMAGE ALT TEXT](https://github.com/aCStandke/Object-Detection/blob/main/mq2.jpg)](https://youtu.be/_8vjy7NFb2M)

# YOLO Model
Yolo works by splitting an image into a S by S gird of cells and the network looks over the grid cells as regions where objects may be located and assigns a bounding box to them; but one bounding box is associated with one gird cell even if the bounding box covers multiple cells based on the bounding box's center. 

## One object:
The network will output an array consisting of the following: 1) the object's bounding box if it exists, containing the box's x and y center coordinates and the box's height and width as determined through regression with l2 loss. See this video for a quick refresher on object location: [object location](https://www.youtube.com/watch?v=LZRfHkTNQqo) and 2)the classification of the image in the form of a probability called the confidence score. 

## Multiple Objects:
For multiple objects in the same grid cell anchor boxes are used that have different shapes and the proper anchor box for an object is chosen through the use of Intersection over Union(IoU), which is just the ratio between the area of the intersection of the object's bounding box in relation to the anchor boxes over their union. See this video for a quick refresher on anchor boxes: [anchor boxes](https://www.youtube.com/watch?v=SXmsPXsYkTw)

# What happens when images are improperly labeled?
Because I did not correctly transform the data for YOLO the object location was off as can be seen by the following batch validation images: 

## Batch-zero val images labels
![IMAGE ALT TEXT](https://github.com/aCStandke/Object-Detection/blob/main/val_images/val_batch0_labels.jpg)

## Batch-zero val images prediction
![IMAGE ALT TEXT](https://github.com/aCStandke/Object-Detection/blob/main/val_images/val_batch0_pred.jpg)

## Code
The code can be found in the [Training YOLOv5s](https://github.com/aCStandke/Object-Detection/blob/main/TrainingYolo.ipynb) which can be run in a colab environment.
