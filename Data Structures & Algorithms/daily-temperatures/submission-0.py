class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        # Get Result Array
        result = [0] * len(temperatures)

        temp_stack = []

        for i in range(len(temperatures)):

            while(temp_stack and temperatures[i] > temperatures[temp_stack[-1]]):
                index = temp_stack.pop()
                result[index] = i - index
            
            temp_stack.append(i)
        
        return result



