# NaivePriorityQueue (aka 'ShittyQueue'): A simple but inefficient priority queue.
# Your implementation should pass the tests in test_naive_priority_queue.py.
# Lauryn Gomez 

class NaivePriorityQueue:
    def __init__(self, data = None):
        self.data = list()

    def enqueue(self, job):
        self.data.append(job)

    def dequeue(self):
        return self.data.pop()
