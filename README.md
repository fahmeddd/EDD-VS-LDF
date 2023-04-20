# EDD vs LDF
# A Real Time Systems Class Project Spring 2023

Assignment:
Design, implement, and run an experiment which as input takes the following
parameters: a set of up to 20 tasks each with a computation time (ci) and
deadline (di).

* The experiment should test, likely through repeated experiments of different deadline
assignment (Di), two possible scheduling algorithms specifically by comparing the
feasibility of schedules created using the relative deadline within DM scheduling versus
the use of the actual deadline in EDF (or some other algorithm).
* If you want test something else (e.g., preemption vs. non-preemption you may do so as well, just
document it)

Implementation:
I will be implementing a Earliest Due Date & Latest Deadline First algorithm simulation in Python as a proof of concept to see how these can algorithms can perform. I will look at how both outputs are provided for a same task, for a simple demonstration to students.

* I did not consider constraints of optimization of speed based on different programming languages. In a practical sense, a real time system should be implemented in operating systems so the information can be presented and executed in a manner that behaves or works in conjunction with how a real-world system will behave.

