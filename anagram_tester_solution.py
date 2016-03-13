#!/usr/bin/python

import sys
import Student as student

def main(argv):
    test1 = ["Test", "Not anagram"]
    test2 = ["CAT", "TAC"]
    test3 = ["ANAGRAM", "MARANAG"]

    isCorrect = True
    #student = problemSet.Correct()

    test1_correct = str(correct_is_anagram(test1[0], test1[1]))
    test1_student = str(student.is_anagram(test1[0], test1[1]))
    print "Correct Output: " + test1_correct
    print "Your Output: "    + test1_student 
    if compare(test1_correct, test1_student):
        print "Correct!"
    else:
        print "Incorrect"
        isCorrect = False

    test2_correct = str(correct_is_anagram(test2[0], test2[1]))
    test2_student = str(student.is_anagram(test2[0], test2[1]))
    print "Correct Output: " + test2_correct
    print "Your Output: "    + test2_student 
    if compare(test2_correct, test2_student):
        print "Correct!"
    else:
        print "Incorrect"
        isCorrect = False

    test3_correct = str(correct_is_anagram(test3[0], test3[1]))
    test3_student = str(student.is_anagram(test3[0], test3[1]))
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

def correct_is_anagram(str1, str2):
    sorted_str1 = sorted(str1)
    sorted_str2 = sorted(str2)
    for i in range(len(sorted_str1)):
        if sorted_str1[i] != sorted_str2[i]:
            return False
    return True


if __name__ == "__main__":
    main(sys.argv[1:])
