class Solution:
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        zeros = []
        begin = 0
        end = 0
        while end < len(seats):
            if seats[begin] != 0:
                begin += 1
                end = begin
            else:
                if seats[end] == 0:
                    end += 1
                else:
                    # if seats[end] == 1
                    zeros.append([begin, end-1])
                    begin = end
        #postprocessing
        if seats[end-1] == 0:
            zeros.append([begin, end-1])
        ##
        print(zeros)
        distance = [(item[1]-item[0])//2 for item in zeros]
        if zeros[0][0] == 0:
            distance[0] = zeros[0][1]-zeros[0][0]
        if zeros[-1][1] == len(seats)-1:
            distance[-1] = zeros[-1][1]-zeros[-1][0]
        return max(distance)
        '''
        # The remaining is to return the index of seat to sit in
        largest = distance.index(max(distance))
        if largest == 0 and zeros[0][0] == 0:
            return 0
        if largest == len(distance)-1 and zeros[-1][1] == len(seats)-1:
            return len(seats)-1
        #not in the beginning or the end
        return zeros[largest][0]+(zeros[largest][1]-zeros[largest][0])//2
        '''