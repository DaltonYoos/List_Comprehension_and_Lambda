#lambda allows you to create multiple function-objects.

def testfunc(num):
    return lambda x: x * num

result10 = testfunc(10)
result100 = testfunc(100)   #This method is the same as the method below. It will yield the same result.

result10 = lambda x: x * 10
resulty100 = lambda x: x * 100  #This method is the same as the method above. It will yield the same result. 

# ^ Returns a function object, they do not return a value. 

print(result10(9))
print(result100(9))

numbers_list = [2,6,8,10,12,7,13,17,0,3,21]

#filter() needs two components, a function and an iterable.

filtered_list = list(filter(lambda num: (num >7), numbers_list))

print(filtered_list)

#map() needs two components, a function and an iterable

mapped_list = list(map(lambda num: num %2, numbers_list))

print(mapped_list)