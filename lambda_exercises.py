''' 1)
Write a Python program to filter a list of integers using Lambda. Go to the editor
Original list of integers:
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Even numbers from the said list:
[2, 4, 6, 8, 10]
Odd numbers from the said list:
[1, 3, 5, 7, 9]
'''
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_numbers = list(filter(lambda num: num %2 == 0, list1))
print(even_numbers)

odd_numbers = list(filter(lambda num: num %2 == 1, list1))
print(odd_numbers)

print('\n')

''' 2)
find which days of the week have exactly 6 characters.
'''

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 
'Sunday']

days_list = list(filter(lambda num: len(num) == 6, weekdays))
print(days_list)

print('\n')

''' 3)
remove specific words from a given list 
Original list:
['orange', 'red', 'green', 'blue', 'white', 'black']
Remove words:
['orange', 'black']
After removing the specified words from the said list:
['red', 'green', 'blue', 'white']
'''
Original_List = ['orange', 'red', 'green', 'blue', 'white', 'black']

New_List = list(filter(lambda x:x!= 'orange' and x!='black', Original_List))
print(New_List)

print('\n')

''' 4)
 remove all elements from a given list present in another list
Original lists:
list1: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2: [2, 4, 6, 8]
Remove all elements from 'list1' present in 'list2:
[1, 3, 5, 7, 9, 10]
 '''

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 = [2, 4, 6, 8]

list_numbers = list(filter(lambda x: x not in list2,list1))
print(list_numbers)


print('\n')

''' 5)
find the elements of a given list of strings that contain specific substring using 
lambda
Original list:
['red', 'black', 'white', 'green', 'orange']
Substring to search:
ack
Elements of the said list that contain specific substring:
['black']
Substring to search:
abc
Elements of the said list that contain specific substring:
[]
'''

list_colors = ['red','black','white','green','orange']

search1 = 'ack'
search2 = 'abc'

search_result1 = list(filter(lambda list_colors: search1 in list_colors,list_colors))
search_result2 = list(filter(lambda list_colors: search2 in list_colors, list_colors))

print(search_result1)
print(search_result2)

print('\n')

''' 6)
check whether a given string contains a capital letter, a lower case letter, a 
number and a minimum length of 8 characters.
(This is like a password verification function, HINT: Python function 'any' may be 
useful)
'''

pass1 = 'GoPackGoGB'
pass2 = 'gopackgogb'
pass3 = 'G0PackGoGB'

password_list = [pass1, pass2, pass3]

func = [lambda password_list: any(x.isupper() for x in password_list),lambda password_list: any(x.islower() for x in password_list),lambda password_list: any(x.isdigit() for x in password_list), lambda password_list: len(password_list) >= 8 ]

if all(func(password_list[0]) for func in func):

    print('Password is valid.')

else:

    print('Sorry, password is invalid.')


if all(func(password_list[1]) for func in func):

    print('Password is valid.')

else:

    print('Sorry, password is invalid.')


if all(func(password_list[2]) for func in func):

    print('Password is valid.')

else:

    print('Sorry, password is invalid.')


print('\n')

''' 7)
Write a Python program to sort a list of tuples using Lambda.
# Original list of tuples:
original_scores = [('English', 88), ('Science', 90), ('Maths', 97), ('Social 
sciences', 82)]
# Expected Result:
# [('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]
'''

scores = [('English',88),('Science',90),('Math',97),('Social Sciences',82)]

scores.sort(key=lambda course:course[1])

print(scores)

print('\n')

#I added spacers between each question to make each easier to read individually