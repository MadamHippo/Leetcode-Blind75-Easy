class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        # make a hash set of characters...with AEIOU (upper/lower for edge cases)
        # make 2 pointers, l and r at start and end of string
        # while l has not crossed r...
            # if s[left] not in hash, increase left by 1
            # if s[right] not in hash, decrease right by 1
            
        # But if s[left] AND s[right] is in hash:
            # then you can swap them so do a swap:
                # python can use reassignment
                # and now still you have to l+=1 and r-=1
                
        
        hashset = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]
        
        s = list(s)
        left, right = 0, len(s)-1
        
        while left < right:
            if s[left] not in hashset: 
            # why didn't I need another while check like the other example?
                left += 1
            if s[right] not in hashset:
                right -= 1

            # why do I need this line below?:
            if s[left] in hashset and s[right] in hashset:
                
                # swap
                s[left], s[right] = s[right], s[left]
                left += 1
                right -=1
            # return 
            '''
            java's version of swap
            
                temp = s[left]
                s[left++] = s[right]
                s[right--] = temp
            
            python's version of swap
            
                tmp = s[l]
                s[l] = s[r]
                s[r] = tmp
                
                l += 1
                r -= 1
            '''
            
        return "".join(s)
