class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
      #Create hash map
      res = defaultdict(list)
      
      for s in strs:
        count = [0]*26  
        #evey single char in each string
        for c in s:
            count[ord(c)-ord('a')] += 1
        #count to append(S)
        res[tuple(count)].append(s)
      
      return list(res.values())