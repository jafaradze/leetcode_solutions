from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars) == 1:
            return 1
        cur_char = chars[0]
        count = 1
        res = ''
        for i in range(1, len(chars)):
            if chars[i] != chars[i - 1]:
                if count == 1:
                    res += cur_char
                else:
                    res += cur_char + str(count)
                cur_char = chars[i]
                count = 1
            else:
                count += 1
        res += cur_char + (str(count) if count != 1 else '')
        chars[:] = list(res)
        return len(chars)

