from typing import Tuple,List ,Callable 
from functools import reduce 

JOBS = List[Tuple[int,int]] # LIST[ ( weight , length )]


def calc_weigthed_sum(jobs : JOBS ) :

    completion_time = 0 
    sum_ = 0 

    for job in jobs :
        weight , length = job 
        completion_time += length 
        sum_ += completion_time * weight

    return sum_  



def schedule_jobs(jobs : JOBS , greedy_criteria : Callable[[int,int],int|float] ) -> int :
    """ shedules the jobs and returns the weighted sum of completion times """

    scheduled = sorted(jobs,key = lambda job : greedy_criteria(job[0],job[1]),reverse=True) 
    # print("scheduled_jobs" , scheduled)
    return calc_weigthed_sum(scheduled)



def load_jobs(file_name : str ) :
    with open(file=file_name) as f :
        lines = f.readlines()
        jobs = []
        for job in lines[1:] : 
            w , l = map(int ,job.split(" "))
            jobs.append((w,l))

    return jobs 



# jobs = [(3,1),(2,2),(1,3)]
# jobs = [(5, 6), (4, 1), (6, 7)]

def test(file ) :

  print(f"[+] testing {file}")
  jobs = load_jobs(file)

  schedule_1 = schedule_jobs(jobs, greedy_criteria = lambda w , l : ( w - l  , w )) 
  schedule_2 = schedule_jobs(jobs, greedy_criteria = lambda w , l : w / l  ) 

  print(f"schedule using difference",schedule_1)
  print(f"schedule using ratio",schedule_2) 
  assert schedule_2 <= schedule_1

test("jobs.testcase")
