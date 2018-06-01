import cv2
import numpy as np
from sklearn import svm
import os
import sys
from PIL import Image



files1=os.listdir("b\\1");
files2=os.listdir("b\\2");
files3=os.listdir("b\\3");
files4=os.listdir("b\\4");
files5=os.listdir("b\\5");
files6=os.listdir("b\\6");
files7=os.listdir("b\\7");
files8=os.listdir("o\\1");
files9=os.listdir("o\\2");
files10=os.listdir("o\\3");
files11=os.listdir("o\\4");
files12=os.listdir("k\\1");
files13=os.listdir("k\\2");
files14=os.listdir("k\\3");
files15=os.listdir("k\\4");
files16=os.listdir("k\\5");

#print len(files);
x = np.zeros((len(files1) + len(files2)+ len(files4)+ len(files5)+ len(files6)+ len(files8)+
              len(files9)+ len(files10) +len(files11) + len(files12) + len(files13)+ len(files14)+ len(files15)+ len(files16) ,7));
count=0;
labels=[];

#*****************************************************************
PATH="b/1/";

for idx,filename in enumerate(files1):
    if filename!="Thumbs.db":
        infile=PATH+filename;
        #outfile="1/"+filename;
        image = cv2.imread(infile);
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY);
        feature = cv2.HuMoments(cv2.moments(image)).flatten()
        features = -np.sign(feature) * np.log10(np.abs(feature))
        x[count]=features;
        labels.append(1);
        count=count+1;
        #print features;

#*****************************************************************
#*****************************************************************
PATH="b/2/";

for idx,filename in enumerate(files2):
    if filename!="Thumbs.db":
        infile=PATH+filename;
        #outfile="1/"+filename;
        image = cv2.imread(infile);
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY);
        feature = cv2.HuMoments(cv2.moments(image)).flatten()
        features = -np.sign(feature) * np.log10(np.abs(feature))
        x[count]=features;
        labels.append(2);
        count=count+1;
        #print features;

#*****************************************************************
#*****************************************************************
##PATH="b/3/";
##
##for idx,filename in enumerate(files3):
##    if filename!="Thumbs.db":
##        infile=PATH+filename;
##        #outfile="1/"+filename;
##        image = cv2.imread(infile);
##        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY);
##        feature = cv2.HuMoments(cv2.moments(image)).flatten()
##        features = -np.sign(feature) * np.log10(np.abs(feature))
##        x[count]=features;
##        labels.append(3);
##        count=count+1;
##        #print features;

#*****************************************************************
#*****************************************************************
PATH="b/4/";

for idx,filename in enumerate(files4):
    if filename!="Thumbs.db":
        infile=PATH+filename;
        #outfile="1/"+filename;
        image = cv2.imread(infile);
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY);
        feature = cv2.HuMoments(cv2.moments(image)).flatten()
        features = -np.sign(feature) * np.log10(np.abs(feature))
        x[count]=features;
        labels.append(4);
        count=count+1;
        #print features;

#*****************************************************************
#*****************************************************************
PATH="b/5/";

for idx,filename in enumerate(files5):
    if filename!="Thumbs.db":
        infile=PATH+filename;
        #outfile="1/"+filename;
        image = cv2.imread(infile);
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY);
        feature = cv2.HuMoments(cv2.moments(image)).flatten()
        features = -np.sign(feature) * np.log10(np.abs(feature))
        x[count]=features;
        labels.append(5);
        count=count+1;
        #print features;

#*****************************************************************
#*****************************************************************
PATH="b/6/";

for idx,filename in enumerate(files6):
    if filename!="Thumbs.db":
        infile=PATH+filename;
        #outfile="1/"+filename;
        image = cv2.imread(infile);
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY);
        feature = cv2.HuMoments(cv2.moments(image)).flatten()
        features = -np.sign(feature) * np.log10(np.abs(feature))
        x[count]=features;
        labels.append(6);
        count=count+1;
        #print features;

#*****************************************************************
#*****************************************************************
PATH="b/7/";

for idx,filename in enumerate(files7):
    if filename!="Thumbs.db":
        infile=PATH+filename;
        #outfile="1/"+filename;
        image = cv2.imread(infile);
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY);
        feature = cv2.HuMoments(cv2.moments(image)).flatten()
        features = -np.sign(feature) * np.log10(np.abs(feature))
        x[count]=features;
        labels.append(7);
        count=count+1;
        #print features;

#*****************************************************************
#*****************************************************************
PATH="o/1/";

for idx,filename in enumerate(files8):
    if filename!="Thumbs.db":
        infile=PATH+filename;
        #outfile="1/"+filename;
        image = cv2.imread(infile);
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY);
        feature = cv2.HuMoments(cv2.moments(image)).flatten()
        features = -np.sign(feature) * np.log10(np.abs(feature))
        x[count]=features;
        labels.append(8);
        count=count+1;
        #print features;

