import sys
import copy


def smallestElementDifference(X, Y, m, n):

    #sorting both arrays and storing it in respective variable
    #X.sort()
    #Y.sort()
    A = sorted(X)
    B = sorted(Y)
    #counter to iterate over
    a = 0
    b = 0

    #Initialize timeunits which is result as max value
    result = sys.maxsize

    #scaning both arrays upto size of the arrays
    while (a < m and b < n):
        if (abs(A[a] - B[b]) < result):
            result = abs(A[a] - B[b])
            #storing the pair(liftfloor,personfloor) having minimum timeunits difference
            temp = A[a]  #liftfloor
            temp1 = B[b]  #personfloor

        #move Smaller Value
        if (A[a] < B[b]):
            a += 1
        else:
            b += 1

    #returning the result and nearest Liftfloor, PersonFloor
    return result, temp, temp1


#Iterate until every person(Max 3) get the lift
def getPositionOfLift(A, B):

    timeunits = 0
    for p in range(len(B)):
        # Calculate size of Both arrays
        m = len(A)
        n = len(B)

        #storing the timeunits, nearest lift and person floor number
        value, liftNo, person = smallestElementDifference(A, B, m, n)

        #print("TimeUnits: ", value)
        print("Lift is picking up the person standing at floor: ", person)
        print("Currently nearest lift is at floor: ", liftNo)
        print("Starting Position of all lifts: ", A)
        timeunits = timeunits + value
        x = A.index(liftNo)
        A[x] = person
        print("Updated Position of all lifts: ", A)
        print(
            f"Time Taken to pick the person standing on floor {person} : {value} timeunits"
        )
        print("=======" * 6)
        #print(len(B))
        B.remove(person)
    return A, timeunits


# Input array for initial position of Lift Floors
LiftStandingPos = [1, 3, 4]
# Input array for position of Waiting Persons Floors
PersonStandingPos = [5, 2]

currentPos, totalTimeUnits = getPositionOfLift(LiftStandingPos,
                                               PersonStandingPos)
print("The Current Positions of Lift is: ", currentPos)
print("Total time taken: ", totalTimeUnits, "timeunits")
