# Lab Objective

* Learn how to apply image segmentation.
* Use clustering techniques to differentiate between image objects.
* All requirements are available at the notebook.

---
# Problem Statement

We intend to perform image segmentation. Image segmentation means that we can group similar pixels together and give these grouped pixels the same label. The grouping problem is a clustering problem. We want to study the use of K-means and Normalized - Cut methods on the Berkeley Segmentation Benchmark. Below we will show the needed steps to achieve the goal of the assignment.

---
# Lab Session

1. Download the dataset and understand the format
	* We will use Berkeley Segmentation Benchmark
	* The data is available at the following [link](http://www.eecs.berkeley.edu/Research/Projects/CS/vision/grouping/BSR/BSR_bsds500.tgz). Note, data cannot be downloaded from original site, check it on web archive.
	* The dataset has 500 images. The test set is 200 images only. We will report our results on the test set only.

2. Visualize the image and the ground truth segmentation
	* Write your own function that reads an image and display an image with its associated ground truth segmentation(s).

3. Segmentation using K-means
Every image pixel is a feature vector of 3-dimension {R,G,B}. We will use this feature
representation to do the segmentation.
	* We will change the K of the K-means algorithm between {3,5,7,9,11} clusters. You will produce different segmentations and save them as colored images. Every color represents a certain group cluster) of pixels.
	* We will evaluate the result segmentation using F-measure, Conditional Entropy. for image I with M available ground-truth segmentations. For a clustering of K-clusters you will report your measures M times and the average of the M trials as well. Report average per dataset as well.
	* Display good results and bad results for every configuration in a,b. Discuss

4. Normalized-Cut Segmentation
	* Use RBF kernel with gamma = {1,10} to generate the similarity graph of the pixels. (Be careful of the graph size, you might need to resize the image first if you don’t have 4GB of RAM).
	* Use Similarity graph as the 5-NN graph. Where Sim(xi,xj)=1 iff xj is one of the nearest three points to xi (or vise versa ). xi is the (Ri,Gi,Bi) coordinates for a pixel xi.
	* In every of the above cases set the number of clusters ={3,5,7,9,11}. You will produce different segmentations and save them as colored images. Every color represents a certain group (cluster) of pixels.
	* We will evaluate the result segmentation using F-measure, Conditional Entropy. for image I with M available ground-truth segmentations. For a clustering of K-clusters you will report your measures M times and the average of the M trials as well. Report average per dataset as well.
	* Display good results and bad results for every configuration in a,b. Discuss.

5. Big Picture
	* Select a set of five images and display their corresponding ground truth against your segmentation results using K-means at K=5. Comment on the results.
	* Select the same five images and display their corresponding ground truth against your segmentation results using Normalized-cut for the 5-NN graph, at K=5. Comment on the results.
	* Select the same five images and contrast your segmentation results using Normalized-cut for the 5-NN graph, at K=5 versus using K-means at K=5. Comment on the results.

---
