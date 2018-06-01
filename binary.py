import cv2
import numpy as np
from sklearn import svm
import os
import sys
from PIL import Image



files1=os.listdir("bharath\\");
PATH="bharath/";


#print len(files);
x = np.zeros((len(files1),7));
count=0;
labels=np.zeros(len(files1));

for idx,filename in enumerate(files1):
    if filename!="Thumbs.db":
        infile=PATH+filename;
        #outfile="1/"+filename;
        image = cv2.imread(infile);
        image = cv2.cvtColor(image,cv2.IMREAD_GRAYSCALE);
        (thresh,im_bw) = cv2.threshold(image, 230, 255, cv2.THRESH_BINARY)
       # cv2.imshow('image',im_bw)
        outfile = "bharath/"+filename
        #print features;
