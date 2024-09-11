import math
from collections import deque
a=int(input("Enter Jug A Capacity"))
b=int(input("Enter Jug B Capacity"))
ai=int(input("Initially Water in Jug A"))
bi=int(input("Initially Water in Jug B"))
af=int(input("Final State of Jug A:"))
bf=int(input("Final State of Jug B:"))

if a<=0 or b<=0:
    print("Jug  capacities must be positive")
    exit(1)
if ai<0 or bi<0 or af<0 or bf<0:
    print("Negative values are not allowed.")
    exit(1)
if ai==af and bi==bf:
    print(f"initial state is already the final state: Jug a{ai} and jug B:{bi}")
    exit()
def bfs_wjug(a,b,ai,bi,af,bf):
    visited=set()
    queqe=deque([(ai,bi,[])])
    while queqe:
        curr_ai,curr_bi,operations=queqe.popleft()
        if(curr_ai,curr_bi) in visited:
            continue
        visited.add((curr_ai,curr_bi))

        if curr_ai==af and curr_bi==bf:
            for i,op in enumerate(operations):
                print(f"Step {i+1}:{op}")
            print(f"Final State Reached: Jug A:{curr_ai},Jug B={curr_bi}")
            return
        possible_op=[
            (a,curr_bi,"Fill Jug A"),
            (curr_ai,b,"Fill Jug B"),
            (0,curr_ai,"Empty Jug A"),
            (curr_ai,0,"Empty Jug B"),
            (curr_ai-min(curr_ai,b-curr_bi),curr_bi+min(curr_ai,b-curr_bi),"Pour From A to B"),
            (curr_ai+min(curr_ai,b-curr_bi),curr_bi-min(curr_ai,b-curr_bi),"Pour From B to A"),
            ]
        for next_ai,next_bi,op in possible_op:
            if(next_ai,next_bi) not in visited:
                queqe.append((next_ai,next_bi,operations+[op]))
    print("No solution found.")
    return

gcd=math.gcd(a,b)
if(af<=a and bf<=b) and (af % gcd==bf %gcd==0):
    bfs_wjug(a,b,ai,bi,af,bf)
else:
    print("Final state is not acheivable with the given capacities.")
