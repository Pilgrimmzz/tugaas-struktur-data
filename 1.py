def bubble_sort(arr):
    n = len(arr)
    data = arr.copy()
    print("\n--- Proses Bubble Sort ---")
    for i in range(n):
        for j in range(0, n - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
            print(f"Iterasi [{i+1},{j+1}]: {data}")
    return data

def selection_sort(arr):
    data = arr.copy()
    n = len(data)
    print("\n--- Proses Selection Sort ---")
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if data[j] < data[min_idx]:
                min_idx = j
        data[i], data[min_idx] = data[min_idx], data[i]
        print(f"Iterasi {i+1}: {data}")
    return data

def insertion_sort(arr):
    data = arr.copy()
    print("\n--- Proses Insertion Sort ---")
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        while j >= 0 and key < data[j]:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key
        print(f"Iterasi {i}: {data}")
    return data

# Quick Sort & Merge Sort menggunakan rekursi, 
# kita gunakan list global atau logger untuk tracking iterasi.
def quick_sort(data):
    print("\n--- Proses Quick Sort ---")
    def _quick_sort(items):
        if len(items) <= 1:
            return items
        pivot = items[len(items) // 2]
        left = [x for x in items if x < pivot]
        middle = [x for x in items if x == pivot]
        right = [x for x in items if x > pivot]
        res = _quick_sort(left) + middle + _quick_sort(right)
        print(f"Dividing: {items} -> Result: {res}")
        return res
    return _quick_sort(data)

def merge_sort(data):
    print("\n--- Proses Merge Sort ---")
    def _merge_sort(items):
        if len(items) <= 1:
            return items
        mid = len(items) // 2
        left = _merge_sort(items[:mid])
        right = _merge_sort(items[mid:])
        
        merged = sorted(left + right) # Penyederhanaan visual
        print(f"Merging: {left} + {right} -> {merged}")
        return merged
    return _merge_sort(data)

# Main Program
if __name__ == "__main__":
    n = int(input("Masukkan jumlah data: "))
    raw_input = input(f"Masukkan {n} data (pisahkan dengan spasi): ")
    arr = [int(x) for x in raw_input.split()]

    print("\nData Awal:", arr)
    print("Hasil Akhir Bubble:", bubble_sort(arr))
    print("Hasil Akhir Selection:", selection_sort(arr))
    print("Hasil Akhir Insertion:", insertion_sort(arr))
    print("Hasil Akhir Quick:", quick_sort(arr))
    print("Hasil Akhir Merge:", merge_sort(arr))