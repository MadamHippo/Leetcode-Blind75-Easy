class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        # Simple elengant Monotone stack
        
      
        # O(n) time and space
        result = [0] * len(temperatures)


        # extra memory stack that contains a pair of memories (value and index as a pair)
        # defined as a list of pairs or tuples
        stack = [] # pair : [temperature, index location]


        # since temperature is List of number digits with a location (index) we use enumerate
        for index, temperature in enumerate(temperatures):
            
            # while stack we initalized and temperature list is bigger than the top of the stack...
            while stack and temperature > stack[-1][0]:

                # unpack the tuple off the top of the stack and assign the unpacked tuple values to variables...
                stackTemperature, stackIndex = stack.pop()

                # The stackTemperature and stackIndex variables are then used to calculate the temperature difference between the current temperature and the previous higher temperature
                result[stackIndex] = (index - stackIndex)

            # store the result in the result list using tuple notation
            stack.append([temperature, index])

        return result


'''
Yes, this code is using pairs or tuples in the form of a list with two elements.

In the code, the stack variable is defined as a list of pairs or tuples, where each pair contains a temperature value and its index location. The pairs are represented as lists with two elements, e.g., [temperature, index].

When the code executes the while loop, it checks whether the stack is not empty and whether the current temperature is greater than the temperature of the last element in the stack. If both conditions are true, it pops the last element from the stack and assigns its temperature and index values to the stackTemperature and stackIndex variables, respectively, using tuple unpacking:

stackTemperature, stackIndex = stack.pop()

The stackTemperature and stackIndex variables are then used to calculate the temperature difference between the current temperature and the previous higher temperature, and store the result in the result list using tuple notation:

result[stackIndex] = (index - stackIndex)

Overall, this code is using tuples in a list format to store pairs of temperature values and their corresponding index locations, and to calculate and store temperature differences as tuples in the result list.
'''
