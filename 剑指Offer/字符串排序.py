#输入一个字符串,按字典序打印出该字符串中字符的所有排列。例如输入字符串abc,
# 则打印出由字符a,b,c所能排列出来的所有字符串abc,acb,bac,bca,cab和cba。
#全排列问题

def Permutation(ss,index):
    #用list 保存Index, 递归
    if len(index) == len(ss):
        str = ''
        for idx in index:
            str+=ss[idx]
        print(str)
        return
    else:
        for i in range(len(ss)):
            if i not in index:
                index.append(i)
                Permutation(ss,index)
                index.pop() #每次递归之后把当前的删除,尝试下一个

if __name__ == '__main__':
    Permutation('abc',[])