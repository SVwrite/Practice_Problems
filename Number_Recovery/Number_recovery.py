'''
Problem
A positive integer  has been stolen. But luckily,  hints are available, each described by two integers  and , meaning that . The hints are numbered  through . While some of those hints are helpful, some might be just a lie. Therefore, we are going to investigate the number  under different possible scenarios.

Initially, we neither trust nor distrust any hint. That is, each hint may be either true or false. Then, in each of the  stages, we will either:

1 id
Entrust the -th hint (). That is, from now on, the -th hint must be true, unless declared otherwise in the future.
2 id
Distrust the -th hint (). That is, from now on, the -th hint must be false, unless declared otherwise in the future.
3 id
Neutralize the -th hint (). That is, from now on, the -th hint may be either true or false, unless declared otherwise in the future.
After each stage, you should determine the number of possible positive values  and report such values in an increasing order. If there are infinitely many such values, print  instead.

Input

The first line contains two space-separated integers  and .

The -th of the following  lines contains two space-separated integers  and , describing the -th hint. It is guaranteed that no two hints are identical. That is, for every two different , , it is guaranteed that  or .

Then,  lines follow, each containing two integers  and  — the type of an update and the index of an affected hint.

Output

After each stage, print the number of possible values of  (in case there are infinitely many of them, print ). If the number of possible values is finite and non-zero, in the same line, continue to print those values in an increasing order.

Constraints

 for every stage (update).

 for every stage.

In tests worth 74 points in total, .

Note that the expected output feature for custom input is disabled for this contest. 

Sample Input
3 10
3 0
0 3
6 3
1 1
3 1
1 2
3 2
1 3
3 3
1 1
1 2
2 1
1 3
Sample Output
1 3
-1
1 3
-1
2 3 9
-1
1 3
1 3
0
0
Time Limit: 1
Memory Limit: 256
Source Limit:'''

def input_module():
    N, Q = map(int, input().split())
    Hints =[]
    Updates =[]
    for i in range(N):
        Hints.append(list(map(int, input().split())))
        Hints[-1].append(3)
    for i in range(Q):
        Updates.append(list(map(int, input().split())))
    return Hints, Updates, N, Q

def Change(update, Hints):
    #print("Change", Hints," ", update, end=" ")
    Hints[update[1]-1][2] = update[0]
    #print(Hints)
    return Hints
   

def numfinder(Hints):
    #print(Hints, "numfinder")
    nums =[-1]
    num_=[]
    for hint in Hints:
        if hint[2] == 3:
            continue
        
        if hint[2] == 1:
            if -1 in nums:
                nums.remove(-1)
                nums.append(hint[1]+hint[0])
                if hint[0] >= hint[1]:
                    nums.append(hint[0] - hint[1])
                continue
            else:
                val =[]
                val.append(hint[1]+hint[0])
                if hint[0] >= hint[1]:
                    val.append(hint[0]-hint[1])
                for num in nums:
                    if num not in val:
                        nums.remove(num)
            
                continue
        
        
        if hint[2] == 2:
            num_.append(hint)
            
            
    
    for hint in num_:
        if (hint[1]+hint[0]) in nums:
                nums.remove(hint[1]+hint[0])
        if hint[0] >= hint[1] and (hint[0]-hint[1]) in nums:
            nums.remove(hint[0] - hint[1])
    
    nums =list(dict.fromkeys(nums))
    nums.sort()

    if -1 in nums:
        print(-1)
    else:
        print(len(nums), end=" ")
        for i in  range(len(nums)):
            print(nums[i], end=" ")
        print("")

def main():
    Hints, Updates, N, Q = input_module()
    #print(Hints, Updates, N, Q)
    for update in Updates:
        Hints = Change(update, Hints)
        numfinder(Hints)


if __name__=="__main__":
    main()