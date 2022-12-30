from collections import deque
T = int(input())

for _ in range(T):
    input() #not used
    cubes = deque(map(int,input().split()))
    ans = "Yes"
   
    while len(cubes) >= 3:
        left, right = cubes.popleft(), cubes.pop()
        if max(left,right) < max(cubes[0],cubes[-1]):
            ans = "No"
            break
    
    print(ans)
    
