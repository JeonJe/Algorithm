#include <string>
#include <vector>
#include <iostream>

using namespace std;

int answer;

void dfs(vector<bool>& visited, vector<vector<int>>&dungeons, vector<int>&path, int k){
    if (path.size() >= dungeons.size()){
        int temp = k;
        int cnt = 0;
        for (int i=0; i<path.size(); i++){
            int need = dungeons[path[i]][0];
            int use = dungeons[path[i]][1];
            if (temp >= need && temp >= use){
                temp -= use;
                cnt++;
            }
        }
        answer = max(answer,cnt);
    } 
    
    for (int i=0; i<dungeons.size(); i++){
        if(!visited[i]){
            visited[i] = true;
            path.push_back(i);
            dfs(visited, dungeons, path, k);
            path.pop_back();
            visited[i] = false;
        }
    }
    
    
}

int solution(int k, vector<vector<int>> dungeons) {
    answer = 0;
    int n = dungeons.size();
    vector<bool> visited(n, false);
    
    for (int i = 0; i < n; i++){
        visited.assign(n, false);
        visited[i] = true;
        vector<int> path = {i};
        dfs(visited, dungeons, path,k);
    } 
    
    return answer;
}
