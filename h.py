import threading
import time

def function_1():
    print("Function 1")
    time.sleep(1)

def function_2():
    print("Function 2")
    time.sleep(1)

def function_3():
    print("Function 3")
    time.sleep(1)

def function_4():
    print("Function 4")
    time.sleep(1)

# Create threads
thread1 = threading.Thread(target=function_1)
thread2 = threading.Thread(target=function_2)
thread3 = threading.Thread(target=function_3)
thread4 = threading.Thread(target=function_4)

# Start threads
thread1.start()
thread2.start()
thread3.start()
thread4.start()

# Wait for threads to complete
thread1.join()
thread2.join()
thread3.join()
thread4.join()