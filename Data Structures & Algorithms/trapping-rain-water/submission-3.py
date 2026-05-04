class Solution:
    def trap(self, height: List[int]) -> int:
        leftmaxx,rightmaxx= [],[]
        max_left,max_right = 0,0
        for i in range(len(height)):
            if height[i]>=max_left:
                leftmaxx.append(max_left)
                max_left = height[i]
            else:
                leftmaxx.append(max_left)
        for i in range(len(height)-1,-1,-1):
            if height[i]>=max_right:
                rightmaxx.append(max_right)
                max_right = height[i]
            else:
                rightmaxx.append(max_right)

        rightmaxx.reverse()

        ans = [max(0,min(leftmaxx[i],rightmaxx[i])-height[i]) for i in range(len(height))]
        print(leftmaxx,rightmaxx,ans)

        return sum(ans)

        

        