#Question 1
#Write a function to print "hello_USERNAME!" USERNAME is the input of the function. The first line of the code has been defined as below.

def hello_name(user_name):
    print("hello_"+user_name)
    

#Question 2
#Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing

def first_odds():
    for num in range(1, 101, 2):
        print(num)
    
    
    
# #Question 3
# #Please write a Python function, max_num_in_list to return the max number of a given list. The first line of the code has been defined as below.

def max_num_in_list(a_list):
    return max(a_list)
    
#Question 4
#Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. The return should be boolean Type (true/false).

def is_leap_year(a_year):
    if(a_year%100==0 and a_year%400==0):
        return True
    elif(a_year%4==0 and a_year%100!=0):
        return True
    else:
        return False

#Question 5
#Write a function to check to see if all numbers in list are consecutive numbers. For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. The return should be boolean Type.

def is_consecutive(a_list):
    for i in range(0,len(a_list)-1):
        if(a_list[i]!=a_list[i+1]-1):
            return False
    return True


hello_name("KAVYA") #Q1
print("")
print("")

first_odds() #Q2
print("")
print("")


my_list=[1,2,3,4,5,6] #Q3
print("Max value in the list",my_list," is ",max_num_in_list(my_list))
print("")
print("")


year=int(input("Enter a year to check if it is a leap year : ")) #Q4
print("The year ",year,"is a leap year : ",is_leap_year(year))
print("")
print("")

my_list1=[1,2,3,4]#Q5
print("This list ",my_list1," has consecutive values : ",is_consecutive(my_list1))
