import math

#Function to find factors of each element in a given list
def factor(inputlist):
    #Step1: Converting the input list into the dictionary
    d = dict((i,1) for i in inputlist)
    #Step2: A for loop to itterate all the elements in the list
    for j in range(len(inputlist)):
        key = inputlist[j] #step3: Assigning the key for the dictionary
        #Step4: Creating a to append all the factors of a given element into a single list
        templist = [1,key] #1 and the number itself are factors
        #Step5: Logic to check all the numbers from 2 to the number divided by 2 to save the number of iterations and hence better time complexity
        for i in range(2, math.floor(key/2)):
            if key % i == 0: #Finding remainders of each element  
                templist.append(i) #appending all the factors to the templist
        d[key] = templist #Assigning the above list as values of the key
        d[key].sort() #Step6: sorting in the ascending order
    print(d)

#Function to find the position of a given element by using Binary Search method. Reference: "https://github.com/zhiwehu/Python-programming-exercises/blob/master/100%2B%20Python%20challenging%20programming%20exercises.txt"
def binarySearch(inputlist, element):
    #Defining 2 variables first and last for the elements in the list
    first = 0
    last = len(inputlist)-1
    index = -1 #Definng the variable index that will store the index position of the element
    #Step1: Iterate till you find the element
    while last>=first and index==-1:
        #finding the mid value as this is a Binary Search
        mid = int(math.floor((last+first)/2.0))
        #If the element is the mid element; index value is set
        if inputlist[mid]==element:
            index = mid
        #If the number is lesser than the mid value; the next list will be from 0th element to mid - 1 element
        elif inputlist[mid]>element:
            last = mid-1
        #If the number is Greater than the mid value; the next list will be from mid+1 element to last element
        else:
            first = mid+1
    #Returning the index if element is found; -1 index indicates the element is not found
    return index+1

user_input = input("Please enter five numbers in ascending order separated by a single space only: ")
inputlist = [int(i) for i in user_input.split(',')]
print("Factors of each element:")
factor(inputlist)
print("Position of the element is :", binarySearch(inputlist, 110))