class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_hash, t_hash = {}, {}

        for ch in range(len(s)):
            s_hash[s[ch]] = 1 + s_hash.get(s[ch], 0)
            t_hash[t[ch]] = 1 + t_hash.get(t[ch], 0)
        
        return t_hash == s_hash