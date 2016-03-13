'''
Execute the Euler method of approximation to first-order ordinary differenetiol equitations.
'''


def euler(f, y0, a, b, h):
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

def newtoncooling(time, temp):
	return -0.07 * (temp - 20)
 
euler(newtoncooling,100,0,100,10)

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
