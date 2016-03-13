#!/usr/bin/python

import sys
import Student as student
'''
initial data is in ascending order
initial data is in descending order
initial data is all the same value
initial data has only two values
initial data has only one value
'''
def main(argv):
    test1 = [[0,1,10,110,111]]
    test2 = [[111,110,10,1,1]]
    test3 = [[0,0,0,0,0,0,0]]
    test4 = [[10, 20]]
    test5 = [[20, 10]]
    test6 = [[10]]

    isCorrect = True

    test1_correct = str(correct_radix_sort(test1[0]))
    test1_student = str(student.radix_sort(test1[0]))
    print "Correct Output: " + test1_correct
    print "Your Output: "    + test1_student 
    if compare(test1_correct, test1_student):
        print "Correct!"
    else:
        print "Incorrect"
        isCorrect = False

    test2_correct = str(correct_radix_sort(test2[0]))
    test2_student = str(student.radix_sort(test2[0]))
    print "Correct Output: " + test2_correct
    print "Your Output: "    + test2_student 
    if compare(test2_correct, test2_student):
        print "Correct!"
    else:
        print "Incorrect"
        isCorrect = False

    test3_correct = str(correct_radix_sort(test3[0]))
    test3_student = str(student.radix_sort(test3[0]))
    print "Correct Output: " + test3_correct
    print "Your Output: "    + test3_student 
    if compare(test3_correct, test3_student):
        print "Correct!"
    else:
        print "Incorrect"
        isCorrect = False

    test4_correct = str(correct_radix_sort(test4[0]))
    test4_student = str(student.radix_sort(test4[0]))
    print "Correct Output: " + test4_correct
    print "Your Output: "    + test4_student 
    if compare(test4_correct, test4_student):
        print "Correct!"
    else:
        print "Incorrect"
        isCorrect = False

    test5_correct = str(correct_radix_sort(test5[0]))
    test5_student = str(student.radix_sort(test5[0]))
    print "Correct Output: " + test5_correct
    print "Your Output: "    + test5_student 
    if compare(test5_correct, test5_student):
        print "Correct!"
    else:
        print "Incorrect"
        isCorrect = False

    test6_correct = str(correct_radix_sort(test6[0]))
    test6_student = str(student.radix_sort(test6[0]))
    print "Correct Output: " + test6_correct
    print "Your Output: "    + test6_student 
    if compare(test6_correct, test6_student):
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

def correct_radix_sort(a,n,maxLen):
    for x in range(maxLen):
        bins = [[] for i in range(n)]
        for y in a:
            bins[(y/10**x)%n].append(y)
        a=[]
        for section in bins:
            a.extend(section)
    return a

if __name__ == "__main__":
    main(sys.argv[1:])
