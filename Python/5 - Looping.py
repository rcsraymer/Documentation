# https://anandology.com/python-practice-book/iterators.html

word = 'Charlotte'


# Loop through string
for letter in word:
    print(letter)
     


# Loop through string with enumerate()
for index, letter in enumerate(word):
    print('Letter {} is in position {}'.format(letter, index))




# Append to List Loop
SomeList = []
for x in range(1,10):    # does not include upper bound (like slicing)
    SomeList.append(x)
  

      
# Loop with Conditional logic
EvensOnly = []
for x in SomeList:
    if x % 2 == 0:
        EvensOnly.append(x)



        
# Loop through list
MyList = [0,1,2]
SecondList = ['Justin',0,MyList]
for x in SecondList:
    if isinstance(x,list):
        print('Element {} is a list which has {} elements'.format(SecondList.index(x),len(x)))
    else:
        print('Element {} is not a list'.format(SecondList.index(x)))

        
        
        
        
# Loop with Logic - One-liner

EvensOnly = [x for x in SomeList if x % 2 == 0]
"""          ^     ^       ^            ^       """
#      ReturnThis  Elem  Iterable    Logic





# checking for values
if 'lo' in word:
    print('Yes')
    
if 2 in MyList:
    print('Yes')
else:
    print('No')
