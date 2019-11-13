# NaivePriorityQueue (aka 'ShittyQueue'): A simple but inefficient priority queue.
# Your implementation should pass the tests in test_naive_priority_queue.py.
# Lauryn Gomez 

class NaivePriorityQueue:
    def __init__(self):
        self.data=[]

    def enqueue(self, job):
        self.data.append(job)

    def dequeue(self):
        if self.is_empty():
            return None
        else:
            hp_job = self.data[0]
            for job in self.data:
                if job > hp_job:
                    hp_job = job
            self.data.remove(hp_job)
            return hp_job

    def is_empty(self):
        return len(self.data) == 0