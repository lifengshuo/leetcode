class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if words == []: 
            return []

        word_dict = {}  # words的哈希表
        for word in words:
            word_dict[word] = word_dict.get(word, 0) + 1

        s_len, w_len = len(s), len(words[0])    # w_len表示一个单词的长度
        t_len = w_len * len(words)              # 符合要求的子串的长度
        ans = []

        for begin in range(s_len - t_len + 1):       # 遍历每个子串的起点
            res_dict = word_dict.copy()         
            j = begin + w_len
            while s[j - w_len:j] in res_dict and res_dict[s[j - w_len:j]] > 0: # 以当前i为起点的子字符串有戏 固定i不动j继续往右 
                res_dict[s[j - w_len:j]] -= 1  # 用掉一个words里的单词
                j += w_len
            if sum(res_dict.values()) == 0:   # 刚好用完 就是这个起点
                ans.append(begin)    
        return ans
