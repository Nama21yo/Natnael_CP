class Matrix:
    def __init__(self, rows, cols, data=None):
        self.rows = rows
        self.cols = cols
        if data:
            if len(data) != rows or any(len(row) != cols for row in data):
                raise ValueError("Invalid matrix dimensions")
            self.data = data
        else:
            self.data = [[0] * cols for _ in range(rows)]
    
    def __repr__(self):
        return "\n".join([" ".join(map(str, row)) for row in self.data])
    
    def add(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrix dimensions must match")
        result = [[self.data[i][j] + other.data[i][j] for j in range(self.cols)] for i in range(self.rows)]
        return Matrix(self.rows, self.cols, result)
    
    def subtract(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrix dimensions must match")
        result = [[self.data[i][j] - other.data[i][j] for j in range(self.cols)] for i in range(self.rows)]
        return Matrix(self.rows, self.cols, result)
    
    def multiply(self, other):
        if self.cols != other.rows:
            raise ValueError("Invalid matrix dimensions for multiplication")
        result = [[sum(self.data[i][k] * other.data[k][j] for k in range(self.cols)) for j in range(other.cols)] for i in range(self.rows)]
        return Matrix(self.rows, other.cols, result)
    
    def transpose(self):
        result = [[self.data[j][i] for j in range(self.rows)] for i in range(self.cols)]
        return Matrix(self.cols, self.rows, result)
    
    def scalar_multiply(self, scalar):
        result = [[self.data[i][j] * scalar for j in range(self.cols)] for i in range(self.rows)]
        return Matrix(self.rows, self.cols, result)
    
# Example usage:
A = Matrix(2, 2, [[1, 2], [3, 4]])
B = Matrix(2, 2, [[5, 6], [7, 8]])
C = A.add(B)
D = A.multiply(B)
E = A.transpose()
print("Matrix A:")
print(A)
print("\nMatrix B:")
print(B)
print("\nA + B:")
print(C)
print("\nA * B:")
print(D)
print("\nTranspose of A:")
print(E)
