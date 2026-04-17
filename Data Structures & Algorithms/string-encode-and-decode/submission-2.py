class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join(f"{len(s)}#{s}" for s in strs)


    def decode(self, s: str) -> List[str]:
        ans = []
        i = 0
        
        while i < len(s):
            # Find the delimiter starting from current position
            j = s.find('#', i)
            
            # Extract the length and jump to the start of the actual string
            length = int(s[i:j])
            start = j + 1
            end = start + length
            
            ans.append(s[start:end])
            
            # Move index to the start of the next length prefix
            i = end
            
        return ans


