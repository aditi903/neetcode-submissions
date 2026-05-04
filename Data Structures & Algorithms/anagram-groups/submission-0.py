class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictionary = defaultdict(list)

        for s in strs:
            sortedstring = ''.join(sorted(s))
            dictionary[sortedstring].append(s)
        return list(dictionary.values())