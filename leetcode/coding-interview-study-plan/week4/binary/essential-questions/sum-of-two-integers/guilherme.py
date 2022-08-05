class Solution:
    def getSum(self, a: int, b: int) -> int:
        soma = []
        signal = 0
        if a * b > 0:
            for i in range(abs(a)):
                soma.append('')
            for i in range(abs(b)):
                soma.append('')
            if a >= 0:
                signal = 1
            else:
                signal = -1
        elif a * b == 0:
            if a == 0:
                signal = b / abs(b)
                for i in range(abs(b)):
                    soma.append('')
            if b == 0:
                signal = a / abs(a)
                for i in range(abs(a)):
                    soma.append('')

        else:
            max_num = max(abs(a), abs(b))
            min_num = min(abs(a), abs(b))
            for i in range(max_num):
                soma.append('')
            for i in range(min_num):
                soma.pop()
            if max_num >= 0:
                signal = 1
            else:
                signal = -1
        print(soma)

        return int(signal * len(soma))
