class Solution:
    def isValid(self, word: str) -> bool:
        vow = 'aeiouAEIOU'
        dig = '0123456789'
        return word.isalnum() and any(char for char in word if char in vow) and \
            any(char for char in word if char not in dig + vow) and len(word) >= 3