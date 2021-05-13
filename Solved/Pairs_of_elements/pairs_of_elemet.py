def input_module():
    N = int(input())
    Q = list(map(int, input().split()))

    return N, Q


def maked(Q):
    count =0
    for i in range(len(Q)):
        for j in range(i+1, len(Q)):
            if ((i+1)**2 + (j+1)**2) == abs(Q[i] - Q[j]):
                count+=1
    return count


def main():
    N, Q = input_module()
    print(maked(Q))


if __name__ == "__main__":
    main()