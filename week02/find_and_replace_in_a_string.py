class Solution:
    # TC: O(NS), N = number of indices, S =  the average lenth of source strings.
    # SC: O(N), N = lenth Of string.
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        string_array = list(s)

        # We are iterating through the indices, sources and target simultaneously.
        for (index, source, target) in zip(indices, sources, targets):
            # For every index we check whether it has the source strings. If not,
            # then we move to the next indexes.
            if not s.startswith(source, index):
                continue
            else:
                # It came to this block, means it has the source strings. We replace 
                # the the current index string with sources string, but we make rest of
                # the strings empty.
                string_array[index] = target
                for i in range(index + 1, index + len(source)):
                    string_array[i] = ""
        return "".join(string_array)
