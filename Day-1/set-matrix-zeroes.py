class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        pos = []
        m = len(matrix)
        n = len(matrix[0])
        # print(n,m)
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    pos.append((i, j))
        for i, j in pos:
            for k in range(n):
                print(i, k)
                matrix[i][k] = 0
            for l in range(m):
                print(l, j)

                matrix[l][j] = 0
        print(matrix)
