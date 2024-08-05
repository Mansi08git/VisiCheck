#importing libraries
import cv2
import os
import pickle
import face_recognition
import numpy as np

#importing images of students to list
folderpath = 'images'
pathlist = os.listdir(folderpath)
print(pathlist)

imglist=[]
stu_name =[]

for path in pathlist:
    imglist.append(cv2.imread(os.path.join(folderpath,path)))
   #print(os.path.splitext(path)[0]) #to get only names
   #split krke stuname mai daal diya
    stu_name.append(os.path.splitext(path)[0])

print(stu_name)
print(len(imglist))

#Encoding images
#opencv uses bgr 
#face_recognition use rgb 
#to convert it , encoding should be done

def findEncodings(imagelist):
    encodelist =[]
    for img in imagelist:
        img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodelist.append(encode)
    return encodelist

print("Encoding start")
encodeList= findEncodings(imglist)
encode_list =[encodeList,stu_name]
#print(encodeList)
print("Encoding complete")


#dumping all the encodings to pickle file

file = open("Encoding.p",'wb')
pickle.dump(encode_list,file)
file.close()


