class Solution:
    def myAtoi(self, s: str) -> int: 
        
        num_map = {
        "0" : 0 , 
        "1" : 1 , 
        "2" : 2 , 
        "3" : 3 , 
        "4" : 4 ,
        "5" : 5 ,
        "6" : 6 ,
        "7" : 7 ,         
        "8" : 8 ,
        "9" : 9  }

        cleaned_input = []
        sign = 1
        valid_input = set(num_map.keys() )
        
        for char in  s :
           if char == "-" :
               sign = -1 

           if char in  valid_input :
               cleaned_input.append(char) 

        num = 0 

        print(cleaned_input)
        
        upper_bound =   2**31 - 1
        lower_bound =  -2**31
        for i,n  in enumerate(reversed(cleaned_input)) :
            
            num += num_map[n] * (10 ** i)
            
            if num * sign < lower_bound :
                num = lower_bound 
                break 
            if num * sign  > upper_bound :
                num = upper_bound 
                break 


        return num * sign


s = Solution()
n =  [ "+2345" , "   -1234 hello" , "  +123 " , "-12" , "3147483648"  ]

for i in n :
    print(s.myAtoi(i))

