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

user_input = input("Please enter five numbers in ascending order separated by a single space only: ")
inputlist = [int(i) for i in user_input.split(',')]
print("Factors of each element:")
factor(inputlist)