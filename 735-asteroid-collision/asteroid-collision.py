class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack=[]
        for i in asteroids:
            if not stack:
                stack.append(i)
            else:
                if i>0:
                    stack.append(i)
                else:
                    if not stack or stack[-1]<0:
                        stack.append(i)
                    elif abs(stack[-1])==abs(i):
                        stack.pop(-1)
                    else:
                        while stack and (stack[-1]>0 and abs(stack[-1])<abs(i)):
                            stack.pop(-1)
                        if not stack:
                            stack.append(i)
                        elif stack[-1]==-i:
                            stack.pop(-1)
                        elif stack[-1]<0:
                            stack.append(i)
        return stack