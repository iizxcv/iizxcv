#include <iostream>
#include <vector>

using namespace std;

int solution(vector<int> bandage, int health, vector<vector<int>> attacks) {
    int answer = 0;
    int HP = health;
    int tick = 1;
    int timeStack = 1;
    vector<vector<int>>::iterator attack_iter = attacks.begin();
    
    while(0 < HP)
    {
        if(attack_iter == attacks.end()) break;
        if(HP <= 0) break;

        if (attack_iter != attacks.end() && tick == (*attack_iter)[0]){
            HP -= (*attack_iter)[1];
            timeStack =0;
            if(HP <= 0) break;
            attack_iter++;
        }
        else if(HP < health){
            HP += bandage[1];
            if (HP > health) HP = health;
            if((timeStack % bandage[0]) == 0)
            {
                timeStack = 0;
                HP += bandage[2];
                if (HP > health) HP = health;
            }
        }
    tick++;
    timeStack++;
    }

    if(HP <= 0) answer = -1;
    else answer = HP;

    return answer;
}