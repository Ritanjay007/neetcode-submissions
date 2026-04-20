class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map= defaultdict(list)
        max_char=26
        
        for s in strs:
            count = [0]* max_char
            for c in s:
                count[ord(c) - ord('a')] +=1
            
            anagram_map[tuple(count)].append(s)
        return list(anagram_map.values())