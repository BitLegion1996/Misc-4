class Solution:
    '''
    Initially, we push a -1 onto the stack to mark the end
    We start with the leftmost bar and keep pushing the current bar's index onto the stack until we get two successive numbers in descending order i.e. until we get heights[i] < heights[i-1]heights[i]<heights[i−1]. 
    Now, we start popping the numbers from the stack until we hit a number stack[j]stack[j] on the stack such that heights\big[stack[j]\big] \leq heights[i]heights[stack[j]]≤heights[i].
    
    '''
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        stack = [-1]
        max_area = float("-inf")
        
        for i in range(len(heights)):
            while stack[-1] != -1 and heights[stack[-1]] >= heights[i]:
                curr_ht = heights[stack.pop()]
                curr_wdth = i - stack[-1] - 1 
                curr_area = curr_ht*curr_wdth
                max_area = max(max_area, curr_area )
            stack.append(i)
            
        while stack[-1] != -1 :
            curr_ht = heights[stack.pop()]
            curr_wdth = len(heights) - stack[-1] - 1 
            curr_area = curr_ht*curr_wdth
            max_area = max(max_area, curr_area )
            
        return max_area
                
