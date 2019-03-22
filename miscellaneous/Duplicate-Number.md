## Question
我们有n+2个数字，他们的取值范围为1-n，其中有两个数字重复了两次，请找出这两个数。## 思路
count sort。一种思路就是用一个长度为N的数组，遍历输入的数字，将对应的数字表示的位置上加一，最后检查数组，输出值为2的数字。
## 优化
我们可以inplace的来解决这个问题，遍历输入，将数字绝对值对应位置的数反转为其相反数，最后遍历输入数组前1-n个位置，如果位置上为正值，则说明反转了两次，即这是我们要找的数。
## Code
```
for i in range(len(nums)):
            nums[abs(nums[i])-1] = - nums[abs(nums[i])-1]
        for i in range(len(nums)):
            if nums[i]>0:
                return i+1
```
