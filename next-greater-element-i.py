class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        '''     
        What to use: 
            Nested for loops
            Output array
            
            Dictionary* (efficient)
            Stack* (efficient)
        
        A. Even more brute force: O(n^2)
        
        Go through the array, and nested loop and find the next greater element to the right and just add that greater element to the output and return that output array.




        B. Brute force:
        O(n*m)
        
        Summary: go through nums2 twice in nested loop to find ALL values that's the next greater element of nums2[i].
        Create a dict that has num1 items as key and index as value. 
        Create a return array size of nums1 preset to -1.
        
        1. Go through every num in nums1 and create a hashmap that pairs the num:index (using enumerate)
        2. Create a returning array output set to [-1]* len(nums1) so all defaults are -1.
        3. Go through every index in nums2 with a for loop:
            if nums2's value is not in nums1's dictionary num:
                skip
            but IF nums2 is in nums1 then we should use another for loop to go through num2's index and nums2 second index to find a value larger than nums2[i]:
                if we do find next greater value, get the dictionary index of the original value, assign it to a new variable (idx)
                now put our attention to the return output array of -1s. We're using that new variable (idx) and telling return output array where and what that new greater element should be in the returning output.
                
                
        
            
        '''
        
        '''   
        
        dictionary_nums1_index = {num:index for num, index in enumerate(nums1)}
        
        output_result = [-1] * len(nums1)
        
        for i in range(len(nums2)):
            if nums2[i] not in dictionary_nums1_index:
                continue
            if nums2[i] in dictionary_nums1_index:
                for j in range(i+1, len(nums2)):
                    if nums2[j] > nums2[i]:
                        new_high_index = dictionary_nums1_index[nums2[i]] # finding the value of nums2[i] in the dictionary and getting the index from the dictionary.
                        output_result[new_high_index] = nums2[j]
                        break
        return output_result
        
        
        '''
                        
        
        '''
        C. Efficient (Nick White's)
        
        1. initalize hashmap, key = current element of nums | value  = next greatest element of nums
        2. create new empty stack
        3. loop through nums2....(push a num onto stack later)
            4. (while stack is not empty and stack's top element is less than num):
                5. put into hashmap by popping it off stack as Key, and num into hashmap as Value
            6. push num into stack
        7. to recreate the output result array we want, for loop thru nums1 and make every element in nums1 the new value from the Dictionary's value OR return -1 as the default.
                
        
        
        
        
        
        
        
        D. Efficient (Neet's):
        O(n + m)
        
        1. Go through every element in nums1 and create a hashmap that pairs the num:index (using enumerate)
        2. Create a returning array output set to [-1]* len(nums1) so all defaults are -1.
        3. Create empty stack
        4. For loop thru index of nums2:
            5. create curr variable and assign nums2[i] to it for future uses..
            6. we want to know if nums2[i] is the next greater element on the top of stack (peeking top of stack is stack[-1])
            7. while current is larger than top of stack...
            8. pop top element out of stack using stack.pop and assign it to a variable called Value
            9. Now we want the index of the Value. So we use our hashmap and get the index of the Value by assigning it to idx
            10. Now set the result equal to curr (since curr is the real next greater value)
        11. if current is in hashmap:
            12. then its in the hash so let's add it to the stack so we can process it and check if what's the next greater element of it.
            13. if it doesn't show up, we don't have to append current to stack.
        14. return output_result
        '''
        
        dictionary_nums1_index = {num:index for index, num in enumerate(nums1)}
        
        output_result = [-1] * len(nums1)
        
        stack = []
        
        for i in range(len(nums2)):
            current = nums2[i] #nums2[i] is the value of nums2 elements
            #current = [1, 3, 4, 2]
            
            # while there is an element in stack AND that element on top of stack is smaller than current...(so if 3 > 1...which is true)
            while stack and current > stack[-1]:
                # assign value = 1
                # pop off top stack element
                value = stack.pop()
                # assign dictionary[1] as variable idx
                idx = dictionary_nums1_index[value]
                
                #output_result[dictionary[1]] = current...basically output_result's dictionary's index is now current 3.
                output_result[idx] = current
                #output_result = [-1, 3]
                
            # look up if current is in dictionary's key, if it does exist add it to stack.
            if current in dictionary_nums1_index:
                stack.append(current)
        return output_result
