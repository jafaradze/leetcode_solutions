class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        st = []
        total = 0
        if x > y:   # ab > ba
            for i in range(len(s)):
                if s[i] == 'b' and st and st[-1] == 'a':
                    total += x
                    st.pop()
                else:
                    st.append(s[i])
            st2 = []
            for i in range(len(st)):
                if st[i] == 'a' and st2 and st2[-1] == 'b':
                    total += y
                    st2.pop()
                else:
                    st2.append(st[i])
        else:   # ba > ab
            for i in range(len(s)):
                if s[i] == 'a' and st and st[-1] == 'b':
                    total += y
                    st.pop()
                else:
                    st.append(s[i])
            st2 = []
            for i in range(len(st)):
                if st[i] == 'b' and st2 and st2[-1] == 'a':
                    total += x
                    st2.pop()
                else:
                    st2.append(st[i])
        return total