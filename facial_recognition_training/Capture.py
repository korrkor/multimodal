import numpy as np
import cv2

class Capture:
    
    def __init__(self):
#        print(details)
        self.path = "facial_recognition_training/"
        self.fname = "korkor"
        # self.lname = details["lname"]
        # self.rolename = details["rolename"]
        # self.institutionname = details["institutionname"]

        detector= cv2.CascadeClassifier('C:\\Users\\Probook6570b\\Documents\\applications and setups\\opencv\\sources\\data\\haarcascades\\haarcascade_frontalface_default.xml')
        cap = cv2.VideoCapture(0)
        Id = int(open(self.path+"ids.txt","r").read())
        
        sampleNum=0 
        # Capture.commit_to_db(self)
        while(True):
            ret, img = cap.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = detector.detectMultiScale(gray, 1.3, 5)
            for (x,y,w,h) in faces:
                cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        
        #incrementing sample number 
                sampleNum=sampleNum+1
                Id=Id+1 
                print("this is the sample mu ", sampleNum)
                #saving the captured face in the dataset folder
                cv2.imwrite(self.path+"dataSet/user."+str(Id)+'.'+str(sampleNum)+"."+str(self.fname)+".jpg",gray[y:y+h,x:x+w])
                
            cv2.imshow('frame',img)
            #wait for 100 miliseconds 
            if cv2.waitKey(100) & 0xFF == ord('q'):
                break
            # break if the sample number is morethan 20
            elif sampleNum>100: 
                file = open("ids.txt","w").write(str(Id))
#                commit_to_db()
                break
        cap.release()
        cv2.destroyAllWindows()    
    
#     def commit_to_db(self):
      
#       import pymysql
# #name = "korkor"
#       try:
#         connection = pymysql.connect(host='localhost',
#                              database='multimodal_ar',
#                              user='root',
#                              password='')
#         if connection.open:
#           db_Info = connection.get_server_info()
#           print("Connected to MySQL database... MySQL Server version on ",db_Info)
#           cursor = connection.cursor()
          
#           sql_insert_query = "INSERT INTO user_details (`firstname`, `lastname`, `position`, `company_name`, `identifier_blob`) VALUES (%s,%s,%s,%s,%s)"
#           insert_tuple = ( self.fname,self.lname,self.rolename,self.institutionname, self.fname)
# #          cursor.execute("select * from user_details where identifier_blob ='" + name + "';")
#           cursor.execute(sql_insert_query, insert_tuple)
#           connection.commit()
# #          record = cursor.fetchall()
#           print ("Your connected to - ")
          

#       finally:
#         print("MySQL connection is closed")
      
capture = Capture()

