## Project: Build a Traffic Sign Recognition Program
[![Udacity - Self-Driving Car NanoDegree](https://s3.amazonaws.com/udacity-sdc/github/shield-carnd.svg)](http://www.udacity.com/drive)

[//]: # (Image References)

[image0]: ./write_up_images/image0.png "Data raw analysis"
[image1]: ./write_up_images/image1.png "Training data set visualisation"
[image2]: ./write_up_images/image2.png "Test data set visualisation"
[image3]: ./write_up_images/image3.png "Validation data set visualisation"
[image4]: ./write_up_images/image4.png "Random sample visualisation"
[image5]: ./write_up_images/image5.png "Augment taining dataset: blurring"
[image6]: ./write_up_images/image6.png "Augment taining dataset: rotation"
[image7]: ./write_up_images/image7.png "Model final accuracies"
[image8]: ./write_up_images/image8.png "Incorrectly classified web image"
[image9]: ./write_up_images/image9.png "Correctly classified web image"
[image10]: ./write_up_images/image10.png "Web images single accuracies"


Overview
---
In this project, knowledge  in deep neural networks and convolutional neural networks is used to classify traffic signs. A model is trained and alidated so it can classify traffic sign images using the [German Traffic Sign Dataset](http://benchmark.ini.rub.de/?section=gtsrb&subsection=dataset). After the model is trained, it is tried out on images of German traffic signs that you find on the web.

The goals / steps of this project are the following:
* Load the data set
* Explore, summarize and visualize the data set
* Design, train and test a model architecture
* Use the model to make predictions on new images
* Analyze the softmax probabilities of the new images
* Summarize the results with a written report

### Load the data set

[German Traffic Sign Dataset](http://benchmark.ini.rub.de/?section=gtsrb&subsection=dataset) is the data set used in this project, It contains the following information:

![alt text][image0]

### Explore, summarize and visualize the data set

Data set is composed of 43 different classes:

ClassId	SignName
0	      Speed limit (20km/h)
1	      Speed limit (30km/h)
2	      Speed limit (50km/h)
3	      Speed limit (60km/h)
4	      Speed limit (70km/h)
5	      Speed limit (80km/h)
6	      End of speed limit (80km/h)
7	      Speed limit (100km/h)
8	      Speed limit (120km/h)
9	      No passing
10	    No passing for vehicles over 3.5 metric tons
11	    Right-of-way at the next intersection
12	    Priority road
13	    Yield
14	    Stop
15	    No vehicles
16	    Vehicles over 3.5 metric tons prohibited
17	    No entry
18	    General caution
19	    Dangerous curve to the left
20	    Dangerous curve to the right
21	    Double curve
22	    Bumpy road
23	    Slippery road
24	    Road narrows on the right
25	    Road work
26	    Traffic signals
27	    Pedestrians
28	    Children crossing
29	    Bicycles crossing
30	    Beware of ice/snow
31	    Wild animals crossing
32	    End of all speed and passing limits
33	    Turn right ahead
34	    Turn left ahead
35	    Ahead only
36	    Go straight or right
37	    Go straight or left
38	    Keep right
39	    Keep left
40	    Roundabout mandatory
41	    End of no passing
42	    End of no passing by vehicles over 3.5 metric

Test, training and validation dataset are plotted using histogram, showing how many sample are present per ClassId.

Training dataset           | Test dataset              | Validation dataset
:-------------------------:|:-------------------------:|:-------------------------:
![alt text][image1] |       ![alt text][image2] |      ![alt text][image3] 
