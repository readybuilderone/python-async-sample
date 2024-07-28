import asyncio
import time

async def brewCoffee():
    print("Start brewCoffee()")
    await asyncio.sleep(5)
    print("End brewCoffee()")
    return "coffee ready"

async def toastBread():
    print("Start toastBread()")
    await asyncio.sleep(3)
    print("End toastBread()")
    return "bread ready"

async def main():
    start_time = time.time()
    
    batch = asyncio.gather(brewCoffee(), toastBread())
    coffee_result, bread_result = await batch
    
    end_time = time.time()
    elapsed_time = end_time - start_time
    print("Coffee: " + coffee_result)
    print("Bread: " + bread_result)
    print("Total time: " + str(elapsed_time))
 
if __name__ == "__main__":   
    asyncio.run(main())