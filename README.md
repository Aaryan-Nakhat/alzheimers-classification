
# Alzheimer's Disease Classification Using a Deep CNN Framework

Classifying Brain MRI Images into 4 categories of Alzheimers.


## Demo

![Demo](miscellaneous/demo-alzheimers.gif)


## Running the app

- Firstly run <code>pip install -r requirements.txt</code> to install all dependencies.
- Then run <code>python app.py</code> to open the web app.## Dataset

The dataset used for this project is taken from Kaggle (<a href = "https://www.kaggle.com/datasets/tourist55/alzheimers-dataset-4-class-of-images">dataset</a>).

The dataset consists of the following four classes of Alzheimer's MRI Images:

* Mild Demented
* Moderate Demented
* Non Demented
* Very Mild Demented
The dataset is comprised of around 6400 brain MRI Images.
## Network Architecture

The network architecture is illustrated below. 

![](miscellaneous/network_architecture.jpg)

A series of convolutional layer – convolutional layer – batch normalization layer – max pooling layer is considered as a convolutional block. 
* Five such convolutional blocks with the number of filters of the Conv2D layers by the factor of 2, ranging from 16 to 256. 
* A 3x3 kernel and relu activation function is used for all the convolutional layers.
* Each maxpooling layer uses a pool size of 3x3 with a stride of 2.
* A dropout layer with a dropout rate of 0.2 is used after each convolutional block.
* The convolutional blocks are followed by a global average pooling layer and a couple of dense layers for classification.## Dataset

The dataset used for this project is taken from Kaggle (<a href = "https://www.kaggle.com/datasets/tourist55/alzheimers-dataset-4-class-of-images">dataset</a>).

The dataset consists of the following four classes of Alzheimer's MRI Images:

* Mild Demented
* Moderate Demented
* Non Demented
* Very Mild Demented
The dataset is comprised of around 6400 brain MRI Images.
## Tech Stack

* Tensorflow
* Keras
* Flask
* Docker
* HTML & CSS


## Feedback

For any queries, feel free to reach me out at: aaryan.nakhat@gmail.com

<a href = "https://www.kaggle.com/datasets/tourist55/alzheimers-dataset-4-class-of-images">Linkedln</a>

