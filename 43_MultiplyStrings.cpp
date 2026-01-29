#include <iostream>
#include <string>
#include <vector>

using namespace std;


void reverse_string(string& str){
    int i = 0, j = str.size() - 1;
    char temp;

    while(i < j){
        temp = str[i];
        str[i] = str[j];
        str[j] = temp;
        i++; j--;
    } 
}
string multiplier(char multiplier, string multiplicand, int zero_count)
{
    string ans;
    int prod, carry;
    carry = 0;

    for (int i = multiplicand.size() - 1; i > -1; i--)
    {
        prod = 0;
        prod = (multiplicand[i] - '0') * (multiplier - '0');
        // cout << "Prod after mult: " << prod << endl;
        prod += carry;
        // cout << "Prod after carry added: " << prod << " " << prod % 10 << endl;
        ans += to_string(prod % 10);
        carry = prod / 10;
    }

    if (carry > 0)
    {
        ans += to_string(carry);
    }

    reverse_string(ans);

    // Adding zeros is not necessary. You are adding pairwise with size as the limit
    for (int i = 1; i <= zero_count; i++){
        cout << "Adding zeroes here: " << ans << endl;
        ans += '0';
        cout << "After adding zeroes: " << ans << endl;
    }
    
    return ans;
}

void show_vector(vector<string> vec){
    for (string str : vec){
        cout << str << endl;
    }
}

string add_strings(string str_1, string str_2){
    int i, j, carry, sum;
    string sum_str = "";
    i = str_1.size() - 1;
    j = str_2.size() - 1;
    carry = 0;
    sum = 0;

    while(i >= 0 || j >= 0 || carry > 0){
        sum = 0;

        if( i >=0 ){
            sum += str_1[i] - '0';
            i--;
        }
        if( j >= 0){
            sum += str_2[j] - '0';
            j--;
        }
        sum += carry;
        sum_str += to_string(sum % 10);
        carry = sum / 10;
    }

    reverse_string(sum_str);
    cout << "This is the sum: " << sum_str << endl;
    return sum_str;
}
string mult(string num1, string num2){

    if (num1[0] == '0' || num2[0] == '0'){
        return "0";
    }
    vector<string> prods = {};
    int zero_count = 0;
    // Better to make the multiplier the shorter string/number
    for(int i = num1.size() - 1; i > -1 ; i--){
        prods.push_back(multiplier(num1[i], num2, zero_count));
        zero_count++;
    }

    string total = "";

    for (string str : prods){
        // cout << "Intermediate Total: " << total << endl;
        total = add_strings(total, str);
    }
    // cout << "FInal Total: " << total << endl;
    
    show_vector(prods);

    cout << "Total: " << total << endl;
    return total;
}
int main(){

    mult("33", "11");
    // string prod = multiplier(6, "23");
    // cout << prod << endl;
    return 0;
}
