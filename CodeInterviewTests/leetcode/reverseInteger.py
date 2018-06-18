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

# def revertInt2(x):
#     if x < 0:
#         return -revertInt2(-x)
#     for(;x != 0; x/=10):
#         d = x % 10
#         if d < 8:
#             if x > Int_Max
#         if x > (d < 8 ? Int_Max : Int_Min):
