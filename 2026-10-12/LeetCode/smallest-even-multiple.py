class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        # c=n*2
        # cm =[]
        # for i in range (1,c+1):
        #     if i%2 == 0 and i%n == 0:
        #         cm.append(i)
        # return cm[0]
        
        if n%2 ==0:
            return n
        else:
            return n*2

        