#include <iostream>
#include <cmath>

using namespace std;

bool powerofFour(double num){

    // No logs for zero
    // The number cannot be negative because given a where a >= 0, a^x >= 0
    if (num <= 0) return false;
    double result;

    result = log(num) / log(4.0);

    return (result == (int)result) ? true : false; 
    // if (result)

}
int main(){
    cout << powerofFour(-64) << endl;
    return 0;
}