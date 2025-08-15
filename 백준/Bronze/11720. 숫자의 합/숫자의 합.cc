#include <iostream>
#include <cstdio>



using namespace std;

int main(){

    int no ;
    scanf("%d", &no);
    if(no > 100){
        return 0;
    }
    string a;
    cin >> a;
    
    int result = 0;
    for(int i = 0; i<no; i++){
        result += a[i] - '0';
    }
    cout << result << "\n";

    return 0;




}
