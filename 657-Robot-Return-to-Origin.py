class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        if moves.count("U") - moves.count("D") == 0 and moves.count("R") - moves.count("L") == 0:
            return True
        else:
            return False