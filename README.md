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


### Overview

In this project, knowledge  in deep neural networks and convolutional neural networks is used to classify traffic signs. A model is trained and alidated so it can classify traffic sign images using the [German Traffic Sign Dataset](http://benchmark.ini.rub.de/?section=gtsrb&subsection=dataset). After the model is trained, it is tried out on images of German traffic signs that you find on the web.

The goals / steps of this project are the following:
* Load the data set
* Explore, summarize and visualize the data set
* Design, train and test a model architecture
* Use the model to make predictions on new images
* Analyze the softmax probabilities of the new images

### Load the data set

[German Traffic Sign Dataset](http://benchmark.ini.rub.de/?section=gtsrb&subsection=dataset) is the data set used in this project, It contains the following information:

![alt text][image0]

### Explore, summarize and visualize the data set

Data set is composed of 43 different classes:

| ClassId	| SignName |
| --- | :-------------: |
0	      | Speed limit (20km/h)
1	      | Speed limit (30km/h)
2	      | Speed limit (50km/h)
3	      | Speed limit (60km/h)
4	      | Speed limit (70km/h)
5	      | Speed limit (80km/h)
6	      | End of speed limit (80km/h)
7	      | Speed limit (100km/h)
8	      | Speed limit (120km/h)
9	      | No passing
10	    | No passing for vehicles over 3.5 metric tons
11	    | Right-of-way at the next intersection
12	    | Priority road
13	    | Yield
14	    | Stop
15	    | No vehicles
16	    | Vehicles over 3.5 metric tons prohibited
17	    | No entry
18	    | General caution
19	    | Dangerous curve to the left
20	    | Dangerous curve to the right
21	    | Double curve
22	    | Bumpy road
23	    | Slippery road
24	    | Road narrows on the right
25	    | Road work
26	    | Traffic signals
27	    | Pedestrians
28	    | Children crossing
29	    | Bicycles crossing
30	    | Beware of ice/snow
31	    | Wild animals crossing
32	    | End of all speed and passing limits
33	    | Turn right ahead
34	    | Turn left ahead
35	    | Ahead only
36	    | Go straight or right
37	    | Go straight or left
38	    | Keep right
39	    | Keep left
40	    | Roundabout mandatory
41	    | End of no passing
42	    | End of no passing by vehicles over 3.5 metric

Test, training and validation dataset are plotted using histogram, showing how many sample are present per ClassId.

Training dataset           | Test dataset              | Validation dataset
:-------------------------:|:-------------------------:|:-------------------------:
![alt text][image1] |       ![alt text][image2] |      ![alt text][image3] 

From the images visuazlization, it is possible to notice that there are some very bright ones (8418) and some dark ones (9911). Background presents the same problem, passing from a one with sky (16852) to a one with a dark backgraound (9911). Also zoom is different from image to image. All the images are quite blurry.

![alt text][image4] 

Imbalanced dataset can lead to completely ignoring the minority class in favor of the majority class. This is happening in current data set, so a data augmentation is needed.
Up-sampling is the process of randomly duplicating observations from the minority class in order to reinforce its signal.
Since the highest number of occurancy for a class is 2010, every class will be bringed to 2500 adding blurred or rotated images.

#### a) Augment the dataset. This is done in 2 different ways:
##### a) Image filtering 

![alt text][image5] 

##### b) Image rotation

![alt text][image6] 

Data flipping is not used because can change traffic sign meaning, leading to uncorrect labeling.
Important is to classify new immages correctly.

#### b) Data processing: all 3 data set should be normalized and randomized.
In addition here, since brightness plays an important role, a contrast equalization is performed, together with the data noralization (0 mean and standard deviation equal to 1) and the data set randomization

### a) Normalization 
### b) Contrast equalization 
### c) Randomization

### Design, train and test a model architecture

#### Architecture
It is a LeNet architecture modified with dropout for convolutional and fully connected layers. At the end, the L2 regularization is applied in order to prevent overfitting.

##### Layer 1: Convolutional.
     Input = 32x32x1. Output = 32x32x8.
     in_height = 32
     in_width  = 32
     filter_height = 5
     filter_width  = 5
     filter_depth  = 8
     out_height = 32 
     out_width  = 32 

##### Activation. 
     ReLu.

##### Dropout.
     keep_p_convolutional = 0.9
    
##### Layer 2: Convolutional.  
     Input = 32x32x8. Output = 30x30x16.
     in_height = 32
     in_width  = 32
     filter_height = 3
     filter_width  = 3
     filter_depth  = 16
     out_height = 30
     out_width  = 30 

##### Activation. 
     ReLu.

#### Pooling. 
     Input = 30x30x16.
     ((30-3+2*0)/2) + 1 = 14
     Output = 14x14x16.
    
##### Dropout.
     keep_p_convolutional = 0.9


##### Layer 3: Convolutional.  
     Input = 14x14x16. Output = 12x12x32.
     in_height = 14
     in_width  = 14
     filter_height = 3
     filter_width  = 3
     filter_depth  = 32
     out_height = 12
     out_width  = 12 


##### Activation. 
     ReLu.
    
#### Pooling. 
     Input = 12x12x32. 
     ((12-2+2*0)/2) + 1 = 6
     Output = 6x6x32.

##### Dropout.
     keep_p_convolutional = 0.9

##### Flatten. Flatten the output shape of the final pooling layer such that it's 1D instead of 3D. 
     6x6x32 = 1152

##### Layer 4: Fully Connected.
     Input  = 1152. 
     Output = 512.

##### Activation. 
     ReLu.

##### Dropout.
     keep_p_fully_connected = 0.6


##### Layer 5: Fully Connected. 
     Input  = 512. 
     Output = 256.

##### Activation. 
     ReLu.
    
##### Dropout.
     keep_p_fully_connected = 0.6

##### Layer 6: Fully Connected. 
     Input  = 256. 
     Output = 128.

##### Activation. 
     ReLu.

##### Dropout.
     keep_p_fully_connected = 0.6

##### Layer 7: Fully Connected (Logits). 
     Input  = 128. 
     Output = 43.  

##### L2 regularization


#### Hyper-Paramters
* Learning rate = 1e-3
* Learning rate decay = 1e-5*2
* Adam Optimizer
* Beta = 1e-2
* Epochs = 32
* Batch size = 128

The model gave satisfying results

![alt text][image7] 

### Use the model to make predictions on new images

The model is behaving pretty well with , correctly predicting 4 images out of 5. This behavior is expected, since the images chosen are high quality images with a high contrast background. The image that is mistakenly predicted is the one containing also the web site source. I wanted to include this image to see if this could be a source of error and see how the model classify this image.

Image 4         | Image 5    
:-------------------------:|:-------------------------:
![alt text][image8] |       ![alt text][image9]  










