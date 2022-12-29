# [프로그래머스] 모음사전

# 현우 says : 문제 읽고나서 전체 탐색이 1초 안에 되는지 생각한다.
# 1초면 보통 10억번의 데이터를 돌리는 시간이다.
# 알파벳이 5개가 중복으로 5번이 최대이니 5*5*5*5*5 는 10억보다 한참 밑이기 때문에 완전탐색으로 하기로 한다.

from itertools import permutations,combinations

vowel = ['A','E','I','O','U']
emptyArr = []
string = ''
index = 0
tempStr = ''
def dfs(depth,string,word):
    global vowel,index,tempStr
    if depth > 5:
        return
    for i in vowel:
        tempStr = (string + i)
        emptyArr.append(tempStr)
        index += 1
        if tempStr == word:
            return
        dfs(depth+1,tempStr,word)
        if tempStr == word:
            return
        
word = "AAAAE"
def solution(word):
    dfs(1,tempStr,word)
    answer = index
    print(answer)
    return answer
solution(word)

#### 현우 C++ 코드 ####
#include <string>
#include <vector>
#include <algorithm>
# using namespace std;
# char alpa[] = {'A', 'E', 'I', 'O', 'U'};
# vector<string>allAlpa;
# void combine(int length, string str) {
#     if(length == str.size()) {
#         allAlpa.push_back(str);
#         return ;
#     }
#     for(int i = 0; i <= 4;i++) {
#         string strNext = str + alpa[i];
#         combine(length, strNext);
#     }
# }
# void init() {
#     for(int i = 1; i <= 5;i++) {
#         string strNew = "";
#         combine(i, strNew);
#     }
# }
# int solution(string word) {
#     int answer = 1;
#     init();
#     sort(allAlpa.begin(), allAlpa.end());
#     for(string s : allAlpa) {
#         if(s == word) {
#             break;
#         }
#         answer++;
#     }
#     return answer;
# }