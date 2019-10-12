def quick_sort(array):
    def sort(low, high):
        if high <= low:
            return

        mid = partition(low, high)
        sort(low, mid - 1)
        sort(mid, high)

    def partition(low, high):
        pivot = array[(low + high) // 2]

        while low <= high:
            while array[low] < pivot:
                low += 1
            while array[high] > pivot:
                high -= 1
            if low <= high:
                array[low], array[high] = array[high], array[low]
                low += 1
                high -= 1
        return low

    return sort(0, len(array) - 1)

a, b = map(int, input().split(" "))


list1 = list(map(int, input().split(" ")))
list2 = list(map(int, input().split(" ")))

answer = list1 + list2
answer.sort()
# quick_sort(answer) # quicksort 시간초과

for a in answer:
    print(a, end=" ")

# quicksort 시간초과