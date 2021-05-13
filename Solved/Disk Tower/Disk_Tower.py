'''Problem
Your task is to construct a tower in  days by following these conditions:

Every day you are provided with one disk of distinct size.
The disk with larger sizes should be placed at the bottom of the tower.
The disk with smaller sizes should be placed at the top of the tower.
The order in which tower must be constructed is as follows:

You cannot put a new disk on the top of the tower until all the larger disks that are given to you get placed.
Print  lines denoting the disk sizes that can be put on the tower on the  day.

Input format

First line:  denoting the total number of disks that are given to you in the  subsequent days
Second line:  integers in which the  integers denote the size of the disks that are given to you on the  day
Note: All the disk sizes are distinct integers in the range of  .

Output format

Print  lines. In the  line, print the size of disks that can be placed on the top of the tower in descending order of the disk sizes.

If on the  day no disks can be placed, then leave that line empty.'''


def input_module():
    N =int(input())
    A =[]
    for a in input().split():
        A.append(int(a))
        if N in A:
            A, N= printer(A, N)
        else:
            print("")
    

def printer(A, N):
    #print(A, N)
    A.sort(reverse=True)
    k = len(A)
    for i in range(k):
        a =A[0]
        if a==N:
            print(a,end=" ")
            A.remove(a)
            N-=1
    print("")
    return A, N

def main():
    input_module()

if __name__=="__main__":
    main()