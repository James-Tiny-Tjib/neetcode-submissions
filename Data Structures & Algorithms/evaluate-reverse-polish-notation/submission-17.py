class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []
        
        for c in tokens:

            if c == "+":
                val2 = int(stack.pop())
                val1 = int(stack.pop())
                stack.append(str(int(val1+val2)))
            elif c == "-":
                val2 = int(stack.pop())
                val1 = int(stack.pop())
                stack.append(str(int(val1-val2)))
            elif c == "*":
                val2 = int(stack.pop())
                val1 = int(stack.pop())
                stack.append(str(int(val1*val2)))            
            elif c == "/":
                val2 = int(stack.pop())
                val1 = int(stack.pop())
                stack.append(str(int(val1/val2)) )          
            else:
                stack.append(c)
        
        return int(stack[0])
