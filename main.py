import numpy as np
import os
from PIL import Image
from sklearn.preprocessing import LabelEncoder
from tensorflow.keras.models import load_model


def getPrediction(filename):
    
    classes = ['Mild Demented', 'Moderate Demented', 'Non Demented', 'Very Mild Demented']

    le = LabelEncoder()
    le.fit_transform(classes)    
    
    model=load_model("models/Alzheimer_Detection_CNN.h5")
    
    img_path = os.path.join(os.path.abspath("static/images"), filename)
    img = np.asarray(Image.open(img_path))
    img = img.T.copy()
    
    if len(img.shape)==3: #for RGB images
        img = img[np.newaxis, ...]
        
    else: #for gray-scale images
        img = img[..., np.newaxis]
        img = np.concatenate((img,img,img), axis=2)
        img = img[np.newaxis,...]
    
    prediction = model.predict(img)                    
    predicted_class = le.inverse_transform([np.argmax(prediction)])[0]
    return predicted_class

#print(getPrediction(filename="MildDementedSample.jpg"))