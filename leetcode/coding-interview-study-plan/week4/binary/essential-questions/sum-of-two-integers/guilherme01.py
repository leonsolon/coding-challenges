class Solution:
    def add_bin(self, bin_a, bin_b):
        bit_sum = ''
        take_away = 0

        for bit_a, bit_b in zip(bin_a[::-1], bin_b[::-1]):
            # print(bit_a, bit_b, take_away)
            if bit_a == bit_b:
                bit_sum += str(take_away)
                if bit_a == '1':
                    take_away = 1
                else:
                    take_away = 0
            else:
                if take_away == 1:
                    bit_sum += '0'
                else:
                    bit_sum += '1'

        if take_away == 1:
            bit_sum += '1'
        bit_sum = bit_sum[::-1]
        return int(bit_sum, 2)

    def sub_bin(self, bin_a, bin_b):
        bit_sub = ''
        give_away = 0

        for bit_a, bit_b in zip(bin_a[::-1], bin_b[::-1]):
            # print(bit_a, bit_b, give_away)
            if give_away == 1:
                if bit_a == '1':
                    bit_a = '0'
                    give_away = 0
                else:
                    bit_a = '1'

            if bit_a == bit_b:
                bit_sub += '0'
            else:
                bit_sub += '1'
                if bit_a == '0':
                    give_away = 1

        bit_sub = bit_sub[::-1]
        return int(bit_sub, 2)

    def getSum(self, a: int, b: int) -> int:
        if a == 0:
            return b
        elif b == 0:
            return a
        elif b == a:
            return 2 * a

        bin_a = bin(abs(a))[2:]
        bin_b = bin(abs(b))[2:]
        len_bin_a = len(bin_a)
        len_bin_b = len(bin_b)
        diff = len_bin_a - len_bin_b
        if diff > 0:
            bin_b = abs(diff) * '0' + bin_b

        if diff < 0:
            bin_a = abs(diff) * '0' + bin_a

        signal = 1
        if (a * b) > 0:
            if a < 0:
                signal = -1

            return signal * self.add_bin(bin_a, bin_b)
        else:
            print('sub')
            if abs(b) > abs(a):
                num = b
                result = self.sub_bin(bin_b, bin_a)

            else:
                num = a
                result = self.sub_bin(bin_a, bin_b)

            signal = int(num / abs(num))
            return signal * result