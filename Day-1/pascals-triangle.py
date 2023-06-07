class Solution(object):
    def generate(self, numRows):
        ans = [[1]]
        for i in range(1,numRows):
            k = [1]
            j=1
            while j<i:
                k.append(prev[j-1]+prev[j])
                j+=1
            k.append(1)
            ans.append(k)
            prev = k
        return ans