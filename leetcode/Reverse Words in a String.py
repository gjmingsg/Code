class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        if s=='':
            return ''
        lw = s.strip().split(' ')
        #print lw
        lw.reverse()
        st=""
        #print lw
        for item in lw:
            if item.strip()=='':
                continue
            st+=(item.strip())
            st+=' '
        return st.strip()


            
        
c = Solution()
print c.reverseWords( "the sky is blue")
print c.reverseWords( " the sky   is blue ")
