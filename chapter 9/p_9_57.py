"""
One of the main applications of priority queues is in operating systems—
for scheduling jobs on a CPU. In this project you are to build a program
that schedules simulated CPU jobs. Your program should run in a loop,
each iteration of which corresponds to a time slice for the CPU. Each job
is assigned a priority, which is an integer between −20 (highest priority)
and 19 (lowest priority), inclusive. From among all jobs waiting to be processed
in a time slice, the CPU must work on a job with highest priority.
In this simulation, each job will also come with a length value, which is an
integer between 1 and 100, inclusive, indicating the number of time slices
that are needed to process this job. For simplicity, you may assume jobs
cannot be interrupted—once it is scheduled on the CPU, a job runs for a
number of time slices equal to its length. Your simulator must output the
name of the job running on the CPU in each time slice and must process
a sequence of commands, one per time slice, each of which is of the form
“add job name with length n and priority p” or “no new job this slice”.
"""

from HeapPriorityQueue import HeapPriorityQueue
from time import sleep
import re

REPATTERN = r"add job ([a-zA-Z]*) with length ([0-9]*) and priority (-?[0-9]*)"


class CPU:
    class CPUERROR(Exception):
        pass  # XD

    class CPUJOB:
        def __init__(self, name, len, pr):
            if not (-20 <= pr <= 19):
                raise CPU.CPUERROR('Priority mus be -20 <= and <= 19')
            self.name = name
            self.length = len
            self.priority = pr

        def cycle(self):
            self.length -= 1

        def prepare(self):
            return [self.pr, self]

        def __len__(self):
            return self.length

    def __init__(self):
        self._jobs = HeapPriorityQueue()
        self._waiting_jobs = []

    def add_job(self, job):
        self._waiting_jobs.append(job)

    def _prepare_jobs(self):
        self._jobs = HeapPriorityQueue([[job.priority, job] for job in self._waiting_jobs if len(job) > 0])
        self._waiting_jobs = []

    def _recycle_job(self, job):
        self._waiting_jobs.append(job)

    def do_cycle(self):
        self._prepare_jobs()
        while not self._jobs.is_empty():
            _, job = self._jobs.remove_min()
            job.cycle()
            self._recycle_job(job)

    def show_jobs(self):
        print('Jobs:')
        for job in self._waiting_jobs:
            print('\t{:>3}: {} => {} length'.format(job.priority, job.name, len(job)))


cpu = CPU()
cpu.add_job(CPU.CPUJOB('System', 1000, -20))
cpu.add_job(CPU.CPUJOB('Winap', 150, 10))
cpu.add_job(CPU.CPUJOB('Minecraft', 100, 5))

while True:
    cpu.do_cycle()
    cpu.show_jobs()
    resp = input('>>> ')
    rez = re.match(REPATTERN, resp)
    if rez:
        name, lenght, priority = rez.group(1), int(rez.group(2)), int(rez.group(3))
        cpu.add_job(CPU.CPUJOB(name, lenght, priority))
    else:
        print('No new job this slice')
