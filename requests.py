import asyncio
import aiohttp
import matplotlib.pyplot as plt

async def make_request(session, url):
    async with session.get(url) as response:
        return await response.text()

async def main():
    url = "http://127.0.0.1:5000/rep"

    async with aiohttp.ClientSession() as session:
        tasks = [make_request(session, url) for _ in range(10000)]
        responses = await asyncio.gather(*tasks)
        
        


if __name__ == "__main__":
    asyncio.run(main())

    '''
    #Bar chart
    file_path = 'load_distribution.txt'
    dictionary={'0':0,'1':0,'2':0}
    with open(file_path,'r') as file:
        for line in file:
            line1=line.strip()
            dictionary[line1]=dictionary[line1]+1

    servers=['Server-0','Server-1','Server-2']
    plt.bar(servers,list(dictionary.values()))
    plt.xlabel('servers')
    plt.ylabel('Distribution')
    plt.title('Load Distribution among 3 severs upon 10,000 asyn requests')
    plt.show()
    '''
    