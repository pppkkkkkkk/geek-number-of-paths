class Solution:
    def numberOfPaths(self, m, n):
        # code here
        # pathCnt = 0
        
        # def dp(i, j, m, n):
        #     nonlocal pathCnt
        #     if i>=m or j>=n:
        #         return
        #     if i==m-1 and j==n-1:
        #         pathCnt += 1
        #     dp(i+1,j, m, n)
        #     dp(i,j+1, m, n)
            
        # dp(0,0,m,n)
        
        # return pathCnt
        dict = {}
        dict[m-1,n-1] = 1
        def dp (i,j,m,n):
            nonlocal dict
            if (i,j)  in dict:
                return dict[(i,j)]
            if i+1<m and j+1<n:
                ans = dp(i+1,j,m,n) + dp(i,j+1,m,n)
                dict[(i,j)] = ans
                return ans 
            if j+1<n:
                ans = dp(i,j+1,m,n)
                dict[(i,j)] = ans
                return ans
            if i+1<m:
                ans = dp(i+1,j,m,n)
                dict[(i,j)] = ans
                return ans
            return 0
            
        return dp(0,0,m,n)