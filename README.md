# Classification-of-Indian-classical-dances
The algorithm proposed in this paper aims to achieve pose recognition in Indian classical dance domain.
Three different dances namely Bharatnatyam, Kathak and Odissi, all together with 15 poses have been considered for pose classification.
An initial database is created consisting of 100 images and split into training and testing dataset. Hu moments are chosen as the 
feature extraction technique to describe the shape context of an image since they are scale, translation and rotation invariant. 
To extract Hu moments, foreground and background of images is separated and resultant images are then converted to binary. 
Since, it is a multiclass classification problem SVM is implemented using one vs one and one vs all approach and the results are contrasted with linear and RBF kernels for both the approaches.


#Steps to run the code
1. Use binary.py to convert all the chroma photogaphs into binary.
2. Run feature_extraction.py to extract Hu moments from binary images.
3. Fit SVM classifier using OVO and OVR techniques using RBF and Linear kernel using SVM_clubbed.py
4. Predict the test data using main_pos.py
