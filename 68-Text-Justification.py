class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        words = words[::-1]
        res = []
        line = []
        cnt = 0
        while words:
            word = words.pop()
            if cnt + len(word) > maxWidth:
                words.append(word)
                #line is full
                cnt -= 1
                extra_blanks = maxWidth - cnt
                if len(line)>1:
                    gap = extra_blanks//(len(line)-1)
                    for i in range(0, len(line)-1):
                        line[i] += ' '*gap
                        extra_blanks -= gap
                    i = 0
                    while extra_blanks:
                        line[i] += ' '
                        i += 1
                        extra_blanks -= 1
                    res.append(' '.join(line))
                    # empty line
                    line = []
                    cnt = 0
                else:
                    res.append(line[0] + ' '*extra_blanks)
                    line = []
                    cnt = 0
            else:
                cnt += len(word)
                line.append(word)
                if cnt == maxWidth-1:
                    if len(line) == 1:
                        res.append(line[0] + ' ')
                        line = []
                        cnt = 0
                    else:
                        line[0] += ' '
                        res.append(' '.join(line))
                        line = []
                        cnt = 0
                elif cnt == maxWidth:
                    res.append(' '.join(line))
                    line = []
                    cnt = 0
                else:
                    cnt += 1
        # very last
        if line:
            word = ' '.join(line)
            res.append(word + ' '*(maxWidth-len(word)))
        return res
        
