def revertInt(x):
    """
    :param x: int
    :return: int
    """
    ret = 0
    Int_Max = pow(2, 32) - 1
    Int_Min = -pow(2, 32)

    while x != 0:
        pop = x % 10
        x /= 10
        if ret * 10 > Int_Max or (ret * 10 == Int_Max and pop > 7):
            return 0
        if ret * 10 < Int_Min or (ret * 10 == Int_Min and pop < -8):
            return 0
        ret = ret * 10 + pop
    return ret


class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        ret = 0
        Int_Max = 0x7FFFFFFF
        # Int_Min = 0x80000000

        if x < 0:
            return - self.reverse(-x)
        while x != 0:
            pop = x % 10
            x = x // 10
            if ret * 10 > Int_Max or (ret * 10 == Int_Max and pop > 7):
                return 0
            ret = ret * 10 + pop
        return ret

