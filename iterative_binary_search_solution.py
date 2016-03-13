#!/usr/bin/python

import sys
import Student as student

def main(argv):
    test1 = [[0,1,2,3], 0]
    test2 = [[-10,-3,0,45], -3]
    test3 = [[-12, 10, 23, 30], 30]

    isCorrect = True
#    student = problemSet.Correct()

    test1_correct = str(correct_binary_search(test1[0], test1[1]))
    test1_student = str(student.binary_search(test1[0], test1[1]))
    print "Correct Output: " + test1_correct
    print "Your Output: "    + test1_student 
    if compare(test1_correct, test1_student):
        print "Correct!"
    else:
        print "Incorrect"
        isCorrect = False

    test2_correct = str(correct_binary_search(test2[0], test2[1]))
    test2_student = str(student.binary_search(test2[0], test2[1]))
    print "Correct Output: " + test2_correct
    print "Your Output: "    + test2_student 
    if compare(test2_correct, test2_student):
        print "Correct!"
    else:
        print "Incorrect"
        isCorrect = False

    test3_correct = str(correct_binary_search(test3[0], test3[1]))
    test3_student = str(student.binary_search(test3[0], test3[1]))
    print "Correct Output: " + test3_correct
    print "Your Output: "    + test3_student 
    if compare(test3_correct, test3_student):
        print "Correct!"
    else:
        print "Incorrect"
        isCorrect = False


def compare(arr1, arr2):
    i = 0;
    if len(arr1) != len(arr2):
        return False

    for i in range(0, len(arr1)):
        if arr1[i] != arr2[i]:
            return False
    return True

def correct_binary_search(l, value):
    low = 0
    high = len(l)-1
    while low <= high: 
        mid = (low+high)//2
        if l[mid] > value: high = mid-1
        elif l[mid] < value: low = mid+1
        else: return mid
    return -1

if __name__ == "__main__":
    main(sys.argv[1:])
