#Example: 

eggs = (1,3,8,3,2)

my_listComprehension = [1/egg for egg in eggs]

print(my_listComprehension)

#Insert here the module/library import statements 

import math
import os 
import random

#1. Calculate the square number of the first 20 numbers. Use square as the name of the list.
# Remember to use list comprehensions and to print your results

square = [i**2 for i in range(20)]
print(square)

#2. Calculate the first 50 power of two. Use power_of_two as the name of the list.
# Remember to use list comprehensions and to print your results

power_of_two = [2**i for i in range(50)]
print(power_of_two)

#3. Calculate the square root of the first 100 numbers. Use sqrt as the name of the list.
# You will probably need to install math library with pip and import it in this file.  
# Remember to use list comprehensions and to print your results

sqrt = [i**2 for i in range(100)]
print(sqrt)

#4. Create this list [-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0]. Use my_list as the name of the list.
# Remember to use list comprehensions and to print your results

my_list = [i-10 for i in range(11)]
print(my_list)

#5. Find the odd numbers from 1-100. Use odds as the name of the list. 
# Remember to use list comprehensions and to print your results

odd = [i for i in range(100) if (i%2!=0)]
print(odd)

#6. Find all of the numbers from 1-1000 that are divisible by 7. Use divisible_by_seven as the name of the list.
# Remember to use list comprehensions and to print your results

divisible_by_seven = [i for i in range(1000) if (i%7==0)]
print(divisible_by_seven)

#7. Remove all of the vowels in a string. Hint: make a list of the non-vowels. Use non_vowels as the name of the list.
# Remember to use list comprehensions and to print your results
# You can use the following test string but feel free to modify at your convenience

teststring = 'Find all of the words in a string that are monosyllabic'
non_vowels = ''.join([i for i in teststring if not i in 'aeiouAEIOU'])
print(non_vowels)

#8. Find the capital letters (and not white space) in the sentence 'The Quick Brown Fox Jumped Over The Lazy Dog'. 
# Use capital_letters as the name of the list.  
# Remember to use list comprehensions and to print your results

teststring2 = 'The Quick Brown Fox Jumped Over The Lazy Dog'
capital_letters = [i for i in teststring2 if i in 'TQBFJOTLD']
print(capital_letters)

# Soluciones en clase

'''
import string
capital_letters_belen = [i for i in teststring2 if i in string.ascii_uppercase]
print(capital_letters_belen)
'''

'''
capital_letters_belen2 = [i for i in teststring2 if i.isupper()]
print(capital_letters_belen2)
'''

#9. Find all the consonants in the sentence 'The quick brown fox jumped over the lazy dog'.
# Use consonants as the name of the list.
# Remember to use list comprehensions and to print your results.

teststring3 = 'The quick brown fox jumped over the lazy dog'
consonants = ''.join([i for i in teststring3 if i in 'bcdfghjklmnpqrstvwxyzT'])
print(consonants)

# Soluciones en clase

'''
vowels = ['a','e','i','o','u']
consonants_belen = [i for i in teststring3 if i not in vowels]
print(consonants_belen)
'''

'''
consonants_belen2 = []
for i in teststring3:
    if i.lower() not in vowels:
        consonants_belen2.append(i)
print(consonants_belen2)
'''

#10. Find the folders you have in your madrid-oct-2018 local repo. Use files as name of the list.  
# You will probably need to import os library and some of its modules. You will need to make some online research.
# Remember to use list comprehensions and to print your results.

files = []
for i in os.listdir('/Users/mariafont1/Documents/IronHack/madrid-oct-2018'):
    files.append(i)
print(type(files))
print(files)

# Soluciones en clase

'''
El corchete del final funciona como un indice:
- el 1 agarra folders 
- el 2 agarra ficheros
- el 0 es medio useless 
- el next es importante aqui si no no funciona el os.walk ya que lo convierte en iterador
El my path, si esta en el mismo folder que en el que estoy trabajando, se puede poner asi:
'../madrid-oct-2018'


mypath = '/Users/mariafont1/Documents/IronHack/madrid-oct-2018'
files_belen = [i for i in next(os.walk(mypath))[1]]
print(files_belen)
'''

#11. Create 4 lists of 10 random numbers between 0 and 100 each. Use random_lists as the name of the list. 
#You will probably need to import random module
# Remember to use list comprehensions and to print your results

x = random.sample(range(0,101),10)

random_list = []
for i in range(4):
    random_list.append(x)
    
print(random_list)

#12. Flatten the following list of lists. Use flatten_list as the name of the output.
# Remember to use list comprehensions and to print your results

list_of_lists = [[1,2,3], [4,5,6], [7,8,9]]
flatten_list = [y for x in list_of_lists for y in x]
print(flatten_list)

#13. Convert the numbers of the following nested list to floats. Use floats as the name of the list. 
# Remember to use list comprehensions and to print your results.

list_of_lists1 = [['40', '20', '10', '30'], ['20', '20', '20', '20', '20', '30', '20'], \
['30', '20', '30', '50', '10', '30', '20', '20', '20'], ['100', '100'], ['100', '100', '100', '100', '100'], \
['100', '100', '100', '100']]
floats = [float(y) for x in list_of_lists1 for y in x]
print(floats)

#14. Handle the exception thrown by the code below by using try and except blocks. 


for i in ['a','b','c']:
    print i**2


#15. Handle the exception thrown by the code below by using try and except blocks. 
#Then use a finally block to print 'All Done.'
# Check in provided resources the type of error you may use. 

x = 5
y = 0

z = x/y




#16. Handle the exception thrown by the code below by using try and except blocks. 
# Check in provided resources the type of error you may use. 

abc=[10,20,20]
print(abc[3])


#17. Handle at least two kind of different exceptions when dividing a couple of numbers provided by the user. 
# Hint: take a look on python input function. 
# Check in provided resources the type of error you may use. 




#18. Handle the exception thrown by the code below by using try and except blocks. 
# Check in provided resources the type of error you may use. 

f = open('testfile','r')
f.write('Test write this')




#19. Handle the exceptions that can be thrown by the code below using try and except blocks. 
#Hint: the file could not exist and the data could not be convertable to int

fp = open('myfile.txt')
    line = f.readline()
    i = int(s.strip())




#20. The following function can only run on a Linux system. 
# The assert in this function will throw an exception if you call it on an operating system other than Linux. 
# Handle this exception using try and except blocks. 
# You will probably need to import sys 

def linux_interaction():
    assert ('linux' in sys.platform), "Function can only run on Linux systems."
    print('Doing something.')


# Bonus Questions:

# You will need to make some research on dictionary comprehension to solve the following questions

#21.  Write a function that asks for an integer and prints the square of it. 
# Hint: we need to continually keep checking until we get an integer.
# Use a while loop with a try,except, else block to account for incorrect inputs.




# 22. Find all of the numbers from 1-1000 that are divisible by any single digit besides 1 (2-9). 
# Use results as the name of the list 

#Solucion en Clase
'''
results = [number for number in range(1,1001) if True in [True for divisor in range (2,10) if number % divisor == 0]]
print(results)
'''

# 23. Define a customised exception to handle not accepted values. 
# You have the following user inputs and the Num_of_sections can not be less than 2.
# Hint: Create a class derived from the pre-defined Exception class in Python

Total_Marks = int(input("Enter Total Marks Scored: ")) 
Num_of_Sections = int(input("Enter Num of Sections: "))


