class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []

        numbers = list(range(2, 10))
        letters = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i'], ['j', 'k', 'l'], ['m', 'n', 'o'],
                   ['p', 'q', 'r', 's'], ['t', 'u', 'v'], ['w', 'x', 'y', 'z']]
        dict_digitis = dict(zip(numbers, letters))
        # print(dict_digitis)

        possible_letters = []
        for digit in digits:
            possible_letters.append(dict_digitis[int(digit)])

        # print(possible_letters)
        possible_letters = possible_letters[::-1]
        while len(possible_letters) >= 2:
            letter1 = possible_letters.pop()
            letter2 = possible_letters.pop()
            # print(letter1, letter2)
            new_letter = []
            for l1 in letter1:
                for l2 in letter2:
                    new_letter.append(l1 + l2)
            possible_letters.append(new_letter)
            # print(new_letter, possible_letters)

        return possible_letters[0]
