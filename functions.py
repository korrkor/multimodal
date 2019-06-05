from scipy.io.wavfile import read
import smtplib, ssl
from EmailConfig import EmailConfig



def calc_distances(sound_file):
    #The minimun value for the sound to be recognized as a knock
    min_val = 5000 
    fs, data = read(sound_file)
    data_size = len(data)
    
    #The number of indexes on 0.15 seconds
    focus_size = int(0.15 * fs)
    focuses = []
    distances = []
    idx = 0
    print("buggin", data)
    
    print("length of data", len(data))
    print("data at ",data[0])
    while idx < data_size:
        if data[idx] > min_val:
            mean_idx = idx + focus_size // 2
            focuses.append(float(mean_idx) / data_size)
            if len(focuses) > 1:
                last_focus = focuses[-2]
                actual_focus = focuses[-1]
                distances.append(actual_focus - last_focus)
            idx += focus_size
        else:
            idx += 1 
    return distances  


def accept_test(pattern, test, min_error):
    if len(pattern) > len(test):
        return False
    for i, dt in enumerate(pattern):
        if not dt - test[i] < min_error:
            return False
    return True

def send_email(message,receipient_list): 
    config = EmailConfig()
    data = config.get_email_config()
    for user in data:
        if user['name'] in receipient_list:
            try:
                server = smtplib.SMTP(user['smtp_server'],user['port'])
                server.ehlo()
                server.starttls()
                server.login(user['sender_email'], user['password'])
                server.sendmail(user['sender_email'], user['receiver_email'], message)        
            except Exception as e:
                print("did not send")
                print(e)
                return False
            else:
                print("email sent with success")
    return True           

# test = calc_distances("test1.wav")
# pattern = calc_distances("knock.wav")
# print(accept_test(pattern, test, 0.1))

# from Profile import Profile
# profile = Profile()
# records = profile.get_active_profiles()
# print("this is records ",["korkor","kweiks"])
# send_email("this is a trial message with many recepients", records) 






