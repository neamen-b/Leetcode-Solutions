#include <iostream>
#include <set>

using namespace std;


int longestSubstring(string s);

int main(){
    string testString = "";
    int answer;
    answer = longestSubstring("abcabcbb!");
    cout << answer;
    return 0;
}

int longestSubstring(string s){
    // Create an empty set of strings that will store the letters in the valid window
    set<char> validWindow;
    int start, end, maxLength;
    start = 0;
    end = 0;
    maxLength = 0;

    while(end < s.size()){

        if(validWindow.count(s[end]) == 0){
            validWindow.insert(s[end]);
            end++;
        } else{
            validWindow.erase(s[start]);
            start++;
        }

        if (maxLength < validWindow.size()){
            maxLength = validWindow.size();
        }
    }

    return maxLength;
}