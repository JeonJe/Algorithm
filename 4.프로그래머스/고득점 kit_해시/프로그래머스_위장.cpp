//https://programmers.co.kr/learn/courses/30/lessons/42578

#include <string>
#include <vector>
#include <map>

using namespace std;

int solution(vector<vector<string>> clothes) {
    int answer = 1;
    map<string,int> hash; //key 는 종류, value 는 몇개인지 
    
    for(int i=0; i<clothes.size();i++){
        hash[clothes[i][1]]++;  // 해당 아이템 종류의 개수 증가
    }
    
    for(auto it=hash.begin(); it!=hash.end(); it++)
       answer = answer * (it->second +1) ;   
    // (A종류 옷 가지수 + 1)*(B종류 옷 가지수 + 1)*(C종류 옷 가지수 + 1) - 1

    return answer-1;
}