# Hikvision security cameras vulnerability 2014-2016 (ICSA-17-124-01) Tool

# Description : 
The tool has been written in Python. Its purpose goes beyond just a simple tool; the list of options you can access includes:

1. Changing the password
2. Saving the encrypted configuration file and the decrypted one
3. Access to camera snapshots and live streams
4. Retrieving additional details such as:
    - Open ports
    - Country, city, organization, ISP, and ASN
    - Location
    - IP range, network address, broadcast address
    - Device name, device ID, model, serial number
    - MAC address
    
    

# How to work with it? 
 you just need to enter the target security camera ip and thats all ... the tool checks the ip for ICSA-17-124-01 vulnerability and if it had the vulnerability the options menu be activated for you  
 **you will need a shodan account ... so it you don't have a one, create it**


# The installation guide :

1. go to the requirements.txt path and in terminal type : 
```bash  
pip install -r requirements.txt
```
2. open extra_details.py and set your Shodan account Username and Password, and save it 
3. Everything done ... for running the tool you can use :
```bash
python ./main.py
```
# The warnings : 
1. The tool has been writen for educatonal purpose and nothing more ... it's you and your own responsibility
2. Any governmental usage from this tool is permanently not allowed 
