class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj_list = {c: set() for w in words for c in w}
        in_deg = {c: 0 for w in words for c in w}

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i+1]
            min_len = min(len(w1), len(w2))
            
            # Prefix check: if "apple" comes before "app", it's invalid
            if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
                return ""

            for j in range(min_len):
                if w1[j] != w2[j]:
                    if w2[j] not in adj_list[w1[j]]:
                        adj_list[w1[j]].add(w2[j])
                        in_deg[w2[j]] += 1
                    break # Only the first differing character defines the order

        q = deque([c for c in in_deg if in_deg[c] == 0])
        res = []
        while q:
            char = q.popleft()
            res.append(char)
            for neighbor in adj_list[char]:
                in_deg[neighbor] -= 1
                if in_deg[neighbor] == 0:
                    q.append(neighbor)

        return "".join(res) if len(res) == len(in_deg) else ""   