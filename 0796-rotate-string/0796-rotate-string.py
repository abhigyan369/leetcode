class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        new_string = s + s
        if len(goal) < len(s): return False
        if goal in new_string:
            return True
        return False