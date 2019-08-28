class Solution:
    """
    @param A: a sparse matrix
    @param B: a sparse matrix
    @return: the result of A * B
    """

    def multiply(self, A, B):
        # write your code here
        # A l*m
        # B m*n
        l = len(A)
        m = len(A[0])
        n = len(B[0])
        C = [[0] * n for _ in range(l)]
        for i in range(l):
            for k in range(m):
                if A[i][k] == 0:
                    continue
                for j in range(n):
                    # print("%d, %d, %d" % (C[i][j], A[i][k], B[k][j]))
                    C[i][j] += A[i][k] * B[k][j]

        return C


class Solution2:
    """
    @param A: a sparse matrix
    @param B: a sparse matrix
    @return: the result of A * B
    """

    def multiply(self, A, B):
        row_vectors = self.convert_to_row_vectors(A)
        col_vectors = self.convert_to_col_vectors(B)

        matrix = []
        for row_vector in row_vectors:
            row = []
            for col_vector in col_vectors:
                row.append(self.multi_vector(row_vector, col_vector))
            matrix.append(row)
        return matrix

    def convert_to_row_vectors(self, matrix):
        vectors = []
        for row in matrix:
            vector = []
            for index, col in enumerate(row):
                if col != 0:
                    vector.append((index, col))
            vectors.append(vector)
        return vectors

    def convert_to_col_vectors(self, matrix):
        n, m = len(matrix), len(matrix[0])
        vectors = []
        for j in range(m):
            vector = []
            for i in range(n):
                if matrix[i][j] != 0:
                    vector.append((i, matrix[i][j]))
            vectors.append(vector)
        return vectors

    def multi_vector(self, v1, v2):
        i, j = 0, 0
        result = 0

        while i < len(v1) and j < len(v2):
            if v1[i][0] < v2[j][0]:
                i += 1
            elif v1[i][0] > v2[j][0]:
                j += 1
            else:
                result += v1[i][1] * v2[j][1]
                i += 1
                j += 1

        return result

sol = Solution()
sol.multiply([[1,0,0],[-1,0,3]], [[7,0,0],[0,0,0],[0,0,1]])