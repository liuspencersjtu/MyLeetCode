class Solution:
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        maillist = set()
        for mail in emails:
            local, domain = mail.split('@')
            local = ''.join(local.split('.'))
            local = local.split('+')[0]
            maillist.add(local+'@'+domain)
        return len(maillist)