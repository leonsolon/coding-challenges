class Solution:
    def addBinary(self, a: str, b: str) -> str:
        len_a = len(a)
        len_b = len(b)
        diff = abs(len_a - len_b)
        if len_a > len_b:
            b = '0' * diff + b

        if len_b > len_a:
            a = '0' * diff + a

        print(a, b)

        take_away = '0'
        result = ''
        for bit_a, bit_b in zip(a[::-1], b[::-1]):
            # print(bit_a, bit_b, take_away)
            if bit_a == bit_b:
                result += take_away
                if bit_a == '1':
                    take_away = '1'
                else:
                    take_away = '0'
            else:
                if take_away == '1':
                    result += '0'
                else:
                    result += '1'
            # print(result, take_away)

        if take_away == '1':
            result += '1'

        result = result[::-1]
        return result        