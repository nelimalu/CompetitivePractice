def binary_search(arr, target):
    first = 0
    last = len(arr) - 1
    
    while first <= last:
        midpoint = (first + last) // 2
        if arr[midpoint] == target:
            return midpoint
        elif arr[midpoint] < target:
            first = midpoint + 1
        else:
            last = midpoint - 1
    return -1


if __name__ == "__main__":
    N, P = map(int, input().split())
    contestants = [int(input()) for _ in range(N)]
    bet = [int(input()) for _ in range(P)]


    for contestant in bet:
        print(binary_search(contestants, contestant))

    