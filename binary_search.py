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

        <br/><!-- panel --><br\>.:|:.
