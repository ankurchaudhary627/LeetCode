class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack=[]
        for i in asteroids:
            if not stack:
                stack.append(i)
            else:
                if i>0: # incoming asteroids is +ve, if top of stack is +ve then no collision, also if top is -ve still no collision
                    stack.append(i)
                else:
                    if stack[-1]<0: # both asteroids are -ve
                        stack.append(i)
                    elif stack[-1]==-i: # equal value asteroids collide
                        stack.pop(-1)
                    else:
                        # Collision is sure here
                        while stack and (stack[-1]>0 and abs(stack[-1])<abs(i)):
                            # keep popping until top element is > incoming asteroid
                            stack.pop(-1)
                        if not stack:
                            stack.append(i)
                        elif stack[-1]==-i:
                            stack.pop(-1)
                        elif stack[-1]<0:
                            stack.append(i)
        return stack