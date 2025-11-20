#include <iostream>
#include <vector>
#include <string>
using namespace std;

void showVector(vector<vector<int>> mat){
    int rows, cols;
    rows = mat.size();
    cols = mat[0].size();

    cout << " Showing matrix" << endl;
    for (int i = 0; i < rows ; i++){
        for (int j = 0; j < cols; j++){
            cout << mat[i][j];
        }
    }
}
vector<vector<int>> makeMatrix(string s, int rows){
    int cols, index, diagonal_length;
    vector<vector<int>> matrix;
    index = 0;
    diagonal_length = rows - 2;

    for (int i = 0; i < 5 ; i++){
        for (int j = 0; j < rows; j++){
            cout << "Matrix made" << endl;
            matrix[j][i] = s.at(index);
            index++;
        }
    }
    return matrix;
}
int main(){
    /** Create a matrix and fill it in the zigzag patter
     * number of rows is given, but how do you find the number of columns?
     * Well I know that the number of columns can not exceed the length of the word, and is at least
     * as big as 1, 1 <= numOfCols <= len(string)
     * 
     */ 
    string s;
    int rows;
    s = "PAYPALISHIRING";
    rows = 3;
    cout << "Test" << endl;
    vector<vector<int>> mat;
    mat = makeMatrix(s, rows);
    showVector(mat);

    return 0;
}