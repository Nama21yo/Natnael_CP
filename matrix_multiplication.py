def mulMat(m1, m2):
    r1 = len(m1)
    c1 = len(m1[0])
    r2 = len(m2)
    c2 = len(m2[0])

    if c1 != r2:
        print("Invalid Input")
        return None

    # Initialize the result matrix with zeros
    res = [[0] * c2 for _ in range(r1)]

    # Perform matrix multiplication
    for i in range(r1):
        for j in range(c2):
            for k in range(c1):
                res[i][j] += m1[i][k] * m2[k][j]

    return res

# Driver code
if __name__ == "__main__":
    m1 = [
        [1, 1],
        [2, 2]
    ]

    m2 = [
        [1, 1],
        [2, 2]
    ]

    result = mulMat(m1, m2)

    print("Multiplication of given two matrices is:")
    for row in result:
        print(" ".join(map(str, row)))
