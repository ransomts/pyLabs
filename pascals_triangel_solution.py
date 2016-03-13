#!/usr/bin/python

import sys
import Student as student

def main(argv):
    test1 = [1]
    test2 = [3]
    test3 = [5]

    isCorrect = True
#    student = problemSet.Correct()

    test1_correct = str(correct_pascal(test1[0]))
    test1_student = str(student.pascal(test1[0]))
    print "Correct Output: " + test1_correct
    print "Your Output: "    + test1_student 
    if compare(test1_correct, test1_student):
        print "Correct!"
    else:
        print "Incorrect"
        isCorrect = False

    test2_correct = str(correct_pascal(test2[0]))
    test2_student = str(student.pascal(test2[0]))
    print "Correct Output: " + test2_correct
    print "Your Output: "    + test2_student 
    if compare(test2_correct, test2_student):
        print "Correct!"
    else:
        print "Incorrect"
        isCorrect = False

    test3_correct = str(correct_pascal(test3[0]))
    test3_student = str(student.pascal(test3[0]))
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

def correct_pascal(n):
   """Prints out n rows of Pascal's triangle.
   It returns False for failure and True for success."""
   row = [1]
   k = [0]
   for x in range(max(n,0)):
      row=[l+r for l,r in zip(row+k,k+row)]
   return row


if __name__ == "__main__":
    main(sys.argv[1:])