#*****************************************************************
#*****************************************************************
PATH="o/2/";

for idx,filename in enumerate(files9):
    if filename!="Thumbs.db":
        infile=PATH+filename;
        #outfile="1/"+filename;
        image = cv2.imread(infile);
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY);
        feature = cv2.HuMoments(cv2.moments(image)).flatten()
        features = -np.sign(feature) * np.log10(np.abs(feature))
        x[count]=features;
        labels.append(9);
        count=count+1;
        #print features;

#*****************************************************************
#*****************************************************************
PATH="o/3/";

for idx,filename in enumerate(files10):
    if filename!="Thumbs.db":
        infile=PATH+filename;
        #outfile="1/"+filename;
        image = cv2.imread(infile);
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY);
        feature = cv2.HuMoments(cv2.moments(image)).flatten()
        features = -np.sign(feature) * np.log10(np.abs(feature))
        x[count]=features;
        labels.append(10);
        count=count+1;
        #print features;

#*****************************************************************
#*****************************************************************
PATH="o/4/";

for idx,filename in enumerate(files11):
    if filename!="Thumbs.db":
        infile=PATH+filename;
        #outfile="1/"+filename;
        image = cv2.imread(infile);
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY);
        feature = cv2.HuMoments(cv2.moments(image)).flatten()
        features = -np.sign(feature) * np.log10(np.abs(feature))
        x[count]=features;
        labels.append(11);
        count=count+1;
        #print features;


#*****************************************************************

#*****************************************************************
PATH="k/1/";

for idx,filename in enumerate(files12):
    if filename!="Thumbs.db":
        infile=PATH+filename;
        #outfile="1/"+filename;
        image = cv2.imread(infile);
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY);
        feature = cv2.HuMoments(cv2.moments(image)).flatten()
        features = -np.sign(feature) * np.log10(np.abs(feature))
        x[count]=features;
        labels.append(12);
        count=count+1;
        #print features;


#*****************************************************************
#*****************************************************************
PATH="k/2/";

for idx,filename in enumerate(files13):
    if filename!="Thumbs.db":
        infile=PATH+filename;
        #outfile="1/"+filename;
        image = cv2.imread(infile);
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY);
        feature = cv2.HuMoments(cv2.moments(image)).flatten()
        features = -np.sign(feature) * np.log10(np.abs(feature))
        x[count]=features;
        labels.append(13);
        count=count+1;
        #print features;


#*****************************************************************
#*****************************************************************
PATH="k/3/";

for idx,filename in enumerate(files14):
    if filename!="Thumbs.db":
        infile=PATH+filename;
        #outfile="1/"+filename;
        image = cv2.imread(infile);
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY);
        feature = cv2.HuMoments(cv2.moments(image)).flatten()
        features = -np.sign(feature) * np.log10(np.abs(feature))
        x[count]=features;
        labels.append(14);
        count=count+1;
        #print features;


#*****************************************************************
#*****************************************************************
PATH="k/4/";

for idx,filename in enumerate(files15):
    if filename!="Thumbs.db":
        infile=PATH+filename;
        #outfile="1/"+filename;
        image = cv2.imread(infile);
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY);
        feature = cv2.HuMoments(cv2.moments(image)).flatten()
        features = -np.sign(feature) * np.log10(np.abs(feature))
        x[count]=features;
        labels.append(15);
        count=count+1;
        #print features;


#*****************************************************************
#*****************************************************************
PATH="k/5/";

for idx,filename in enumerate(files16):
    if filename!="Thumbs.db":
        infile=PATH+filename;
        #outfile="1/"+filename;
        image = cv2.imread(infile);
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY);
        feature = cv2.HuMoments(cv2.moments(image)).flatten()
        features = -np.sign(feature) * np.log10(np.abs(feature))
        x[count]=features;
        labels.append(16);
        count=count+1;
        #print features;


#*****************************************************************        


for i in range (0,len(x)-len(labels)):
	labels.append(11);

#***********************************traning*********************
#x = -np.sign(x) * np.log10(np.abs(x))	
#print repr(x)
clf = svm.SVC(kernel='linear',C = 1.0);
#clf = svm.SVC( kernel='rbf',C = 1.0,gamma = 'auto');
clf.fit(x,labels);

print "Traning done";

#**************************TESTING*********************************
test=os.listdir("test\\");
PATH="test/";
for idx,filename in enumerate(test):
    if filename!="Thumbs.db":
        infile=PATH+filename;
        #outfile="1/"+filename;
        image = cv2.imread(infile);
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY);
        feature = cv2.HuMoments(cv2.moments(image)).flatten()
        features = -np.sign(feature) * np.log10(np.abs(feature))
        print filename,clf.predict(features);
