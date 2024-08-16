# async 
import asyncio, time

def count():
    print("One")
    time.sleep(1)
    print("Two")

def main():
    #await asyncio.gather(count(), count(), count())
    for _ in range(13):
        count()

if __name__ == "__main__":
    #import time
    s = time.perf_counter()
    #asyncio.run(main())
    main()
    elasped = time.perf_counter() - s
    print(f"{__file__} executed in {elasped: 0.2f} seconds.")
