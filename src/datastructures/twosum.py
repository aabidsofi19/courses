"""
The goal of this problem is to implement a variant of the 2-SUM algorithm covered in this week's lectures.

The file contains 1 million integers, both positive and negative (there might be some repetitions!).
This is your array of integers, with the ithith row of the file specifying the ithith entry of the array.

Your task is to compute the number of target values `t` in the interval [-10000,10000] (inclusive) 
such that there are distinct numbers x,y in the input file that satisfy x+y = t. 
(NOTE: ensuring distinctness requires a one-line addition to the algorithm from lecture.)

Write your numeric answer (an integer between 0 and 20001) in the space provided.

"""


from typing import List
from collections import defaultdict

def two_sum(input : List[int] , t : int) -> int :
    
    seen = defaultdict(lambda : 0,{})
    count = 0

    for x in input :
        seen[x] += 1
        y = t - x 
        # print("x" ,x ,"needed" , y ) 

        if seen[y] > 0 :
            count +=1
            # print(x,y)
            seen[y] -= 1
            break
    
    return count 


# arr = [1,2,4,4,6,8,0]

# two_sum(arr,8)


def solution() :
    
    with open("./twoSum.testcase") as f :
         nums = [ int(l.strip())  for l in f.readlines() ]
    # nums = [-3,-1,1,2,9,11,7,6,2]
    count = 0 
    for t in range(-10000,10001) : 
        c= two_sum(nums,t)
        # print("done t",t , c )
        count += c 

    return count 
 



if __name__ == "__main__":
    ans = solution()
    print(ans)





