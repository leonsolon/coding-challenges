class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def generateParenthesisRecursion(str_parenthesis, need_to_open, need_to_close):
            if need_to_open == 0 and need_to_close == 0:
                result.append(str_parenthesis)
                return

            if need_to_open > 0:
                generateParenthesisRecursion(str_parenthesis + "(", need_to_open - 1, need_to_close + 1)

            if need_to_close > 0:
                generateParenthesisRecursion(str_parenthesis + ")", need_to_open, need_to_close - 1)

        generateParenthesisRecursion('', n, 0)

        return result