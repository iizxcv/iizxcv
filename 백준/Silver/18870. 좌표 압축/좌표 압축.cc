#include <iostream>
#include <vector>
#include <unordered_map>
#include <algorithm>
using namespace std;
int main()
{
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
    sort(cp_arr.begin(), cp_arr.end());
    unordered_map<int, int> umap;
    umap.reserve(n);

    int cnt = 0;
    for (int i = 0; i < cp_arr.size(); i++)
    {
        if (umap.find(cp_arr[i]) == umap.end())
        {
            umap[cp_arr[i]] = cnt;
            cnt++;
        }
    }
    for (int i = 0; i < arr.size(); i++)
    {
        cout << umap[arr[i]] << " ";
    }
}