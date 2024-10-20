class MinStack:
    def __init__(self) -> None:
        self.min_max_stack = []
        self.stack = []

    # O(1) time
    def peek(self):
        return self.stack[-1] if self.stack else None

    # O(1) time
    def push(self, value):
        new_min_max = {"min": value, "max": value}
        if self.stack:
            new_min_max["min"] = min(new_min_max["min"], self.min_max_stack[-1]["min"])
            new_min_max["max"] = max(new_min_max["max"], self.min_max_stack[-1]["max"])
        
        self.min_max_stack.append(new_min_max)
        self.stack.append(value)
    
    # O(1) time
    def get_min(self):
        return self.min_max_stack[-1]["min"] if self.stack else None
    
    # O(1) time
    def get_max(self):
        return self.min_max_stack[-1]["max"] if self.stack else None
    
    # O(1) time
    def pop(self):
        if not self.stack:
            return None

        self.min_max_stack.pop()
        return self.stack.pop()