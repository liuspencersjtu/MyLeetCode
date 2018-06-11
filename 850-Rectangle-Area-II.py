class Solution:
	def rectangleArea(self, rectangles):
		"""
		:type rectangles: List[List[int]]
		:rtype: int
		"""
		MOD = 1000000007
		xset = set([])
		yset = set([])
		area = 0
		for (x1, y1, x2, y2) in rectangles:
			xset.add(x1)
			xset.add(x2)
			yset.add(y1)
			yset.add(y2)

		xlist = sorted(list(xset))
		ylist = sorted(list(yset))
		# print(xlist)
		# print(ylist)

		area = 0
		for i in range(len(xlist) - 1):
			for j in range(len(ylist) - 1):
				cnt = 0
				for (x1, y1, x2, y2) in rectangles:
					if all([
						xlist[i] >= x1,
						xlist[i + 1] <= x2,
						ylist[j] >= y1,
						ylist[j + 1] <= y2]):
						cnt += 1
						break
				if cnt == 1:
					area += (xlist[i + 1] - xlist[i]) * (ylist[j + 1] - ylist[j])
					area %= MOD
		return area






