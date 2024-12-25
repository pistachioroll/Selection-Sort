def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        index = i
        x = arr[i]
        minn = arr[i]
        for j in range(i, n):
            if arr[j] <= minn:
                minn = arr[j]
                index2 = j
        arr[index] = minn
        arr[index2] = x



# Пример использования:
my_list = [64, 34, 25, 12, 22, 11, 90, 1, 6, 100]
selection_sort(my_list)
print("Отсортированный список:", my_list)