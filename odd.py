class Solution:
    def oddEven(self, s: str) -> str:
   
        x = 0
        y = 0
        count = [0] * 27
        
        for i in range(len(s)):
            count[ord(s[i]) - ord('a') + 1] += 1
        
        for i in range(1, 27):
            if count[i] != 0 and count[i] % 2 == 0 and i % 2 == 0:
                x += 1
            elif count[i] % 2 == 1 and i % 2 == 1:
                y += 1
        
        sum_val = x + y
        if sum_val % 2 == 1:
            return "ODD"
        else:
            return "EVEN"

        

