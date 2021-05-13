#!/usr/bin/bash python3

def input_module():
    H, C, Q = map(int, input().split())
    Crew =[]
    Queries =[]
    for i in range(C):
        a = list(map(int, input().split()))
        Crew.append(a)

    for i in range(Q):
        q = list(map(int, input().split()))
        Queries.append(q)
    
    return Crew, Queries, H

def dutyChart(Crew, H):
    Duty ={}
    for i in range(1,H+1):
        Duty[i] =[]
        for c in Crew:
            if i>= c[1] and i<= c[2]:
                Duty[i].append(c[0])
    return Duty

def entry(q, Duty):
    if len(Duty[q[1]]) == 0 :
        return 'YES'
    elif q[0] > max(Duty[q[1]]):
        return 'YES'
    return 'NO'

def main():
    Crew, Queries, H = input_module()
    Duty = dutyChart(Crew, H)
    print(Duty)
    for q in Queries:
        print(entry(q, Duty))

if __name__ == "__main__":
    main()
