# Hikvision security cameras vulnerability 2014-2016 (ICSA-17-124-01) Tool

# Description : 
The tool has been writen in pyhton. The purpose of this is something more than just a simple tool, options you can have access to are : 
1- changing the password
2- saving the encrypted configure file and also the decrypted one 
3- have access to snapshot and also the live stream of camera 
4- getting extra details like : 
    1- open ports
    2- country, city, org, isp and asn
    3- location
    4- ip range, network address, broadcast address
    5- device name, device id, model, serial number
    6- mac address
    
    

# How to work with it? 
 you just need to enter the target security camera ip and thats all ... the tool checks the ip for ICSA-17-124-01 vulnerability and if it had the vulnerability the options menu be activated for you 
 ** you will need a shodan account ... so it you don't have a one, create it **


# The installation guide :

1- go to the requirements.txt path and in terminal type : 
pip install -r requirements.txt
2- open extra_details.py and set your Shodan account Username and Password, and save it 
3- Everything done ... use python ./main.py in path terminal to run the tool 
