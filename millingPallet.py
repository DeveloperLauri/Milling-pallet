# 19.5.23 Lauri Inkilä
# This algorithm simulates a tool changer in a milling machine.
# It prints the minimum number of moves to the target tool.
# The physical tool changer device would be circular - the code is developed accordingly.
# Time complexity O(n).

def millingToolChanger(tools, startIndex, target):
    length = len(tools)
    
    # Step counter variables.
    clockwise = 0
    counterClockwise = 0
    stepCounter = startIndex

    # Moving clockwise
    while True:
        if target == tools[stepCounter]:
            break
        
        # Circular list
        # Divident = divisor * quotient (integer division) + remainder
        stepCounter += 1 % length
        clockwise += 1

    stepCounter = startIndex

    # Moving counter clockwise
    while True:
        if target == tools[stepCounter]:
            break

        # Circular list
        # Divident = divisor * quotient (integer division) + remainder
        stepCounter -= 1 % length
        counterClockwise += 1

    return min(clockwise, counterClockwise)

if __name__ == "__main__":

    tools = ['ballendmill', 'keywaycutter', 'facemill', 'slotdrill']
    startIndex = 1
    target = 'facemill'

    result = millingToolChanger(tools, startIndex, target)
    print(result)
