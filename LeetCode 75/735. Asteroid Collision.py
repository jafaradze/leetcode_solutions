from typing import List

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for i in range(len(asteroids)):

            while stack and asteroids[i] < 0 and stack[-1] > 0:
                if -asteroids[i] > stack[-1]:
                    stack.pop()
                    continue
                elif -asteroids[i] == stack[-1]:
                    stack.pop()
                break
            else:
                stack.append(asteroids[i])
        return stack
