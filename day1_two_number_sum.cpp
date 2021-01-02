#include <bits/stdc++.h>

using namespace std;

void ans(int arr[], int n, int targetSum)
{
    sort(arr, arr + n);
    int l = 0;
    int r = n - 1;

    for (int i = 0; i < n; i++)
    {
        if ((arr[l] + arr[r]) < targetSum)
        {
            l++;
        }
        if (arr[l] + arr[r] > targetSum)
        {
            r++;
        }
    }
    cout << "The two numbers are " << arr[l] << " and " << arr[r] << endl;
}

int main()
{
    int arr[] = {3, 5, -4, 8, 11, 1, -1, 6};
    int targetSum = 10;
    int n = sizeof(arr) / sizeof(arr[0]);
    ans(arr, n, targetSum);
    return 0;
}