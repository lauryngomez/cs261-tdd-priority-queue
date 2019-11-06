# Job: A process or task that has a priority.
# Your implementation should pass the tests in test_job.py.
# LAURYN GOMEZ

class Job:

    def __init__(self, priority = None, message = None):
        self.priority = priority
        self.message = message
        
    def __eq__(self, job):
        return self.priority == job.priority
    
    def __lt__(self, job):
        return self.priority < job.priority
    
    def __gt__(self, job):
        return self.priority > job.priority