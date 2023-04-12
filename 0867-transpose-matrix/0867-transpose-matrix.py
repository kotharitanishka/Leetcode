class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        # for i in range (0,len(matrix[0])):
        #     for j in range (i,len(matrix)):
        #         temp = matrix[i][j]
        #         matrix[i][j] = matrix[j][i]
        #         matrix[j][i] = temp
        # return(matrix)
        matrix2 = [[0 for j in range(len(matrix))] for i in range(len(matrix[0]))]
        for i in range (0,len(matrix2)):
            for j in range (0,len(matrix2[0])):
                matrix2[i][j] = (matrix[j][i])
        return(matrix2)
        
        