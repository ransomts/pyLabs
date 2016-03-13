

def monte_carlo_pi(n):
    from random import random, randint
    from math import sqrt
    count_inside = 0
    for count in range(0, n):
        x = random()
        y = random()
        d = sqrt(x*x + y*y)
        if d < 1: count_inside += 1
    return 4.0 * count_inside / n



'''
Problem: You have 100 doors in a row that are all initially closed. You make 100 passes by the doors. The first time through, you visit every door and toggle the door (if the door is closed, you open it; if it is open, you close it). The second time you only visit every 2nd door (door #2, #4, #6, ...). The third time, every 3rd door (door #3, #6, #9, ...), etc, until you only visit the 100th door.

Question: What state are the doors in after the last pass? Which are open, which are closed?
'''
def doors(n):
    for i in range(1, n):
        if i**0.5 % 1:
            state='open'
        else:
            state='close'
        return ("Door {}:{}".format(i, state))

'''
Decide if two strings passed to the function are anagrams.
'''

def is_anagram(str1, str2):
    sorted_str1 = sorted(str1)
    sorted_str2 = sorted(str2)
    for i in range(len(sorted_str1)):
        if sorted_str1[i] != sorted_str2[i]:
            return False
    return True


'''
Problem: You have 100 doors in a row that are all initially closed. You make 100 passes by the doors. The first time through, you visit every door and toggle the door (if the door is closed, you open it; if it is open, you close it). The second time you only visit every 2nd door (door #2, #4, #6, ...). The third time, every 3rd door (door #3, #6, #9, ...), etc, until you only visit the 100th door.

Question: What state are the doors in after the last pass? Which are open, which are closed?
'''
def doors():
    for i in range(1, 101):
        if i**0.5 % 1:
            state='open'
        else:
            state='close'
        print("Door {}:{}".format(i, state))

'''
Search for the index of an element in a list with an iterative binary search. Return -1 (a nonsense index value) if the element is not in the list.
'''

def binary_search(l, value):
    low = 0
    high = len(l)-1
    while low <= high: 
        mid = (low+high)//2
        if l[mid] > value: high = mid-1
        elif l[mid] < value: low = mid+1
        else: return mid
    return -1

'''
Problem: You have 100 doors in a row that are all initially closed. You make 100 passes by the doors. The first time through, you visit every door and toggle the door (if the door is closed, you open it; if it is open, you close it). The second time you only visit every 2nd door (door #2, #4, #6, ...). The third time, every 3rd door (door #3, #6, #9, ...), etc, until you only visit the 100th door.

Question: What state are the doors in after the last pass? Which are open, which are closed?
'''
def doors():
    for i in range(1, 101):
        if i**0.5 % 1:
            state='open'
        else:
            state='close'
        print("Door {}:{}".format(i, state))

         
'''
There are four types of common coins in US currency: quarters (25 cents), dimes (10), nickels (5) and pennies (1). There are 6 ways to make change for 15 cents:

A dime and a nickel;
A dime and 5 pennies;
3 nickels;
2 nickels and 5 pennies;
A nickel and 10 pennies;
15 pennies.
How many ways are there to make change for a dollar using these common coins? (1 dollar = 100 cents).
'''
def changes(amount, coins):
    ways = [0] * (amount + 1)
    ways[0] = 1
    for coin in coins:
        for j in xrange(coin, amount + 1):
            ways[j] += ways[j - coin]
    return ways[amount]

#print changes(100, [1, 5, 10, 25])
#print changes(200, [1, 5, 10, 25])

'''
Problem: You have 100 doors in a row that are all initially closed. You make 100 passes by the doors. The first time through, you visit every door and toggle the door (if the door is closed, you open it; if it is open, you close it). The second time you only visit every 2nd door (door #2, #4, #6, ...). The third time, every 3rd door (door #3, #6, #9, ...), etc, until you only visit the 100th door.

Question: What state are the doors in after the last pass? Which are open, which are closed?
'''
def doors():
    for i in range(1, 101):
        if i**0.5 % 1:
            state='open'
        else:
            state='close'
        print("Door {}:{}".format(i, state))

         

'''
Detect a divide by zero error without checking if the denominator is zero
'''

def div_check(x, y):
    try:
        x / y
    except ZeroDivisionError:
        return True
    else:
        return False

'''
Problem: You have 100 doors in a row that are all initially closed. You make 100 passes by the doors. The first time through, you visit every door and toggle the door (if the door is closed, you open it; if it is open, you close it). The second time you only visit every 2nd door (door #2, #4, #6, ...). The third time, every 3rd door (door #3, #6, #9, ...), etc, until you only visit the 100th door.

Question: What state are the doors in after the last pass? Which are open, which are closed?
'''
def doors():
    for i in range(1, 101):
        if i**0.5 % 1:
            state='open'
        else:
            state='close'
        print("Door {}:{}".format(i, state))

         
'''
Execute the Euler method of approximation to first-order ordinary differenetiol equitations.
'''


def euler(f, y0, a, b, h):
    t, y = a, y0
    values = [(a, y0)]
    results = []
    while t <= b:
        t += h
        y += h * f(t,y)
        values.append((t,y))
    for entry in values:
        results.append(entry)
    return results

def newtoncooling(time, temp):
	return -0.07 * (temp - 20)
 
euler(newtoncooling,100,0,100,10)

'''
Problem: You have 100 doors in a row that are all initially closed. You make 100 passes by the doors. The first time through, you visit every door and toggle the door (if the door is closed, you open it; if it is open, you close it). The second time you only visit every 2nd door (door #2, #4, #6, ...). The third time, every 3rd door (door #3, #6, #9, ...), etc, until you only visit the 100th door.

Question: What state are the doors in after the last pass? Which are open, which are closed?
'''
def doors():
    for i in range(1, 101):
        if i**0.5 % 1:
            state='open'
        else:
            state='close'
        print("Door {}:{}".format(i, state))

         
