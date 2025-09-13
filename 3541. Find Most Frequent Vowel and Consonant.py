class Solution:
    def maxFreqSum(self, s: str) -> int:
        counter_vow = dict()
        counter_con = dict()
        for char in s:
            if char in 'aouie':
                counter_vow[char] = counter_vow.get(char, 0) + 1
            else:
                counter_con[char] = counter_con.get(char, 0) + 1
        max_vow = 0 if counter_vow == {} else max(counter_vow.values())
        max_con = 0 if counter_con == {} else max(counter_con.values())
        return max_vow + max_con
        