import cv2
import numpy as np
from sklearn import svm
import os
import sys
from PIL import Image
from sklearn.svm import LinearSVC
import numpy


files1=os.listdir("b3\\1");
files2=os.listdir("b3\\2");
files3=os.listdir("b3\\3");
files4=os.listdir("b3\\4");
files5=os.listdir("b3\\5");
files6=os.listdir("b3\\6");
#files7=os.listdir("b\\7");



#print len(files);
x = np.zeros((len(files1) + len(files2)+ len(files3)+ len(files4)+ len(files5)+ len(files6),7));
count=0;
labels=[];

#*****************************************************************
PATH="b3/1/";
print "#1"
for idx,filename in enumerate(files1):
    if filename!="Thumbs.db":
        infile=PATH+filename;
        #outfile="1/"+filename;
        image = cv2.imread(infile);
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY);
        features = cv2.HuMoments(cv2.moments(image)).flatten()
        x[count]=features;
        labels.append(0);
        count=count+1;
        print (features);

#*****************************************************************
#*****************************************************************
PATH="b3/2/";
print "#2"
for idx,filename in enumerate(files2):
    if filename!="Thumbs.db":
        infile=PATH+filename;
        #outfile="1/"+filename;
        image = cv2.imread(infile);
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY);
        features = cv2.HuMoments(cv2.moments(image)).flatten()
        x[count]=features;
        labels.append(1);
        count=count+1;
        print (features);

#*****************************************************************
#*****************************************************************
PATH="b3/3/";
print "#3"
for idx,filename in enumerate(files3):
    if filename!="Thumbs.db":
        infile=PATH+filename;
        #outfile="1/"+filename;
        image = cv2.imread(infile);
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY);
        features = cv2.HuMoments(cv2.moments(image)).flatten()
        x[count]=features;
        labels.append(2);
        count=count+1;
        print (features);

#*****************************************************************
#*****************************************************************
PATH="b3/4/";
print "#4"
for idx,filename in enumerate(files4):
    if filename!="Thumbs.db":
        infile=PATH+filename;
        #outfile="1/"+filename;
        image = cv2.imread(infile);
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY);
        features = cv2.HuMoments(cv2.moments(image)).flatten()
        x[count]=features;
        labels.append(3);
        count=count+1;
        print (features);

#*****************************************************************
#*****************************************************************
PATH="b3/5/";
print "#5"
for idx,filename in enumerate(files5):
    if filename!="Thumbs.db":
        infile=PATH+filename;
        #outfile="1/"+filename;
        image = cv2.imread(infile);
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY);
        features = cv2.HuMoments(cv2.moments(image)).flatten()
        x[count]=features;
        labels.append(4);
        count=count+1;
        print (features);

#*****************************************************************
#*****************************************************************
PATH="b3/6/";
print "#6"
for idx,filename in enumerate(files6):
    if filename!="Thumbs.db":
        infile=PATH+filename;
        #outfile="1/"+filename;
        image = cv2.imread(infile);
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY);
        features = cv2.HuMoments(cv2.moments(image)).flatten()
        x[count]=features;
        labels.append(5);
        count=count+1;
        print (features);

#*****************************************************************
#*****************************************************************
#PATH="b/7/";
#print "#7"
#for idx,filename in enumerate(files7):
#    if filename!="Thumbs.db":
 #       infile=PATH+filename;
        #outfile="1/"+filename;
   #     image = cv2.imread(infile);
   #     image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY);
  #      features = cv2.HuMoments(cv2.moments(image)).flatten()
  #      x[count]=features;
 #       labels.append(6);
 #       count=count+1;
      #  print repr(features);


#*****************************************************************
        

for i in range (0,len(x)-len(labels)):
	labels.append(11);

#***********************************traning*********************	
clf = svm.SVC(kernel='linear', C = 1.0);

#lin_clf = svm.LinearSVC()
#lin_clf.fit(x, labels) 
#LinearSVC(C=1.0, class_weight=None, dual=True, fit_intercept=True,
#     intercept_scaling=1, loss='squared_hinge', max_iter=1000,
#     multi_class='ovr', penalty='l2', random_state=None, tol=0.0001,
#     verbose=0)
	
clf.fit(x,labels);

print "Traning done";

#**************************TESTING*********************************
test=os.listdir("test\\");
PATH="test/";
print "#test"
for idx,filename in enumerate(test):
    if filename!="Thumbs.db":
        infile=PATH+filename;
        #outfile="1/"+filename;
        image = cv2.imread(infile);
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY);
        features = cv2.HuMoments(cv2.moments(image)).flatten()
        print (features)
        print filename,clf.predict(features);
       
