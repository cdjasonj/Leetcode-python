"""
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。

示例 1:

输入: ["flower","flow","flight"]
输出: "fl"
示例 2:

输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。
说明:

所有输入只包含小写字母 a-z 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-common-prefix
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
#最大子串匹配。
# 时间on*m 空间on ,暴力解法
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        _str = ''
        if len(strs)>0:
            min_length = min([len(str) for str in strs])
            for i in range(min_length):
                temp = strs[0][i]
                for str in strs[1:]:
                    if str[i] != temp:
                        return _str
                _str+=temp
            return _str
        else:
            return _str
