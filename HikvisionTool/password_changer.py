import requests  
from requests.auth import HTTPBasicAuth 

def change_password(ip,username,user_id,current_password,new_password) :
    

    url = f'http://{ip}/ISAPI/Security/users/{user_id}'  
    
    xml_payload = f'''<?xml version="1.0" encoding="UTF-8"?>  
    <User xmlns="http://www.hikvision.com/ver20/XMLSchema" version="2.0">  
        <id>1</id> <!-- User ID for admin -->  
        <userName>{username}</userName>  
        <password>{new_password}</password>  
    </User>'''  

    try:  
        response = requests.put(url,headers={'Content-Type': 'application/xml'},
                                data=xml_payload,auth=HTTPBasicAuth(username, current_password))
        
        if response.status_code == 200:
            con = 'password changed succesfully'  
        else:  
            con = 'failed to change password'  

    except Exception as e:  
        con = 'an error acuured while sending request' 

    return con 
        
#change_password('185.99.214.37','admin',1,'Ahmadizadeh123','Ahmadizadeh')