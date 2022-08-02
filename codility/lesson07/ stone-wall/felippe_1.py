class Solution:
    def hammingWeight(self, n: int) -> int:
        bin_n = bin(n)[2:]
        return bin_n.count('1')