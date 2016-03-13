#!/usr/bin/python

import sys
import random
import math
import Student as student

def main(argv):
    from random import random
    from random import randint
    from math import sqrt

    test1 = [100]
    test2 = [10000]
    test3 = [1000000]
    test4 = [5000000]

    isCorrect = True

    test1_correct = correct_monte_carlo_pi(test1[0])
    test1_student = student.monte_carlo_pi(test1[0])
    print "\nOur Output: " + str(test1_correct)
    print "Your Output: "    + str(test1_student)
    if compare(test1_correct, test1_student, 1):
        print "Correct!"
    else:
        print "Incorrect"
        isCorrect = False

    test2_correct = correct_monte_carlo_pi(test2[0])
    test2_student = student.monte_carlo_pi(test2[0])
    print "\nOur Output: " + str(test2_correct)
    print "Your Output: "    + str(test2_student)
    if compare(test2_correct, test2_student, 0.3):
        print "Correct!"
    else:
        print "Incorrect"
        isCorrect = False

    test3_correct = correct_monte_carlo_pi(test3[0])
    test3_student = student.monte_carlo_pi(test3[0])
    print "\nOur Output: " + str(test3_correct)
    print "Your Output: "    + str(test3_student)
    if compare(test3_correct, test3_student, 0.05):
        print "Correct!"
    else:
        print "Incorrect"
        isCorrect = False

    test4_correct = correct_monte_carlo_pi(test4[0])
    test4_student = student.monte_carlo_pi(test4[0])
    print "\nOur Output: " + str(test4_correct)
    print "Your Output: "    + str(test4_student)
    if compare(test4_correct, test4_student, 0.005):
        print "Correct!"
    else:
        print "Incorrect"
        isCorrect = False


def compare(arr1, arr2, epsilon):

    upper_bound = arr1 + epsilon
    lower_bound = arr1 - epsilon
    return arr2 < upper_bound and arr2 > lower_bound

import random
import math
def correct_monte_carlo_pi(n):
    count_inside = 0
    for count in range(0, n):
        x = random.random()
        y = random.random()
        d = math.sqrt(x**2 + y**2)
        if d < 1: count_inside += 1
    count += 1
    return 4.0 * count_inside / count

if __name__ == "__main__":
    main(sys.argv[1:])
