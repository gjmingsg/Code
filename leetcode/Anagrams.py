class Solution:
    # @param strs, a list of strings
    # @return a list of strings
    def anagrams(self, strs):
        if len(strs)==1:
            return []
        hs = {}
        for i in strs:
            s=self.reverse(i)
            if hs.has_key(s)==False:
                hs[s]=[]
            hs[s].append(i)
        l=[]
        for key,item in hs.iteritems():
            if len(item)>1:
                for x in item:
                    l.append(x)
        return l
    
    def reverse(self,lstr):
        if len(lstr)<=1:
            return lstr
        l=[item for item in lstr]
        l.sort()
        return reduce(lambda x,y:x+y,l)


c = Solution()
#print c.reverse("123456")

print c.anagrams(["12345","54321","123"])


print c.anagrams(["",""]) == ["",""]

print c.anagrams(["","b"]) == []

print c.anagrams(["ant","ant"]) == ["ant","ant"]
print c.anagrams(["and","dan"]) == ["and","dan"]

