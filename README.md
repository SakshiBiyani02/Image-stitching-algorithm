# Objective  
The goal of this task is to demonstrate how image stitching can be used to combine several 
photos of a newspaper's two-page spread into one high-resolution image. The task involves 
taking multiple pictures of the spread and using an image stitching algorithm to merge them 
into a single, clear document. The aim is to join the images smoothly while keeping the 
original content and layout intact. 
# Tech Stack 
## 1. Programming Language: 
Python 
## 2. Libraries and Key Functions: 
### OpenCV: 
#### cv2.ORB_create() – For ORB feature detection. 
#### cv2.BFMatcher() – For feature matching. 
#### cv2.Stitcher.create() – For stitching images together. 
#### cv2.drawKeypoints() – For visualizing keypoints. 
#### cv2.imwrite() – For saving images. 
#### cv2.line() – For drawing lines between keypoints. 
#### cv2.putText() – For adding text annotations. 
### NumPy: np.random.randint() – For generating random colors. 
## 3. Platform: Google Colab that uses files.upload() – For uploading images. 
## 4. Output Format: JPEG (.jpeg) – For saving the final stitched image. 
# Algorithm Used :  
The main algorithm used in this code is the Feature-Based Image Stitching algorithm. It 
uses ORB (Oriented FAST and Rotated BRIEF) for feature detection and description. The 
steps include detecting keypoints from multiple images, matching those keypoints across 
images, and using homography to align and stitch the images together. 
1. ORB (Oriented FAST and Rotated BRIEF): This is a fast feature detection algorithm 
designed to identify key points in an image and extract their descriptors. ORB is more 
efficient than other feature detectors like SIFT and SURF and works well for real-time 
applications. 
2. Brute Force Matcher (BFMatcher): This technique is used to match keypoints 
based on the similarity of their descriptors. The BFMatcher finds the best matches 
between two sets of keypoints and sorts them by distance. 
3. OpenCV Stitcher: OpenCV provides an in-built Stitcher class that takes a set of 
images and combines them into a single large image. It computes the transformation 
matrix (homography) to align the images. 
# Features 
1. ORB Feature Detection: 
#Detects keypoints and computes descriptors for each image. 
#ORB works efficiently by combining the FAST detector with BRIEF descriptors 
and adding orientation to make it rotation-invariant. 
2. Feature Matching with BFMatcher: 
o Matches features between images based on their descriptors using the 
BFMatcher algorithm. 
o Selects the best matches and visualizes them by drawing lines between 
corresponding points on the images. 
3. Dense Crisscross Feature Lines: 
o Draws colorful lines connecting keypoints and image corners. This feature 
provides a visual representation of the density and distribution of keypoints 
across the image. 
4. Enhanced Visualization: 
o Displays feature matches between two images, with highlighted keypoints 
and lines connecting them. 
o Incorporates text and colorful markers to enhance visual appeal. 
5. Image Stitching: 
o Uses OpenCV’s Stitcher.create() to stitch multiple images together based on 
detected keypoints. 
o If successful, it merges the images into one panoramic or wide-angle image. 
# Methodology 
## 1. Image Upload: 
o The process begins by uploading the images to the environment using the 
files.upload() method from the google.colab library. 
## 2. Image Loading: 
o The uploaded images are loaded into the system using OpenCV’s imread() 
function. If an image cannot be loaded, an error message is shown. 
## 3. Feature Detection: 
o Each image is converted to grayscale, which simplifies the image and 
enhances the feature detection process. 
o The ORB algorithm is used to detect keypoints (distinct points of interest in 
the image) and compute their descriptors (unique features for matching). 
## 4. Dense Crisscross Line Drawing: 
o The detected keypoints are connected with colorful lines, including 
connections to the four corners of the image, to visually enhance the feature 
map. This helps in understanding the distribution of features across the 
image. 
## 5. Feature Matching: 
o Using the Brute Force Matcher, the program matches the keypoints between 
two images based on their descriptors. 
o The top 100 best matches are selected and visualized on the images by 
drawing lines between corresponding keypoints. 
## 6. Image Stitching: 
o The cv2.Stitcher.create() function is used to stitch the images together. The 
function computes a homography (a transformation matrix) that aligns the 
images and merges them into a single panoramic image. 
## 7. Saving Output: 
o If the stitching is successful, the stitched image is saved as 
stitched_output.jpeg. Additionally, the feature matches and dense feature 
lines are saved as separate images. 
# Implementation  
1. Image Upload: Images are uploaded using the files.upload() method. 
2. Feature Detection: The ORB algorithm is used to detect keypoints and compute 
descriptors in grayscale images. 
3. Feature Matching: BFMatcher is employed to match keypoints between two images, 
and the best matches are drawn. 
4. Stitching: OpenCV’s Stitcher.create() function stitches images by calculating 
homographies and aligning the images. 
5. Saving Output: The final stitched image, along with visualizations of keypoints and 
feature matches, is saved as .jpeg files. 
# Result 
## Input
### Image 1
![img1](https://github.com/SakshiBiyani02/Image-stitching-algorithm/blob/main/img1.jpg)
### Image 2
![img2](https://github.com/SakshiBiyani02/Image-stitching-algorithm/blob/main/img2.jpg)
### Image 3
![img3](https://github.com/SakshiBiyani02/Image-stitching-algorithm/blob/main/img3.jpg)
### Image 4
![img4](https://github.com/SakshiBiyani02/Image-stitching-algorithm/blob/main/img4.jpg)
### Image 5
![img5](https://github.com/SakshiBiyani02/Image-stitching-algorithm/blob/main/img5.jpg)
### Image 6
![img6](https://github.com/SakshiBiyani02/Image-stitching-algorithm/blob/main/img6.jpg)
### Image 7
![img7](https://github.com/SakshiBiyani02/Image-stitching-algorithm/blob/main/img7.jpg)
### Image 8
![img8](https://github.com/SakshiBiyani02/Image-stitching-algorithm/blob/main/img8.jpg)
## Output
## Console output
![console_output](https://github.com/SakshiBiyani02/Image-stitching-algorithm/blob/main/console_output.png)
## Dense feature lines while processing the task
![dense](https://github.com/SakshiBiyani02/Image-stitching-algorithm/blob/main/dense_feature_lines_output.jpg)
## Final stitched output
![Output](https://github.com/SakshiBiyani02/Image-stitching-algorithm/blob/main/stitched_output%20(1).jpeg)
