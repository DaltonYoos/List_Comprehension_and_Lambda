
list1 = [10, 20, 30, 40, 50]

list2 =[]

for x in list1:
    if x > 20:
        
        x += 100
        list2.append(x)

print(list2)

list2 = [x+100 for x in list1 if x > 20]

print(list2)

#a list of numbers from 0 through 9
x = [i for i in range(10)]
print(x)


#find the square of each number from 0 to 9
x = [i**2 for i in range(10)]
print(x)

#multiply each element in a list by 3

list1 = [3,4,5]
multiplied = [item*3 for item in list1]
print(multiplied)

#Does not matter what you name the iterator, as long as you maintain consistency in you expression

#grab the first letter of each word

listofwords = ['this', 'is', 'a', 'list', 'of', 'words']

items = [i[0] for i in listofwords]
print(items)

#making letters lower and upper case

result = [x.lower() for x in ['A','B','C']]
print(result)

result2 = [x.upper() for x in result]
print(result2)

#add an if condition

#find the square of all even numbers from 0 to 4
new_range = [i*i for i in range(5) if i  % 2 ==0]
print(new_range)

#extract the numbers from the phrase below
string = 'Hello 12345 World!'
numbers = [x for x in string if x.isdigit()]
print(numbers)

#extract letter from a list

string = 'Hello 12345 World!'
letters = [x for x in string if x.isalpha()]
print(letters)

#find line 3 in the file test.txt
infile = open('test.txt', 'r')
result = [i.strip('\n') for i in infile if 'line3' in i]
print(result)
#i.strip removes the formatting of '\n'

#using a function
def double(x):
    return x*2

print(double(10))

mylist = [double(x) for x in range(10) if x%2 == 0]
print(mylist)

#having 2 arguments in the same list
result = [x+y for x in [10,20,30] for y in [20,40,60]]
print(result)