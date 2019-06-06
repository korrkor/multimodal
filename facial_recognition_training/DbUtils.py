import pymysql

#import Error
class DbUtils:

    host='localhost'
    database='doorbell_notification'
    user='root'
    password=''
    
    def __init__(self, name="", blob=""): 
        self.name = name
        self.blob = blob
        
    
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

    def commit_to_db(self):
        cursor, connection = self.db_connection()
        sql_query = "INSERT INTO recogniser_details (`name`, `identifier_blob`) VALUES (%s,%s)"
        # print()
        insert_tuple = (self.name,self.blob)
        cursor.execute(sql_query, insert_tuple)
        print("INSERT INTO recogniser_details (`name`, `identifier_blob`) VALUES (%s,%s)")

        connection.commit()
        return True
        

    
    

                
    
# profile = Profile()
# profile.get_active_profiles()


    
      
      
      
  
  

