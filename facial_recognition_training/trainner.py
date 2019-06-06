# -*- coding: utf-8 -*-
import cv2,os
import numpy as np
from PIL import Image

class Trainer:  
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    global detector
    detector = cv2.CascadeClassifier("C:\\Users\\Probook6570b\\Documents\\applications and setups\\opencv\\sources\\data\\haarcascades\\haarcascade_frontalface_default.xml");
    
    def getImagesAndLabels(path):
        #get the path of all the files in the folder
        print("this is the path ", path)
        imagePaths=[os.path.join(path,f) for f in os.listdir(path)] 
        #create empth face list
        faceSamples=[]
        #create empty ID list
        Ids=[]
        names=[]
        #now looping through all the image paths and loading the Ids and the images
        for imagePath in imagePaths:
            #loading the image and converting it to gray scale
            pilImage=Image.open(imagePath).convert('L')
            #Now we are converting the PIL image into numpy array
            imageNp=np.array(pilImage,'uint8')
            #getting the Id from the image
            Id=int(os.path.split(imagePath)[-1].split(".")[1])
            name=str(os.path.split(imagePath)[-1].split(".")[3])
            print("this is the id" + str(Id) +"and this is the name" + str(name))
            # extract the face from the training image sample
            faces=detector.detectMultiScale(imageNp)
            #If a face is there then append that in the list as well as Id of it
            for (x,y,w,h) in faces:
                faceSamples.append(imageNp[y:y+h,x:x+w])
                Ids.append(Id)
                names.append(name)   
        return faceSamples,Ids 
      
    faces,Ids = getImagesAndLabels('dataSet')
    recognizer.train(faces, np.array(Ids)) 
    recognizer.write('trainner/trainner.yml')
              



