import heapq

class Task:
    def __init__(self, description, priority):
        self.description = description
        self.priority = priority

    def __lt__(self, other):
        return self.priority < other.priority

class PriorityQueue:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, priority):
        task = Task(description, priority)
        heapq.heappush(self.tasks, task)

    def get_highest_priority_task(self):
        if not self.is_empty():
            task = heapq.heappop(self.tasks)
            return task.description

    def is_empty(self):
        return len(self.tasks) == 0
