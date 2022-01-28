import time

def collatz(num):
    if num % 2 == 0:
        num = num //2
    else: num = 3*num+1
    return num



n = input("Enter the number here: ")

n = int(n)

while True:
    if n != 1:

        n = collatz(n)
        print(n)
    else: break

    time.sleep(0.5)




