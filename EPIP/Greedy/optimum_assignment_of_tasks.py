"""
Each worker must be assigned exactly two tasks. Each task takes a fixed amount of time.
For example, if there are 6 tasks whose durations ate 5,2,1,6,4,4 hours, then an
optimum assignment is to give the first two tasks (i.e., the tasks with duration 5 and 2) to one
worker, the next two (1 and 6) to another worke1 and the last two tasks (4 and 4) to the last worker.
For this assignment, all tasks will finish after max(5 + 2,1 + 6,4 + 4) = 8 hours.
"""