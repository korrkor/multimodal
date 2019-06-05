import pymysql
from EmailConfig import EmailConfig
#import Error
class Profile:
  host='localhost'
  database='doorbell_notification'
  user='root'
  password=''
  
  def __init__(self, name="", email="", pin=""): 
    self.name = name
    self.email = email
    # self.email_password = email_password
    self.pin = pin
   
  
  def log_in(self):  
    cursor, connection = self.db_connection()
    cursor.execute("Select * from profile_details where name = '" + self.name +"' and pin = '" + self.pin +"';")
    record = cursor.fetchone()
    return record
  
  def db_connection(self):
    try:
      connection = pymysql.connect(host=self.host,
                             database=self.database,
                             user=self.user,
                             password=self.password)
      if connection.open:
        db_Info = connection.get_server_info()
        print("Connected to MySQL database... MySQL Server version on ",db_Info)
        cursor = connection.cursor()
        return cursor, connection 
    except:
     print ("Error while connecting to MySQL")
     return False 
              
  def create_profile(self):
    try:
      cursor, connection = self.db_connection()
      sql_insert_query = "INSERT INTO profile_details (`name`, `email`, `pin`, `status`) VALUES (%s,%s,%s,%s)"
      insert_tuple = ( self.name,self.email,self.pin, 0)
      cursor.execute(sql_insert_query, insert_tuple)
      connection.commit()

      # *********create config file*******************
      config = EmailConfig(name = self.name, receiver_email=self.email) 
      config.create_config_file()
      return True
    except:
      return False 

  def activate_monitor(self,user):
      try:
        cursor, connection = self.db_connection()
        cursor.execute("Update profile_details set status = 1 where name ='" + user +"';")
        connection.commit()
        return True
      except:
        return False 

  def get_active_profiles(self):
      try:
        profile_list = []
        cursor, connection = self.db_connection()
        cursor.execute("Select name from profile_details where status = 1;")
        record = cursor.fetchall()
        for r in record:
          profile_list.append(r[0])
        
        return profile_list
      except:
        return False 

    
# profile = Profile()
# profile.get_active_profiles()


    
      
      
      
  
  

