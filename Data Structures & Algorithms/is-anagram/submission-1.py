class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        list1 = {}
        list2= {}
        for char in s:
            if char not in list1:
                list1[char]=1
            else:
                list1[char]+=1
        for char in t:
            if char not in list2:
                list2[char]=1
            else:
                list2[char]+=1
        return list1 == list2
