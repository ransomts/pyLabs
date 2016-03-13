#!/usr/bin/python

import sys
import Student as student

def newtoncooling(time, temp):
	return -0.07 * (temp - 20)

def main(argv):
    test1 = [newtoncooling, 100,0,100,10]

    isCorrect = True
#    student = problemSet.Correct()

    test1_correct = str(correct_euler(test1[0], test1[1], test1[2], test1[3], test1[4]))
    test1_student = str(student.euler(test1[0], test1[1], test1[2], test1[3], test1[4]))
    print "Correct Output: " + test1_correct
    print "Your Output: "    + test1_student 
    if compare(test1_correct, test1_student):
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

def correct_euler(f, y0, a, b, h):
    t, y = a, y0
    values = [(a, y0)]
    results = []
    while t <= b:
        t += h
        y += h * f(t,y)
        values.append((t,y))
    for entry in values:
        results.append(entry)
    return results


if __name__ == "__main__":
    main(sys.argv[1:])
