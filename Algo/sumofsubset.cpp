#include<iostream>

using namespace std;

int sos(int arr[], int n, int s) {
    if (n==0)
        return (s==0) ? 1 : 0;
    return sos(arr, n-1, s)+sos(arr, n-1, s-arr[n-1]);
}

int main() {

    int arr[]={10,5,15};
    int s=20, n=3;
    if (sos(arr, n, s)) {
        cout << "True";
    }
    else {
        cout << "False";
    }
}