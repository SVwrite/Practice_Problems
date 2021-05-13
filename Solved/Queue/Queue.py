'''Micro just purchased a queue and wants to perform N operations on the queue. The operations are of following type:

 : Enqueue x in the queue and print the new size of the queue.
D : Dequeue from the queue and print the element that is deleted and the new size of the queue separated by space. If there is no element in the queue then print 1 in place of deleted element.

Since Micro is new with queue data structure, he need your help.

Input:
First line consists of a single integer denoting N
Each of the following N lines contain one of the operation as described above.

Output:
For each enqueue operation print the new size of the queue. And for each dequeue operation print two integers, deleted element (1, if queue is empty) and the new size of the queue.'''


def input_module():
    N = int(input())
    Operations  =[]
    while N>0:
        N-=1
        op = input().split()
        
        Operations.append(op)
    return Operations

def decide(operation, Array):
    if operation[0] == 'E':
        Array = enqueue(operation[1], Array)
        return Array
    if operation[0] == 'D':
        Array = dequeue(Array)
        return Array

def enqueue(val, Array):

    Array.append(int(val))
    print(len(Array))
    return Array

def dequeue(Array):
 
    if len(Array) == 0:
  
        print('-1 0')
        return Array
    print(Array.pop(0), end = ' ')
    print(len(Array))
   
    return Array


def main():
    Queue =[]
    Operations = input_module()
    for operation in Operations:
   
        Queue = decide(operation, Queue)

if __name__ == '__main__':
    main()