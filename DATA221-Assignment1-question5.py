def circleAreaCoverage(radiusOfCircle1, radiusOfCircle2):
    if radiusOfCircle1 <= 0 or radiusOfCircle2 <= 0:
        return "Invalid input: radii must be positive"

    pi = 3.14159
    areaOfCircle1 = pi * radiusOfCircle1 * radiusOfCircle1
    areaOfCircle2 = pi * radiusOfCircle2 * radiusOfCircle2

    if areaOfCircle1 > areaOfCircle2:
        largerCircle = areaOfCircle1
        smallerCircle = areaOfCircle2
    else:
        largerCircle = areaOfCircle2
        smallerCircle = areaOfCircle1

    return (smallerCircle / largerCircle) * 100
