import multiprocessing

def merge_sort_parallel(arr):
    if len(arr) <= 1:
        return arr

    # Chia mảng thành hai nửa
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    multiprocessing.current_process().daemon = False


    # Sắp xếp hai nửa mảng bằng các tiến trình con
    with multiprocessing.Pool(processes=2) as pool:
        left_half = pool.apply_async(merge_sort_parallel, (left_half,))
        right_half = pool.apply_async(merge_sort_parallel, (right_half,))

        left_half = left_half.get()
        right_half = right_half.get()

    return merge(left_half, right_half)

def merge(left, right):
    result = []
    left_idx, right_idx = 0, 0

    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1

    result.extend(left[left_idx:])
    result.extend(right[right_idx:])

    return result

if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6, 7]
    sorted_arr = merge_sort_parallel(arr)
    print(sorted_arr)
