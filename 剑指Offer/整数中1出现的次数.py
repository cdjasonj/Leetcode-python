#求出1~13的整数中1出现的次数,并算出100~1300的整数中1出现的次数？
# 为此他特别数了一下1~13中包含1的数字有1、10、11、12、13因此共出现6次,
# 但是对于后面问题他就没辙了。ACMer希望你们帮帮他,
# 并把问题更加普遍化,可以很快的求出任意非负整数区间中1出现的次数（从1 到 n 中1出现的次数）。



def NumberOf1Between1AndN_Solution(self, n):
    #1-10 个位数出现1 ， 出现1 次
    #1-100 十位数出现1， 出现 10 次  10 11 12 .
    #1-1000 百位数出现 ，出现100次， 100 101 102 -- 199
    # 1-10^i 右边第二数，数字出现10^(i-1)次
    #