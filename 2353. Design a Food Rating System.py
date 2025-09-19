import heapq
from collections import defaultdict
from typing import List

class FoodRatings:
    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.foods = {}
        self.cuisine_heaps = defaultdict(list)

        for f, c, r in zip(foods, cuisines, ratings):
            self.foods[f] = [c, r]
            heapq.heappush(self.cuisine_heaps[c], (-r, f))

    def changeRating(self, food: str, newRating: int) -> None:
        cuisine, _ = self.foods[food]
        self.foods[food][1] = newRating
        heapq.heappush(self.cuisine_heaps[cuisine], (-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        heap = self.cuisine_heaps[cuisine]
        while heap:
            rating, food = heap[0]
            if -rating == self.foods[food][1]:
                return food
            heapq.heappop(heap)

food = ["kimchi", "miso", "sushi", "moussaka", "ramen", "bulgogi"]
cuisine = ["korean", "japanese", "japanese", "greek", "japanese", "korean"]
rating = [9, 12, 8, 15, 14, 7]
foodratings = FoodRatings(food, cuisine, rating)
print(foodratings.highestRated("korean"))
print(foodratings.highestRated("japanese"))
foodratings.changeRating("sushi", 16)
print(foodratings.highestRated("japanese"))
foodratings.changeRating("ramen", 16)
print(foodratings.highestRated("japanese"))

