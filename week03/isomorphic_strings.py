class Solution:
    # TC: O(n + n) -> 0(n), n = size of s or t
    # SC: o(n + n) -> 0(n) ->, n = 26 -> O(1)
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_map = {}
        t_map = {}

        for s_char, t_char in zip(s, t):
            # We are mapping both strings to each other and it is necessary.
            # For example: if s = "bar" and t = "foo". If we map them correctly,
            # b -> f, a -> o, r -> o. If we just mapped only one string, but not
            # with each other, this mistake would not have been detected.
            if ((s_char in s_map) and (s_map[s_char] != t_char)) or ((t_char in t_map) and (t_map[t_char] != s_char)):
                return False

            s_map[s_char] = t_char
            t_map[t_char] = s_char
        
        return True
