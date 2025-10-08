#include <iostream>
#include <map>
#include <tuple>
#include <deque>
#include <list>
#include <string>
using namespace std;
int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    map<char, list<int>> alpha;

    string s;
    cin >> s;

    int i = 0;
    for (auto c : s)
    {
        alpha[c].push_back(i);
        i++;
    }
    int n;
    cin >> n;
    deque<tuple<char, int, int>> questions;
    deque<int> ans;
    for (i = 0; i < n; i++)
    {
        char a;
        int b;
        int c;
        cin >> a >> b >> c;
        questions.push_back({a, b, c});
    }
    for (auto [a, b, c] : questions)
    {
        int cnt = 0;
        for (auto it : alpha[a])
        {
            if (b <= it && it <= c)
            {
                cnt++;
                continue;
            }
        }
        ans.push_back(cnt);
    }
    for (auto answer : ans)
    {
        cout << answer << "\n";
    }
    //     cout << int('A') << '\n';
    //     cout << int('a') << '\n';
}
