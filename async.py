import asyncio
import time


async def hello(i):
    print(f'Hello .{i}..')

start_time = time.time()

async def main():
    tasks = []
    for i in range(10):
    
        # do nothing here but generate tasks
        task = hello(i)
        tasks.append(task)

        print(f'before if statement {i}', round((time.time() - start_time), 4))
        if i % 2 == 0:
            print(f'before doing tasks {i}', round((time.time() - start_time), 4))
            # run and get results for many tasks
            await asyncio.gather(*tasks)
            
            # remove previous tasks
            tasks = []
            print(f'before async sleep {i}', round((time.time() - start_time), 4))
            await asyncio.sleep(5)
            print(f'after async sleep {i}', round((time.time() - start_time), 4))
        print(f'after  if statement {i}', round((time.time() - start_time), 4))

    await asyncio.gather(*tasks)

asyncio.run(main())


########################################################################################


async def fetch(url, session, i):
    data = None
    while data is None:
        try:
            async with session.get(url) as r:
                r.raise_for_status()  # Raises stored HTTPError, if one occurred.
                data = await r.json()
                print(data['ResponseData'])
                
        except Exception as e:
            print(f'error No:{i} {str(e)}')
            await asyncio.sleep(10)  # sleep 10 seconds and try again


async def fetch_generator(urls,header):
    tasks, num_connectors = [], 10
    connector = aiohttp.TCPConnector(limit=num_connectors)
    async with aiohttp.ClientSession(headers=header, connector=connector) as session:

        for i in range(len(urls)):
            task = fetch_transactions_executor(urls[i], session, i, types)
            tasks.append(task) # no excute, just generate takes
               
            if ((i + 1) % num_connectors) == 0:
                await asyncio.gather(*tasks) # excute and wait all tasks finished
                tasks = [] # create an empty list

        # you now have all response bodies in this variable
        responses = await asyncio.gather(*tasks)
        return responses

loop = asyncio.get_event_loop()
future = asyncio.ensure_future(fetch_generator(urls_list, hearder))
loop.run_until_complete(future)
