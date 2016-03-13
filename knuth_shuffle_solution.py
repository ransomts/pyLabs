#!/usr/bin/python

import sys
import Student as student

def main(argv):
    test1 = [[0,1,2,3]]
    test2 = [[-10,-3,0,45]]
    test3 = [[-12, 10, 23, 30]]

    isCorrect = True

    test1_correct = str(correct_knuth_shuffle(test1[0]))
    test1_student = str(student.knuth_shuffle(test1[0]))
    print "Correct Output: " + test1_correct
    print "Your Output: "    + test1_student 
    if compare(test1_correct, test1_student):
        print "Correct!"
    else:
        print "Incorrect"
        isCorrect = False

    test2_correct = str(correct_knuth_shuffle(test2[0]))
    test2_student = str(student.knuth_shuffle(test2[0]))
    print "Correct Output: " + test2_correct
    print "Your Output: "    + test2_student 
    if compare(test2_correct, test2_student):
        print "Correct!"
    else:
        print "Incorrect"
        isCorrect = False

    test3_correct = str(correct_knuth_shuffle(test3[0]))
    test3_student = str(student.knuth_shuffle(test3[0]))
    print "Correct Output: " + test3_correct
    print "Your Output: "    + test3_student 
    if compare(test3_correct, test3_student):
        print "Correct!"
    else:
        print "Incorrect"
        isCorrect = False

    print "Keep in mind that a random shuffele such as this means that each iteration is different from the others.\n" 

def compare(arr1, arr2):
    return True
    i = 0;
    if len(arr1) != len(arr2):
        return False

    for i in range(0, len(arr1)):
        if arr1[i] != arr2[i]:
            return False
    return True

from random import randrange
 
def correct_knuth_shuffle(x):
    for i in range(len(x)-1, 0, -1):
        j = randrange(i + 1)
        x[i], x[j] = x[j], x[i]
    return x

if __name__ == "__main__":
    main(sys.argv[1:])
