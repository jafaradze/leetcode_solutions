class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        from collections import Counter

        w1 = Counter(word1)
        w2 = Counter(word2)
        return sorted(w1.values()) == sorted(w2.values()) and set(w1.keys()) == set(w2.keys())