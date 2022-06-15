from turtle import color
from keras.models import load_model
from PIL import Image, ImageOps
import matplotlib
import numpy as np
matplotlib.use('Agg')
import matplotlib.pyplot as plt 
import os


def process_img(img,filename): 
    np.set_printoptions(suppress=True) 
    model = load_model('model.h5')
    data = np.ndarray(shape=(1, 256, 256, 3), dtype=np.float32) 
    image = Image.open(img) 
    size = (256, 256)
    image = ImageOps.fit(image, size, Image.ANTIALIAS) 
    image_array = np.asarray(image) 
    normalized_image_array = (image_array.astype(np.float32) / 255.0) 
    data[0] = normalized_image_array 
    prediction = model.predict(data) 
    pred_new = prediction[0]
    pred = max(pred_new)  
    index = pred_new.tolist().index(pred) 
    
    left = [1, 2, 3, 4, 5] 
    height = pred_new.tolist()
    new_height = []
    for i in height:
        new_height.append(round(i, 2) * 100)
    #k=new_height.sort() 
    c=[]
    for i in range(len(new_height)):
        if new_height[i]==max(new_height):
            c[i]='g' 
    tick_label = ['normal', 'mild', 'moderate', 'severe', 'proliferative'] 
    plt.bar(left, new_height, tick_label=tick_label, width=0.5,color=c) 
    plt.xlabel('Severity')
    plt.ylabel('Probability')
    plt.title('Diabetic Retinopathy') 
    plt.savefig(os.path.dirname(__file__) + '\static\output\graph.png') 
    plt.clf()
    result = []

    if index == 0:
        result.append("Normal")
    elif index == 1:
        result.append("Mild")
    elif index == 2:
        result.append("Moderate")
    elif index == 3:
        result.append("Severe") 
    elif index == 4:
        result.append("Proliferative")  

    accuracy = round(pred, 2) 
    result.append(int(accuracy * 100)) 
    for i in pred_new:
        result.append(int(i*100))  

    return result 
