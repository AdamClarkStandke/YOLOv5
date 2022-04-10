#!/usr/bin/env python
# coding: utf-8

# In[ ]:


'''Implementing Faster R-CNN with PyTorch as described by Ivan Vasiley 
in his book: Advanced deep learning with Python'''


# In[1]:


import warnings
warnings.filterwarnings('ignore')


# In[2]:


import os.path
import numpy as np
import requests
import torchvision
import torchvision.transforms as transforms
from PIL import Image
import matplotlib.pyplot as plt
from torchinfo import summary
import cv2


# In[3]:


# Downloading the COCO class name dataset file
# Contains the names of the classes the network can
# detect
classes_file = 'coco.names'

# downloads the raw gitHub file (i.e. assests)
if os.path.isfile(classes_file):
    url = 'https://raw.githubusercontent.com/pjreddie/darknet/master/data/coco.names'
    # issues a HTTP GET request to get resource 
    r = requests.get(url)
    # writes the content out
    with open(classes_file, 'wb') as f:
        f.write(r.content)


# In[4]:


# loading the class names as a list 
with open(classes_file, 'r') as f:
    classes = [line.strip() for line in f.readlines()]

# printing the differnt classes that can be detected
# by faster R-CNN
# print(classes)


# In[5]:


# getting test image for object detection
image = cv2.imread('/mnt/chromeos/GoogleDrive/MyDrive/Datasets/baby.PNG')
# displaying generic test image with no detection and labels



# In[6]:


# Constructs a Faster R-CNN model with a ResNet-50-FPN backbone
model = torchvision.models.detection.fasterrcnn_resnet50_fpn(pretrained=True)


# In[7]:


# summary(model)


# In[8]:


# setting the model in evaluation mode(lol no training)
model.eval()


# In[20]:


# transforming image to tensor
transform = transforms.Compose([
    transforms.ToPILImage(),
    transforms.ToTensor()
])
nn_input = transform(image)
#getting output from the model
output = model([nn_input])


# In[21]:


# random colors for each class of the COCO dataset
colors = np.random.uniform(0,255, size=(len(classes), 3))


# In[22]:


# iterating over the network outputs for all boxes
for box, box_class, score in zip(output[0]['boxes'].detach().numpy(), 
                                output[0]['labels'].detach().numpy(),
                                output[0]['scores'].detach().numpy()):
    # filter the boxes by CI score
    if score > 0.9:
        # transform bounding box format to be 
        # top-left and bottom-right pixels of box (has to be integers)
        box = [(int(box[0]), int(box[1])), (int(box[2]), int(box[3]))]
        # selecting class color
        color = colors[box_class]
        # extracting class name
        class_name = classes[box_class]
        #drawing the bounding box
        cv2.rectangle(image, box[0], box[1],color=color, thickness=2)
        # displaying the box class label
        cv2.putText(img=image, text=class_name, org=box[0],
                    fontFace = cv2.FONT_HERSHEY_SIMPLEX,
                    fontScale=1, color=color, thickness=2)


# In[23]:


cv2.imshow('Object detection', image)
cv2.imwrite('FasterR-CNN2.png', image)

# In[ ]:




