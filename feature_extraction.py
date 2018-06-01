import cv2
import numpy as np
from sklearn import svm
import os
import sys
from PIL import Image



files1=os.listdir("test_o\\");
PATH="test_o/";

#print len(files);
x = np.zeros((len(files1),7));
count=0;
labels=np.zeros(len(files1));

for idx,filename in enumerate(files1):
    if filename!="Thumbs.db":
        infile=PATH+filename;
        #outfile="1/"+filename;
        image = cv2.imread(infile);
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY);
        feature = cv2.HuMoments(cv2.moments(image)).flatten()
        features = -np.sign(feature) * np.log10(np.abs(feature))
        x[count]=features;
        
        labels[count]=1;
    
        count=count+1;
        
        print repr(features);
        