'''
Python, like in many languages, has need to filter through
a data structure and return elements that fit a criteria.
Fill in a function that takes an array and a conditional 
function and returns the elements that fit into the filter.
'''


def filter_array (array, filter_function):
    return_array  = []
    for element in array:
        if (filter_function(element)):
            return_array.append(element)
    return return_array

'''
Problem: You have 100 doors in a row that are all initially closed. You make 100 passes by the doors. The first time through, you visit every door and toggle the door (if the door is closed, you open it; if it is open, you close it). The second time you only visit every 2nd door (door #2, #4, #6, ...). The third time, every 3rd door (door #3, #6, #9, ...), etc, until you only visit the 100th door.

Question: What state are the doors in after the last pass? Which are open, which are closed?
'''
def doors():
    for i in range(1, 101):
        if i**0.5 % 1:
            state='open'
        else:
            state='close'
        print("Door {}:{}".format(i, state))

         
'''
Search for the index of an element in a list with an iterative binary search. Return -1 (a nonsense index value) if the element is not in the list.
'''

def binary_search(l, value):
    low = 0
    high = len(l)-1
    while low <= high: 
        mid = (low+high)//2
        if l[mid] > value: high = mid-1
        elif l[mid] < value: low = mid+1
        else: return mid
    return -1

'''
Problem: You have 100 doors in a row that are all initially closed. You make 100 passes by the doors. The first time through, you visit every door and toggle the door (if the door is closed, you open it; if it is open, you close it). The second time you only visit every 2nd door (door #2, #4, #6, ...). The third time, every 3rd door (door #3, #6, #9, ...), etc, until you only visit the 100th door.

Question: What state are the doors in after the last pass? Which are open, which are closed?
'''
def doors():
    for i in range(1, 101):
        if i**0.5 % 1:
            state='open'
        else:
            state='close'
        print("Door {}:{}".format(i, state))

         
''' 
Use Python swap notation to perform a Knuth shuffle and return a random permutation of a list.
'''

from random import randrange
 
def knuth_shuffle(x):
    for i in range(len(x)-1, 0, -1):
        j = randrange(i + 1)
        x[i], x[j] = x[j], x[i]
    return x
 

'''
Problem: You have 100 doors in a row that are all initially closed. You make 100 passes by the doors. The first time through, you visit every door and toggle the door (if the door is closed, you open it; if it is open, you close it). The second time you only visit every 2nd door (door #2, #4, #6, ...). The third time, every 3rd door (door #3, #6, #9, ...), etc, until you only visit the 100th door.

Question: What state are the doors in after the last pass? Which are open, which are closed?
'''
def doors():
    for i in range(1, 101):
        if i**0.5 % 1:
            state='open'
        else:
            state='close'
        print("Door {}:{}".format(i, state))

         
'''
Print out the nth row of Pascal's triangle
'''

def pascal(n):
   """Prints out n rows of Pascal's triangle.
   It returns False for failure and True for success."""
   row = [1]
   k = [0]
   for x in range(max(n,0)):
      row=[l+r for l,r in zip(row+k,k+row)]
   return row

'''
Problem: You have 100 doors in a row that are all initially closed. You make 100 passes by the doors. The first time through, you visit every door and toggle the door (if the door is closed, you open it; if it is open, you close it). The second time you only visit every 2nd door (door #2, #4, #6, ...). The third time, every 3rd door (door #3, #6, #9, ...), etc, until you only visit the 100th door.

Question: What state are the doors in after the last pass? Which are open, which are closed?
'''
def doors():
    for i in range(1, 101):
        if i**0.5 % 1:
            state='open'
        else:
            state='close'
        print("Door {}:{}".format(i, state))

         
''' Search for the index of an element in a list with a recursive binary search. Reurn -1 (a nonsense index value) if the element is not in the list.
'''

def binary_search(l, value, low = 0, high = -1):
    if not l: return -1
    if(high == -1): high = len(l)-1
    if low == high:
        if l[low] == value: return low
        else: return -1
    mid = (low+high)//2
    if l[mid] > value: return binary_search(l, value, low, mid-1)
    elif l[mid] < value: return binary_search(l, value, mid+1, high)
    else: return mid

'''
Problem: You have 100 doors in a row that are all initially closed. You make 100 passes by the doors. The first time through, you visit every door and toggle the door (if the door is closed, you open it; if it is open, you close it). The second time you only visit every 2nd door (door #2, #4, #6, ...). The third time, every 3rd door (door #3, #6, #9, ...), etc, until you only visit the 100th door.

Question: What state are the doors in after the last pass? Which are open, which are closed?
'''
def doors():
    for i in range(1, 101):
        if i**0.5 % 1:
            state='open'
        else:
            state='close'
        print("Door {}:{}".format(i, state))

         
'''
Determine if a string is a numeric.
'''

def is_numeric (s):
    try:
        i = float(s)
    except (ValueError, TypeError):
        return False
    return True

# Note: only works for positive integers
def alternate_solution (s):
    if s.isdigit():
        return True
    return False

'''
Problem: You have 100 doors in a row that are all initially closed. You make 100 passes by the doors. The first time through, you visit every door and toggle the door (if the door is closed, you open it; if it is open, you close it). The second time you only visit every 2nd door (door #2, #4, #6, ...). The third time, every 3rd door (door #3, #6, #9, ...), etc, until you only visit the 100th door.

Question: What state are the doors in after the last pass? Which are open, which are closed?
'''
def doors():
    for i in range(1, 101):
        if i**0.5 % 1:
            state='open'
        else:
            state='close'
        print("Door {}:{}".format(i, state))

         
