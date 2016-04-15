class Solution:
    # @param path, a string
    # @return a string
    def simplifyPath(self, path):
        stack = []
        index = 0
        lindex = 0
        while index < len(path):
            top = stack[len(stack)-1]
            lindex = path.index('/',index+1)
            item = path[index,lindex]
            if item == '/..':
                #
            elif item == '/'
            
            
