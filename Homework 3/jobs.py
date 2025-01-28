from dataclasses import dataclass
from heapq import heapreplace, heappush

@dataclass
class Job:
   profit: int
   deadline: int

def max_profit_jobs(jobs):
    # Sort jobs by profit in descending order
    jobs.sort(key = lambda x: x.profit, reverse = True)

    # Use priority queue (min-heap) to track scheduled jobs
    heap = [ ]

    # Schedule each job
    for job in jobs:
        # If there is space in the heap, push job
        if len(heap) < job.deadline:
            heappush(heap, job.profit)

        # Else, if heap is full and current job has higher profit, use it to replace job with smallest profit
        elif heap[0] < job.profit:
            heapreplace(heap, job.profit)

    # Calculate total profit from jobs in the heap
    total_profit = sum(heap)

    return total_profit

# Example usage
if __name__ == "__main__":
    jobs = [
        Job(100, 2),
        Job(19, 1),
        Job(27, 2),
        Job(25, 1),
        Job(15, 3)
    ]

    print("Max profit =", max_profit_jobs(jobs))