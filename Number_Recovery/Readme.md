Link:
https://www.hackerearth.com/practice/data-structures/queues/basics-of-queues/practice-problems/algorithm/number-recovery-0b988eb2/

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
Source Limit: