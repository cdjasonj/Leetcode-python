# -*- coding:utf-8 -*-
def GetNumberOfK( data, k):
    # write code here
    count = 0
    for idx, _data in enumerate(data):

        if _data == k:
            count += 1

            for j in range(idx + 1, len(data) - 1):
                if data[j] == k:
                    count += 1
                else:
                    break
            break

    return count

print(GetNumberOfK([1,2,3,3,3,3,4,5],3))