import requests
from requests.auth import HTTPDigestAuth
import re
import ipaddress  
from ipwhois import IPWhois  




headers = { 'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7'     
,'accept-language':'en-US,en;q=0.9,fa;q=0.8,de;q=0.7'
,'cache-control':'max-age=0'
,'content-type':'application/x-www-form-urlencoded'
,'cookie':'session=VCkK9nX1ezrBzAMMm721gjyQ4hGGB2Ouw14Xsd3uPPV5p8yK9Tw5sShk5VR54vNcVgSFy4BDe_9Xj-n6eRT3a4AFlXYAAAAAAAAASm96BmdHQdnBnnOA5cp9lCiMDGNvbnRpbnVlX3VybJSMGmh0dHBzOi8vYWNjb3VudC5zaG9kYW4uaW8vlIwHX2NzcmZ0X5SMKDU4ZTVmY2JjOTlhNDQzMDZkYmVlNjZmMzBhMWVlMTMwMDQzNjY0ZjmUdYeULg'
,'origin':'https://account.shodan.io'
,'priority':'u=0, i'
,'referer':'https://account.shodan.io/login'
,'sec-ch-ua':'"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"'
,'sec-ch-ua-mobile':'?0'
,'sec-ch-ua-platform':'"Windows"'
,'sec-fetch-dest':'document'
,'sec-fetch-mode':'navigate'
,'sec-fetch-site':'same-origin'
,'sec-fetch-user':'?1'
,'upgrade-insecure-requests':'1'
,'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'
}

data = { 'username':'YOUR USERNAME'  # PUT YOUR SHODAN ACCOUNT USERNAME HERE
,'password':'YOUR PASSWORD'          # PUT YOUR SHODAN ACCOUNT PASSWORD HERE
,'grant_type':'password'
,'continue':'https://account.shodan.io/login'
,'csrf_token':''
}


def shodan(ip) :
    with requests.Session() as s : 
        
        login = requests.get('https://account.shodan.io/login')
        csrf_token = re.findall(r'value="[\d,\w]*"',login.text)[1].split('=')[1][1:-1]
        data['csrf_token'] = csrf_token
        s.post('https://account.shodan.io/login',data=data,headers=headers)
        d = s.get(f'https://www.shodan.io/host/{ip}')

        ports = ' / '.join(re.findall(r'<a href="#\d*" class="bg-primary">(.*?)<\/a>',d.text))
        org = re.search(r'<a href="\/search\?query=org(.*?)>(.*?)<\/a>',d.text).group(2)
        isp = re.search(r'<a href="\/search\?query=isp(.*?)>(.*?)<\/a>',d.text).group(2)
        asn = re.search(r'<a href="\/search\?query=asn(.*?)>(.*?)<\/a>',d.text).group(2)
        country = re.search(r'<a href="\/search\?query=country(.*?)>(.*?)<\/a>',d.text).group(2)
        city= re.search(r'<a href="\/search\?query=city(.*?)>(.*?)<\/a>',d.text).group(2)

    return [f'open ports :\n{ports}',f'country :\n{country}',f'city :\n{city}',f'organisation :\n{org}',f'isp :\n{isp}',f'asn :\n{asn}']
    

def loc_finder(ip) : 
    
    response = requests.get(f"https://geolocation-db.com/json/{ip}&position=true").json()  
    loc = f'https://www.google.com/maps/?q={response['latitude']},{response['longitude']}'
    return [f'location link :\n{loc}']



def ip_detail(ip) : 
    
    ipwhois = IPWhois(ip)  
    details = ipwhois.lookup_rdap() 
    a = ipaddress.ip_network(details['asn_cidr'],strict=False)
    return [f'ip range :\n{details['asn_cidr']}',f'network address :\n{a.network_address}',f'broadcast address :\n{a.broadcast_address}']



def hikvision_detail(ip,port,username,password) : 
    url = f'http://{ip}:{port}/ISAPI/System/deviceInfo'
    hik_request = requests.Session()
    hik_request.auth = HTTPDigestAuth(username, password)
    response = hik_request.get(url).text
    result = re.findall(r'<(\w+)>(.*?)<\/\1>',response)
    return result


def get_all(ip,port,username,password) : 
    result = ''
    for i in [shodan(ip),loc_finder(ip),ip_detail(ip)] : 
        for detail in i : 
            result+=f'{detail}\n'
    for i in hikvision_detail(ip,port,username,password) :  
        if i[0] in ['deviceName','deviceID','model','serialNumber','macAddress'] :
            result+=f'{i[0]} :\n{i[1]}\n'
    return result

#print(get_all('109.122.229.103',80,'admin','abcd1234')) 