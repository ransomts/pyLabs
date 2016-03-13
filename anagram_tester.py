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

        <br/><!-- panel --><br\>.:|:.
