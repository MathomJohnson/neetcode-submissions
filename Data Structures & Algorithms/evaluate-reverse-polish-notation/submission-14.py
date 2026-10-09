class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []

        for t in tokens:
            if t == "+":
                op1 = stack.pop()
                op2 = stack.pop()
                stack.append(str(int(op1) + int(op2)))
            elif t == "-":
                op1 = stack.pop()
                op2 = stack.pop()
                stack.append(str(int(op2) - int(op1)))
            elif t == "*":
                op1 = stack.pop()
                op2 = stack.pop()
                stack.append(str(int(op1) * int(op2)))
            elif t == "/":
                op1 = stack.pop()
                op2 = stack.pop()
                stack.append(str(int(int(op2) / int(op1))))
            else:
                stack.append(t)

        return int(stack[0])