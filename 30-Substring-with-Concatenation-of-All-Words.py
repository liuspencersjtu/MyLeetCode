import collections
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if len(words)==0 or len(s)<len(words)*len(words[0]):
            return []
        res, n, m , word_len = [], len(s), len(words), len(words[0])
        maps = collections.Counter(words)
        
        for i in range(word_len):
            cur_map, count, start, cur = collections.defaultdict(int), 0, i, i
            while cur + word_len <= n:
                cur_str = s[cur:cur+word_len]
                if cur_str in maps:
                    cur_map[cur_str] += 1
                    if cur_map[cur_str] <=maps[cur_str]:
                        count += 1
                    while cur_map[cur_str] > maps[cur_str]:
                        begin_str = s[start:start+word_len]
                        cur_map[begin_str] -= 1
                        start += word_len
                        if cur_map[begin_str] < maps[begin_str]:
                            count -= 1
                    if count == m:
                        res.append(start)
                        begin_str = s[start:start+word_len]
                        cur_map[begin_str] -= 1
                        start+=word_len
                        count-=1
                else:
                    cur_map, count, start = collections.defaultdict(int), 0 ,cur + word_len
                cur += word_len
        return res
#         res, n, m, word_len = [], len(s), len(words), len(words[0])
#         maps = collections.Counter(words)
        
#         for i in range(word_len):
#             cur_map, count, start, cur = {}, 0, i, i
#             while cur + word_len <= n:
#                 cur_str = s[cur:cur+word_len]
#                 if cur_str in maps:
#                     cur_map[cur_str] = cur_map.get(cur_str, 0) + 1     
#                     if cur_map[cur_str] <= maps[cur_str]:
#                         count += 1
#                     while cur_map[cur_str] > maps[cur_str]:
#                         begin_str = s[start:start+word_len]
#                         cur_map[begin_str] -= 1
#                         start += word_len
#                         if cur_map[begin_str] < maps[begin_str]:
#                             count -= 1
#                     if count == m:
#                         res.append(start)
#                         begin_str = s[start:start+word_len]
#                         cur_map[begin_str] -= 1
#                         start += word_len
#                         count -= 1
#                 else:
#                     cur_map, count, start = {}, 0, cur + word_len
#                 cur += word_len
                
#         return res
