from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {"+", "-", "*", "/"}

        for token in tokens:
            if token not in operators:
                # token is a number
                stack.append(int(token))
            else:
                # token is an operator
                b = stack.pop()  # right operand
                a = stack.pop()  # left operand

                if token == "+":
                    stack.append(a + b)
                elif token == "-":
                    stack.append(a - b)
                elif token == "*":
                    stack.append(a * b)
                else:  # token == "/"
                    # truncate toward zero
                    stack.append(int(a / b))

        # final result
        return stack[-1]