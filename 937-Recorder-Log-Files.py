class Solution:
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        logs_tr = []
        for item in logs:
            item = item.split()
            logs_tr.append(' '.join(item[1:]+[item[0]]))
        logs_letter = []
        logs_digit = []
        for item in logs_tr:
            if ord(item[0])-ord('a')>=0:
                logs_letter.append(item)
            else:
                logs_digit.append(item)
        logs_letter.sort()
        logs_letter = map(lambda x:x.split(),logs_letter)
        logs_letter = map(lambda x:' '.join([x[-1]]+x[:-1]),logs_letter)
        #for item in logs_letter:
        #    item = item.split()
        logs_digit = map(lambda x:x.split(),logs_digit)
        logs_digit = map(lambda x:' '.join([x[-1]]+x[:-1]),logs_digit)
        return list(logs_letter)+list(logs_digit)
            