from time import time

import time
n = 20
ind = False

while True:
    time.sleep(0.5)
    
    if ind:
        
        print(" " * n, end="")
        print("******")
        n = n +1
    
    else : 
        
        print(" " * n, end="")
        print("******")
        n = n-1
    
    if n == 20:
        ind = False
    if n == 1:
        ind = True
    
    


    



