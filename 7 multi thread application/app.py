import time 
import threading  
from threading import *  

def cal_sqre(num): 
    print(" Calculate the square root of the given number")  
    for n in num:    
        time.sleep(0.3)   
        print(' Square is : ', n * n)  
  
def cal_cube(num):   
    print(" Calculate the cube of the given number")  
    for n in num:   
        time.sleep(0.3)   
        print(" Cube is : ", n * n *n)  
  
ar = [4, 5, 6, 7, 2]   
  
t = time.time()   

# Create threads for calculating squares and cubes
th1 = threading.Thread(target=cal_sqre, args=(ar, ))  
th2 = threading.Thread(target=cal_cube, args=(ar, ))  

# Start the threads
th1.start()  
th2.start()  

# Wait for the threads to finish
th1.join()  
th2.join()  

# Calculate and print the total time taken by threads to execute
print(" Total time taken by threads is:", time.time() - t) 

# Print a message indicating that the main thread is executing again
print(" The main thread has resumed execution.") 

# Print a message indicating that both threads have finished executing
print(" Threads 1 and 2 have finished their execution.")
