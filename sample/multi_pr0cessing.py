"""
# from multiprocessing import Pool - Note: if you use this, you have to create the process under `if __name__ == '__main__':
from multiprocessing.pool import ThreadPool as Pool
import time

def square(x):
    time.sleep(2)
    return x**2

def cube(x):
    time.sleep(2)
    return x**3

# if __name__ == "__main__": # uncomment this and add indentation on below code, if using Pool instead of ThreadPool
## without mult-processing
t = time.time()
res1 = list(map(square, [x for x in range(10)]))
res2 = list(map(cube, [x for x in range(10)]))
print('Without multi-processing', time.time()-t)


## with multi-processing
p = Pool()
t = time.time()
res1 = p.map_async(square, [x for x in range(10)])
res2 = p.map_async(cube, [x for x in range(10)])
print('With multi-processing', time.time()-t)

t = time.time()
print([res1.get(), res2.get()])
print(f"time took for unpacking result: {time.time()-t}")
"""

# import multiprocessing
  
# def print_cube(num):
#     """
#     function to print cube of given num
#     """
#     print("Cube: {}".format(num * num * num))
  
# def print_square(num):
#     """
#     function to print square of given num
#     """
#     print("Square: {}".format(num * num))
  
# if __name__ == "__main__":
#     # creating processes
#     p1 = multiprocessing.Process(target=print_square, args=(10, ))
#     p2 = multiprocessing.Process(target=print_cube, args=(10, ))
  
#     # starting process 1
#     p1.start()
#     # starting process 2
#     p2.start()
  
#     # wait until process 1 is finished
#     p1.join()
#     p2.join()
#     # wait until process 2 is finished
  
#     # both processes finished
#     print("Done!")
    
from multiprocessing import Process
from time import sleep


def func1(j1):
    rocket = j1
    print('start func1')
    while rocket < 10:
        rocket += 1
        sleep(5)
        print(rocket, " -r1")
    print('end func1')


def func2(j2):
    rocket = j2
    print('start func2')
    while rocket < 30:
        rocket += 1
        sleep(2)
        print(rocket, " -r2")
    print('end func2')


if __name__ == '__main__':
    p1 = Process(target=func1, args=(0,))
    p1.start()
    p2 = Process(target=func2, args=(10,))
    p2.start()