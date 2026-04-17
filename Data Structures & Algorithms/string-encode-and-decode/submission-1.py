class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""

        for st in strs:
            n = len(st)
            s += str(n)
            s += '#'
            s += st
        print(s)
        return s


    def decode(self, s: str) -> List[str]:
        ans = []
        i = 0
        n = len(s)

        while i < n:
            st = ""
            j = i
            run_length = 0

            while j < n and s[j].isdigit():
                run_length *= 10
                run_length += int(s[j])
                j += 1
            
            if s[j] == '#':
                st += s[j+1: j+1+run_length]
                ans.append(st)
                i = j + 1 + run_length
            else:
                i += 1
        
        return ans


