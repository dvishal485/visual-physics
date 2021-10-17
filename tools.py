def vectorMagnitude(vector: list):
    sumOfSquares = 0
    for x in vector:
        sumOfSquares += float(x)**2
    return sumOfSquares**(1/2)
