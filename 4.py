def getNumberList(filename): # Define a function that returns a list of numbers with filename as paramater
    with open(filename,'r') as f:
        strList = f.read().split()
        numberList = [int(num) for num in strList]
    return numberList

def getAverage(filename, func): # Define a function that returns the average of the numbers from a file, with the filename and the function that returns numbers as parameters
    numbers = func(filename)
    return sum(numbers)

def main():
    filename = input("Input the file name: ")
    average = getAverage(filename, getNumberList)
    print(average)

main()

v = open('bb.txt','r')


import pickle
filename = input('Enter file name: ')
with open (filename, "wb") as F1:
    while True:
        op = int (input ("Enter 1 to add data, 0 to quit"))
        if (op == 1):
            size = int(input ("Enter byte size : "))
            order = int (input ("Enter byte order : "))
            pickle.dump([size,order],F1)
        elif op == 0:
            break
#4c
import pickle
F1 =  open ("file.dat", "rb")
while True:
    try:
        l = pickle.load(F1)
        print (l[0] + l[1])
    except EOFError:
        break
F1.close()