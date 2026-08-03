class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        num_stack = []
        for t in tokens:
            if t == '+':
                num_1 = num_stack[-2]
                num_2 = num_stack.pop()
                num_stack[-1] = num_1 + num_2
            elif t == '-':
                num_1 = num_stack[-2]
                num_2 = num_stack.pop()
                num_stack[-1] = num_1 - num_2
            elif t == '*':
                num_1 = num_stack[-2]
                num_2 = num_stack.pop()
                num_stack[-1] = num_1 * num_2
            elif t == '/':
                num_1 = num_stack[-2]
                num_2 = num_stack.pop()
                num_stack[-1] = int(num_1 / num_2)
            else:
                num_stack.append(int(t))

        return num_stack[0]   
                
