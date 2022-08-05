class Solution:
    def isValid(self, s: str) -> bool:
        opened_characters = []
        for i, el in enumerate(s):
            if el in '([{':
                opened_characters += el
            else:
                if len(opened_characters) <= 0:
                    return False
                else:
                    el_open = opened_characters.pop()
                    if el_open == '(' and el != ')':
                        return False
                    elif el_open == '[' and el != ']':
                        return False
                    if el_open == '{' and el != '}':
                        return False

        if len(opened_characters) > 0:
            return False
        else:
            return True