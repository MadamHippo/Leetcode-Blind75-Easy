'''
The problem asks you to find the product of all elements in an array except the current element at each index. Here's a step-by-step solution that is simple and straightforward:

Create an output array of the same length as the input array, with all elements initialized to 1. This array will store the final result.
Create two variables, left_product and right_product, both initialized to 1. These variables will be used to keep track of the product of elements to the left and right of the current element, respectively.
Loop through the input array from left to right. In each iteration, multiply left_product by the current element, and then store the result in the corresponding position of the output array. Then, update left_product by multiplying it by the current element.
Reset right_product to 1, and loop through the input array again, but this time from right to left. In each iteration, multiply right_product by the current element, and then multiply the corresponding position of the output array by right_product. Finally, update right_product by multiplying it by the current element.
Return the output array.
In this solution, we use two loops to calculate the product of elements to the left and right of each element in the input array. By multiplying the output array by left_product and right_product in each iteration, we are able to obtain the final result of the product of all elements except the current element at each index.
'''

        # O(n) Time and O(n) Space Solution


        N = len(nums)

        
        left_prefix = [1]*N
        right_suffix = [1]*N
        
        for i in range(1, N):
            # we start at index 1 instead of 0 because we are starting there to create sort of a dummy node to prevent tons of edge cases.
            left_prefix[i] = nums[i-1] * left_prefix[i-1]
            print(left_prefix)
                    
        for i in reversed(range(0, N-1)):  #range(N-2, -1, -1)
            # N - 1 because we want to reference it in the calculations AND dummy node purposes to prevent edge cases.
            right_suffix[i] = nums[i+1] * right_suffix[i+1]
        
            print(right_suffix)
            
        for i in range(len(nums)):
            nums[i] = left_prefix[i] * right_suffix[i]
            
        return nums
