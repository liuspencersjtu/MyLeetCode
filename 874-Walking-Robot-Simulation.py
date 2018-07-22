class Solution:
    def robotSim(self, commands, obstacles):
        """
        :type commands: List[int]
        :type obstacles: List[List[int]]
        :rtype: int
        """
        EuclideanDis = 0
        location = [0,0]
        direc = 'up'
        directions = ['left', 'up', 'right', 'down']
        #obstacles = set(obstacles)
        obstacleSet = set(map(tuple, obstacles))
        
        for command in commands:
            if command == -2:
                if direc == 'up':
                    direc = 'left'
                elif direc == 'right':
                    direc = 'up'
                elif direc == 'down':
                    direc = 'right'
                else:#direc == 'left'
                    direc = 'down'
            if command == -1:
                if direc == 'left':
                    direc = 'up'
                elif direc == 'up':
                    direc = 'right'
                elif direc == 'right':
                    direc = 'down'
                else:
                    direc = 'left'
            else:
                times = command
                if direc == 'up':
                    while times>0:
                        location[1] += 1
                        if (location[0],location[1]) in obstacleSet:
                            location[1] -= 1
                            break
                        times -= 1
                        EuclideanDis = max(EuclideanDis, location[0]**2+location[1]**2)
                if direc == 'right':
                    while times>0:
                        location[0]+=1
                        if (location[0],location[1]) in obstacleSet:
                            location[0]-=1
                            break
                        times -= 1
                        EuclideanDis = max(EuclideanDis, location[0]**2+location[1]**2)
                if direc == 'down':
                    while times>0:
                        location[1]-=1
                        if (location[0],location[1]) in obstacleSet:
                            location[1] += 1
                            break
                        times -= 1
                        EuclideanDis = max(EuclideanDis, location[0]**2+location[1]**2)
                if direc == 'left':
                    while times>0:
                        location[0]-=1
                        if (location[0],location[1]) in obstacleSet:
                            location[0]+=1
                            break
                        times -= 1
                        EuclideanDis = max(EuclideanDis, location[0]**2+location[1]**2)
        return EuclideanDis