class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for oper in tokens:
            if oper == "+":
                stack.append(stack.pop() + stack.pop())
            elif oper == "-":
                a,b = stack.pop(), stack.pop()
                stack.append(b-a)
            elif oper == "*":
                stack.append(stack.pop() * stack.pop())
            elif oper == "/":
                a,b = stack.pop(), stack.pop()
                stack.append(int( float(b / a)))
            else:
                stack.append(int(oper))
        
        return int(stack[-1])
        