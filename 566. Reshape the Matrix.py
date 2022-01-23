Problem: '''566. Reshape the Matrix
In MATLAB, there is a handy function called reshape which can reshape an m x n matrix into a new one with a different size r x c keeping its original data.

You are given an m x n matrix mat and two integers r and c representing the number of rows and the number of columns of the wanted reshaped matrix.

The reshaped matrix should be filled with all the elements of the original matrix in the same row-traversing order as they were.

If the reshape operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix.

 

Example 1:


Input: mat = [[1,2],[3,4]], r = 1, c = 4
Output: [[1,2,3,4]]

Example 2:


Input: mat = [[1,2],[3,4]], r = 2, c = 4
Output: [[1,2],[3,4]]

'''
  
Code:
  
  class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        d1 = []
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                d1.append(mat[i][j])
                
        print(d1)
        if len(d1)==r*c:
            idx=0
            reshaped=[]
            for i in range(r):
                temp=[]
                for j in range(c):
                    temp.append(d1[idx])
                    idx+=1
                reshaped.append(temp)
            return reshaped
        else:
            return mat
