#Eerie Planet
==========================
###Link : https://www.hackerearth.com/practice/data-structures/queues/basics-of-queues/practice-problems/algorithm/weird-planet-2000a170/

--------------------------
##Status : Unsolved
--------------------------
You own a club on eerie planet. The day on this planet comprises of H hours. You appointed C crew members to handle the huge crowd that you get, being the best club on the planet. Each member of the crew has fixed number of duty hours to work. There can be multiple or no crew members at work at any given hour of the day.
Being on weird planet, the rules of this club cannot be normal. Each member of the crew only allows people who are taller than him to enter the club when he is at work.
Given the schedule of work and heights of the crew members, you have to answer Q queries. Each query specifies the time of entry and height of a person who is visiting the club. You have to answer if the person will be allowed to enter the club or not.

Input:
First line of the input contains 3 integers, . Representing number of hours in a day, number of crew members and number of queries respectively.
Next C lines follow, where each line contains 3 integers, , representing height of the crew member and start and end hour of his/her work schedule. He/she works for hours , both inclusive.
Next Q lines follow, each containing 2 integers, , representing height and time (in hour) of the person trying to enter the club.

Output:
Q lines, each line containing "YES" or "NO", without the quotes, answering if the person will be allowed to enter the club or not.

Constraints:






Sample Input
10 1 5
50 2 6
10 1
10 2
50 5
51 6
100 10
Sample Output
YES
NO
NO
YES
YES
Time Limit: 2
Memory Limit: 256
Source Limit:
Explanation
During the first hour, there is no crew member and hence person is allowed.
During hours 2 and 5, person is not taller than crew member, hence is not allowed to enter.
4th person is taller than the crew member at work and hence person is allowed.
During the 10th hour, there is no crew member and hence person is allowed.