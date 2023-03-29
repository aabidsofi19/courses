from typing import Tuple, List, Callable

# Define type alias for jobs list
JOBS = List[Tuple[int, int]]  # LIST[ (weight, length) ]


def calc_weighted_sum(jobs: JOBS) -> int:

    """
    Calculates the weighted sum of completion times of the given jobs.

    :param jobs: A list of job tuples, where each tuple contains two integers:
    the job weight and length.
    :return: An integer representing the weighted sum of completion times.
    """
    completion_time = 0
    sum_ = 0

    # Iterate through jobs and calculate completion times and sum
    for job in jobs:
        weight, length = job
        completion_time += length
        sum_ += completion_time * weight

    return sum_


def schedule_jobs(
    jobs: JOBS, greedy_criteria: Callable[[int, int], int | float]
) -> int:
    """
    Schedules the given jobs according to the specified greedy criteria and
    returns the weighted sum of completion times.

    :param jobs: A list of job tuples, where each tuple contains two integers:
    the job weight and length.
    :param greedy_criteria: A function that takes two integers representing
    the job weight and length, and returns a score
                            that is used to sort the jobs in decreasing order.
    :return: An integer representing the weighted sum of completion times of
    the scheduled jobs.
    """
    # Sort the jobs using the specified greedy criteria
    scheduled = sorted(
        jobs, key=lambda job: greedy_criteria(job[0], job[1]), reverse=True
    )
    # Calculate the weighted sum of completion times of the scheduled jobs
    return calc_weighted_sum(scheduled)


def load_jobs(file_path: str) -> JOBS:
    """
    Loads job data from a file and returns a list of job tuples.

    :param file_path: A string representing the path to the file containing
    the job data.
    :return: A list of job tuples, where each tuple contains two integers: the
    job weight and length.
    """
    with open(file=file_path) as f:
        lines = f.readlines()
        jobs = []
        for job in lines[1:]:
            w, l = map(int, job.split(" "))
            jobs.append((w, l))

    return jobs


def test(file_path: str) -> None:
    """
    Runs tests on the scheduling algorithm using job data from a file.

    :param file_path: A string representing the path to the file containing
    the job data.
    :return: None
    """
    # Print the name of the file being tested
    print(f"[+] Testing {file_path}")
    # Load the job data from the file
    jobs = load_jobs(file_path)
    # Schedule the jobs using the difference greedy criterion
    schedule_1 = schedule_jobs(jobs, greedy_criteria=lambda w, l: (w - l, w))
    # Schedule the jobs using the ratio greedy criterion
    schedule_2 = schedule_jobs(jobs, greedy_criteria=lambda w, l: w / l)
    # Print the results of the two schedules
    print("Schedule using difference criterion:", schedule_1)
    print("Schedule using ratio criterion:", schedule_2)

    # because schedule_2 is most optimal
    assert schedule_2 <= schedule_1
