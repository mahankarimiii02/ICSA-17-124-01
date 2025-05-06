# Hikvision Security Cameras Vulnerability 2014-2016 (ICSA-17-124-01) Tool

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
    
    

# How to use it? 
You just need to enter the target camera's IP address, and that’s all... The tool will check the IP for the ICSA-17-124-01 vulnerability. If vulnerable, the options menu will be activated for you.

**Note: You will need a Shodan account. If you don’t have one, create one.**


# Installation Guide :

1. Go to the directory containing ```requirements.txt``` and run in the terminal : 
```bash  
pip install -r requirements.txt
```
2. Open ```extra_details.py``` and set your Shodan account username and password, then save the file.
3. Everything done ... To run the tool, use:
```bash
python ./main.py
```
# The warnings : 
1. The tool has been written for educational purposes only and nothing more. I'm not responsible for other usages.
2. Any governmental usage of this tool is strictly prohibited.
