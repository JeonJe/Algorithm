#include <string>
#include <vector>
#include <algorithm>
using namespace std;

string solution(vector<string> participant, vector<string> completion) {
	vector <string>::iterator it;
	for (int i = 0; i < completion.size(); i++) {
		it = find(participant.begin(), participant.end(), completion.at(i));
		if (it != participant.end()) it = participant.erase(it);
		
	}
	string answer="";

	return participant[0];
}

