#include <iostream>
#include <cstdio>


using namespace std;

int main(){
    pair<int,char> p;
    scanf("%d", &p.first);
    int lot = p.first;

    // printf("%d",lot);
    if(lot == 1)
        return 0;
    int mod_no =2;
    for(int i = mod_no; i < lot;){
        if((lot % i) == 0){
            lot /= i;
            printf("%d\n",i);

        }
        else{i++;}
    }
    printf("%d\n",lot);
    return 0;
}