import json
from pathlib import Path


class EmailConfig:
    
    def __init__(self, name ="", receiver_email = ""):
      self.name = name
      self.sender_email = "korkorkoteyafutu@gmail.com"
      self.receiver_email = receiver_email
      self.password = "62131121"
      self.smtp_server = "smtp.gmail.com"
      self.port = 587
    
    
    def check_file(self):
        my_file = Path("config.txt")
        if my_file.is_file():
            return True
        return False

    def create_config_file(self):
        if self.check_file():
            with open('config.txt') as json_file:
                config = json.load(json_file)
                config.append({   'name':self.name,
                'sender_email': self.sender_email,
                'password':self.password,
                'smtp_server': self.smtp_server,
                'port' : self.port,
                'receiver_email': self.receiver_email
            })
        else:
            config = [
                {   'name':self.name,
                    'sender_email': self.sender_email,
                    'password':self.password,
                    'smtp_server': self.smtp_server,
                    'port' : self.port,
                    'receiver_email': self.receiver_email
                }
            ] 
        with open('config.txt', 'w') as outfile:
            json.dump(config, outfile) 
    
    def get_email_config(self): 
        print("geting email config")
        with open('config.txt') as json_file:  
            print("file open")
            data = json.load(json_file)
            print("thsis i the file ", data)
        return data

# config = EmailConfig()
# # print(config.get_email_config())
# for data in config.get_email_config():
#     print(data["name"])
        
        
        
        
        

