'''
It’s the day we’ve all been waiting for; Luke and Lorelai are finally getting married! Luke and Lorelai have both arrived at the chapel at the same time (at different entrances), and must get to their respective dressing rooms. American wedding tradition says that it is bad luck for the bride and groom to see each other on the day of their wedding before the ceremony. Lorelai’s daughter, Rory, needs your help as a CS4102 student, in finding the shortest paths for Luke and Lorelai to take ensuring that neither is in the other’s line-of-sight.
You are given a connected undirected graph, with each node representing a room in the chapel, and edges indicating that those rooms are adjacent. Obviously, Luke and Lore- lai can only travel between adjacent rooms and they are within the other’s line-of-sight if and only if they simultaneously occupy the same or adjacent rooms. Give “schedules” of room locations for each of Luke and Lorelai, which together represent the shortest suitable paths.
Your algorithm will read from a file called “chapel.txt”. The first line of this file will contain an integer n representing the number of rooms (vertices) in the chapel (graph). We will refer to each vertex by an integer between 0 and n − 1; i.e., by an index. The next 2 lines will each contain two space-separated integers between 0 and n − 1. The first of the two lines indicates the start and end vertices for Luke, respectively. The second of those two lines indicates the start and end vertices for Lorelai, respectively. The remain- ing n lines will respectively (in order of index) list each vertex’s neighboring vertices as space-separated integers each between 0 and n − 1, collectively giving an adjacency list representation of the graph. An example input is given in Figure 1 below.
Your output will be two space-delineated lists of integers, separated by a line break. The first list will give the schedule for Luke, the second list will give the schedule for Lorelai. A schedule is the sequence of vertices each must take simultaneously so that they do not occupy the same or adjacent vertices at the same time. An example output is given in Figure 2 below.

7
06
24
3
2
13 0245 3
36
5


03566 21234
'''
class Solution(object):
	"""docstring for Solution"""
	def __init__(self):
		self.route={0:[0,3],1:[1,2],2:[1,2,3],3:[0,2,3,4,5],4:[3,4],5:[3,6,5],6:[5,6]}
		
	def search(self):
		queue_man = [[0]]
		queue_woman = [[2]]
		k = 1
		while k<8:
			## BFS for the man:
			## for example, item = [0,3,2] represent 0-3-2
			newqueue_man = []
			newqueue_man_end = []
			for item in queue_man:
				for vertex in self.route[item[-1]]:
					newqueue_man.append(item+[vertex])
					if vertex == 6:
						newqueue_man_end.append(item+[vertex])

			## BFS for the woman:
			newqueue_woman = []
			newqueue_woman_end = []
			for item in queue_woman:
				for vertex in self.route[item[-1]]:
					newqueue_woman.append(item+[vertex])
					if vertex == 4:
						newqueue_woman_end.append(item+[vertex])

			## check if there is a solution:
			for way1 in newqueue_man_end:
				for way2 in newqueue_woman_end:
					## check is there is any collision in way1 and way2
					check = True
					for i in range(len(way1)):
						if way1[i] == way2[i]:
							check = False
							break
						if way1[i] in self.route[way2[i]] or way2[i] in self.route[way1[i]]:
							check = False
							break
					if check:
						return [way1,way2]

			queue_man = newqueue_man
			queue_woman = newqueue_woman

		k+=1
