#include <iostream>
#include <vector>

using namespace std;

void printArray(vector<int> arr) {
    for (int i : arr) cout << i << " ";
    cout << endl;
}

void bubbleSort(vector<int> arr) {
    cout << "\n--- Bubble Sort ---" << endl;
    int n = arr.size();
    for (int i = 0; i < n-1; i++) {
        for (int j = 0; j < n-i-1; j++) {
            if (arr[j] > arr[j+1]) swap(arr[j], arr[j+1]);
        }
        cout << "Iterasi " << i+1 << ": "; printArray(arr);
    }
}

void selectionSort(vector<int> arr) {
    cout << "\n--- Selection Sort ---" << endl;
    int n = arr.size();
    for (int i = 0; i < n-1; i++) {
        int min_idx = i;
        for (int j = i+1; j < n; j++)
            if (arr[j] < arr[min_idx]) min_idx = j;
        swap(arr[i], arr[min_idx]);
        cout << "Iterasi " << i+1 << ": "; printArray(arr);
    }
}

void insertionSort(vector<int> arr) {
    cout << "\n--- Insertion Sort ---" << endl;
    int n = arr.size();
    for (int i = 1; i < n; i++) {
        int key = arr[i];
        int j = i - 1;
        while (j >= 0 && arr[j] > key) {
            arr[j + 1] = arr[j];
            j--;
        }
        arr[j + 1] = key;
        cout << "Iterasi " << i << ": "; printArray(arr);
    }
}

int main() {
    int n, val;
    cout << "Masukkan jumlah data: "; cin >> n;
    vector<int> data;
    cout << "Masukkan data: ";
    for(int i=0; i<n; i++) {
        cin >> val;
        data.push_back(val);
    }

    bubbleSort(data);
    selectionSort(data);
    insertionSort(data);
system("pause");
    return 0;
}