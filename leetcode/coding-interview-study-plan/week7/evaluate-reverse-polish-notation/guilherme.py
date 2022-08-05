from math import floor, ceil


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = '+-*/'
        for t in tokens:
            if t not in operators:
                stack.append(int(t))
            else:
                op2 = stack.pop()
                op1 = stack.pop()
                if t == '+':
                    stack.append(op1 + op2)
                elif t == '-':
                    stack.append(op1 - op2)
                elif t == '*':
                    stack.append(op1 * op2)
                elif t == '/':
                    result = op1 / op2
                    if result > 0:
                        stack.append(floor(result))
                    else:
                        stack.append(ceil(result))

        return stack.pop()