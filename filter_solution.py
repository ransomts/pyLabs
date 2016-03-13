#!/usr/bin/python

import sys
import Student as student

def main(argv):
    test1 = [[0,2,1,3,4,5], (lambda x: x % 2 == 0)]
    test2 = [[0,2,1,3,4,5], (lambda x: x % 2 == 1)]

    isCorrect = True
#    student = problemSet.Correct()

    test1_correct = str(correct_filter_array(test1[0], test1[1]))
    test1_student = str(student.filter_array(test1[0], test1[1]))
    print "Correct Output: " + test1_correct
    print "Your Output: "    + test1_student 
    if compare(test1_correct, test1_student):
        print "Correct!"
    else:
        print "Incorrect"
        isCorrect = False

    test2_correct = str(correct_filter_array(test2[0], test2[1]))
    test2_student = str(student.filter_array(test2[0], test2[1]))
    print "Correct Output: " + test2_correct
    print "Your Output: "    + test2_student 
    if compare(test2_correct, test2_student):
        print "Correct!"
    else:
        print "Incorrect"
        isCorrect = False


def compare(arr1, arr2):
    i = 0
    if len(arr1) != len(arr2):
        return False

    for i in range(0, len(arr1)):
        if arr1[i] != arr2[i]:
            return False

    return True

def correct_filter_array (array, filter_function):
    return_array  = []
    for element in array:
        if (filter_function(element)):
            return_array.append(element)
    return return_array

if __name__ == "__main__":
    main(sys.argv[1:])
