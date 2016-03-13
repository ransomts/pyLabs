#!/usr/bin/python

import sys
import Student as student

def main(argv):
    test1 = [1]
    test2 = [10]
    test3 = [101]

    isCorrect = True

    test1_correct = str(correct_doors(test1[0]))
    test1_student = str(student.doors(test1[0]))
    print "Correct Output: " + test1_correct
    print "Your Output: "    + test1_student 
    if compare(test1_correct, test1_student):
        print "Correct!"
    else:
        print "Incorrect"
        isCorrect = False

    test2_correct = str(correct_doors(test2[0]))
    test2_student = str(student.doors(test2[0]))
    print "Correct Output: " + test2_correct
    print "Your Output: "    + test2_student 
    if compare(test2_correct, test2_student):
        print "Correct!"
    else:
        print "Incorrect"
        isCorrect = False

    test3_correct = str(correct_doors(test3[0]))
    test3_student = str(student.doors(test3[0]))
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

def correct_doors(n):
    for i in range(1, n):
        if i**0.5 % 1:
            state='open'
        else:
            state='close'
        return ("Door {}:{}".format(i, state))

if __name__ == "__main__":
    main(sys.argv[1:])
