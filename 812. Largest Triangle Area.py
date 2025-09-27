from typing import List

class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        max_s = 0
        for i in range(len(points) - 2):
            x1, y1 = points[i]
            for j in range(i + 1, len(points) - 1):
                x2, y2 = points[j]
                for k in range(j + 1, len(points)):
                    x3, y3 = points[k]
                    a = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
                    b = ((x2 - x3) ** 2 + (y2 - y3) ** 2) ** 0.5
                    c = ((x1 - x3) ** 2 + (y1 - y3) ** 2) ** 0.5
                    if a + b > c and a + c > b and b + c > a:
                        p = (a + b + c) / 2
                        S = (p * (p - a) * (p - b) * (p - c)) ** 0.5
                        max_s = max(max_s, S)
        return max_s