#include <iostream>
#include <vector>
#include <unordered_map>
#include <algorithm>
using namespace std;

void solution(std::vector<int> &arr)
{
    std::vector<int> copy_arr = arr;
    sort(copy_arr.begin(), copy_arr.end());
    copy_arr.erase(unique(copy_arr.begin(), copy_arr.end()), copy_arr.end());

    // for (int i = 0; i < arr.size(); i++)
    // {
    // auto it = find(copy_arr.begin(), copy_arr.end(), arr[i]);
    //     if (it != copy_arr.end())
    //     {
    //         arr[i] = int(it - copy_arr.begin());
    //     }
    // }
    for (int i = 0; i < arr.size(); i++)
    {
        int default_val = -1;
        for (int li = 0, ri = copy_arr.size() - 1; li <= ri;)
        {
            int mid = (li + ri) / 2;
            if (copy_arr[mid] < arr[i])
            {
                default_val = max(default_val, mid);
                li = mid + 1;
            }
            else
            {
                ri = mid - 1;
            }
        }
        arr[i] = default_val + 1;
    }
}

int main()
{
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(nullptr);
    std::cout.tie(nullptr);
    int n;
    cin >> n;

    vector<int> arr;
    for (int i = 0; i < n; i++)
    {
        int in;
        cin >> in;
        arr.push_back(in);
    }
    vector<int> cp_arr = arr;

    solution(arr);
    for (auto a : arr)
    {
        cout << a << " ";
    }
}