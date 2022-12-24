class Solution:
    # TC: 0(N*K) N = number of strings, K = Maximum size of K
    # SC: O(N*K) N = Number of hashes in the worst case, K = Maximum size of of a string 
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        # For every string we are generating a specific hash key.
        # The hash keys depends on the difference of each character.
        def generate_key(string: str) -> str:
            key_list = []
            for (a,b) in zip(string, string[1:]):
                key_list.append(chr((ord(b) - ord(a)) % 26 + ord('a')))
            return "".join(key_list)
        
        group_map = collections.defaultdict(list)
        # We will populate the map using the hashkeys.
        for string in strings:
            hash_key = generate_key(string)
            group_map[hash_key].append(string)
        
        return list(group_map.values())
