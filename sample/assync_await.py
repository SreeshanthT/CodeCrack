import asyncio

async def print_B(): #Simple async def
    print("B")

async def main_def():
    print("A")
    await asyncio.gather(print_B())
    print("C")
asyncio.run(main_def())



async def eternity():
   # Sleep for 60 minutes
   await asyncio.sleep(3)
   print('yay!')


async def main():
   try:
       # timeout if function takes longer than 1 second
       await asyncio.wait_for(eternity(), timeout=2.0)
   except asyncio.TimeoutError:
       print('timeout!')


asyncio.run(main())
