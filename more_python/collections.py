# Collection: Is unordered or ordered group of elements. 

x = [4, True, 'hi'] # list of elements, a list is denoted by []. Lists are mutable

x.append('wang') # append function addes more elements to the end of the list. 
x.extend([5,97,96,1498,'March']) #extend appends all these elements to the mentioned list.
print(x.pop()) # pop removes the last element and returns the last element of the list.

y = [4, 9, 5, 'Jeff']
print(len(x), len(y)) # len function determines the length of the list
print(x)

print(x[3]) # using the index of an element returns the element stores at that particular index.

x[3] = 'Derick' # You can change the value of an element by directly assigning it another value. This assigns index 3 a new value of Derick.