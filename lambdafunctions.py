#used in a function within a function 

#can take any number of arguments (on the left side) but are a single expression (a + 10)

#returns an object 

#the variable is a function name 

#used when you need a function for a short period of time
'''
def myfunc(n):
    return lambda a : a * n 

mydoubler = myfunc(2) #n = 2, what is a?

print(mydoubler(11)) #a is 11, output 22

def myfunc(n):
    return lambda a : a * n 

mytripler = myfunc(3)

print(mytripler(11)) #whatever number you give it, it will triple it
                    #a is provided by the program because it will change
                    #you don't pass a as an argument because a will change a lot

def myfunc(n):
    return lambda a : a * n 

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(3))

#lamdba functions can be used to apply filters
numbers_list = [2,4,6,8,10,11,4,12,7,13,17,0,3,21]
filtered_list = list(filter(lambda num: (num > 7), numbers_list)) #if the numbers in the numbers list are greater than 7, add it to a new list

numbers_list = [2,4,6,8,10,11,4,12,7,13,17,0,3,21]
filtered_list = list(map(lambda num: (num % 2), numbers_list)) #map goes through each, doesn't filter
print(filtered_list) #return the remainders when each number in the list is divided by 2

x = lambda a: a + 10
print(x(5)) #x is an instance of that object, output 5
'''
