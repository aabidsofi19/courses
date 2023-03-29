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

def two_sum_range(input : List[int] , target_start : int , target_end : int) -> int :
    
    count = 0

    l = 0 
    r = len(input) -1 
    pairs = []
    while r > l and l < r :
        print(l,r)
        
        pair_sum = input[l] + input[r] 
        print(pair_sum)
        print("pairs",input[l],input[r])

        if pair_sum >= target_start and pair_sum <= target_end :
            print("success") 
            count +=1 
            r-=1
            continue

        if pair_sum < target_start :
            l+=1 
            continue 
        if pair_sum > target_end :
            r-=1
            continue


    return count
        
        
        
        
def two_sum(nums):
    nums = {int(n) for n in nums}
    return sum(
        1
        for n in range(-10000, 10001)
        if any(n - x in nums and 2 * x != n for x in nums)
    )
      


# arr = [1,2,4,4,6,8,0]

# two_sum(arr,8)


def solution() :
    
    with open("./twoSum.testcase") as f :
          nums = [ int(l.strip())  for l in f.readlines() ]
    # nums = [-3,-1,1,2,9,11,7,6,2]
    # c= two_sum_range(sorted(nums),-10000,10000)

    # c= two_sum_range(sorted(nums),3,8)
    print("done", two_sum(nums) )

 



if __name__ == "__main__":
    ans = solution()
    print(ans)





