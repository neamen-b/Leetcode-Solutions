#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

// Proptypes Arguments. References to vector instead of copies
float findMedian1(vector<int>& num1, vector<int>& num2);
int binarySearch(vector<int>& arr, int target);
void showVector(vector<int>& vec){
    for (int val : vec){
        cout << val << endl;
    }
}
vector<int> merge(vector<int>& vec1, vector<int>& vec2);
float findMedian2(vector<int>& mergedVector);

int main(){
    vector<int> arr = {};
    vector<int> arr2 = {};

    vector<int> merged = merge(arr, arr2);
    showVector(merged);
    cout << findMedian2(merged);
    // cout << binarySearch(arr, 2);
    // cout << "Median value: " << " " << findMedian1(arr, arr2);
    return 0;
}


int binarySearch(vector<int>& arr, int target){
    // Empty vector
    if (arr.size() == 0){
        return 0;
    }
    int start, end, mid;
    start = 0;
    end = arr.size() - 1;
    
    while (start <= end){
        mid = floor((start + end) / 2);

        if (arr[mid] < target){
            start = mid + 1;
        } else if (arr[mid] > target){
            end = mid - 1;
        } else {
            return mid;
        }
    }
    return start;
}

// This acheives, I think at least, the goal but is not O(m + n)
/**
 * Instead this solution is O(length of shorter vector * log(length of longer vector))
 * So either O(n * log(m)) or O(m * log(n))
 * If they are the same size, O(n * log(n))
 */
float findMedian1(vector<int>& num1, vector<int>& num2){
    int lenOfNum1, lenOfNum2;
    lenOfNum1 = num1.size();
    lenOfNum2 = num2.size();

    // No mdeian if both vecotrs are empty
    if (lenOfNum1 + lenOfNum2 == 0){
        return -1;
    }
    vector<int>* ptrToLarger;
    vector<int>* ptrToSmaller;
    float median;

    if (lenOfNum1 > lenOfNum2){
        ptrToLarger = &num1;
        ptrToSmaller = &num2;
    } else {
        ptrToLarger = &num2;
        ptrToSmaller = &num1;
    }

    for (int i = 0; i < ptrToSmaller->size(); i++){
        int insertionIndex;
        insertionIndex = binarySearch(*ptrToLarger, ptrToSmaller->at(i));
        cout << "insertion index " << " " << insertionIndex << " Number from smaller" << " " << ptrToSmaller->at(i) << endl;
        showVector(*ptrToLarger);
        ptrToLarger->insert(ptrToLarger->begin() + insertionIndex, ptrToSmaller->at(i));
        showVector(*ptrToLarger);
        // nlogn
    }

    cout << "Larger after transformation, final : " << endl;
    showVector(*ptrToLarger);
    cout << "Smaller" << endl;
    showVector(*ptrToSmaller);
    
    if ((ptrToLarger->size() % 2) == 0){
        int rightIndex, leftIndex;
        rightIndex = ptrToLarger->size() / 2;
        leftIndex = rightIndex - 1;
        cout << "left index: " << " " << leftIndex << " right index" << " " << rightIndex << endl;
        // cout << (5 + 6) / 2.0 << endl;
        median = (ptrToLarger->at(leftIndex) + ptrToLarger->at(rightIndex)) / 2.0;

    } else{
        median = ptrToLarger->at(floor(ptrToLarger->size() / 2.0));
    }

    return median;
}

// This merge using two pointers
// IT passed
vector<int> merge(vector<int>& vec1, vector<int>& vec2){

    // New merged array
    vector<int> mergedVector;
    int vec1Size, vec2Size;
    vec1Size = vec1.size();
    vec2Size = vec2.size();

    if(vec1Size + vec2Size == 0){
        return vec1;
    }

    vector<int>* shorter;
    vector<int>* longer;

    if(vec1Size > vec2Size){
        longer = &vec1;
        shorter = &vec2;
    } else{
        longer = &vec2;
        shorter = &vec1;
    }

    int indexShorter, indexLonger;
    indexShorter = 0;
    indexLonger = 0;

    while(indexShorter < shorter->size() && indexLonger < longer->size()){
        cout << "shorterindex: " << indexShorter << " " << "longerIndex: " << indexLonger << endl;
        if(shorter->at(indexShorter) <= longer->at(indexLonger)){
            mergedVector.push_back(shorter->at(indexShorter));
            indexShorter++;
        } else{
            mergedVector.push_back(longer->at(indexLonger));
            indexLonger++;
        }
    }

    // Whatever is left can be appended to the end
    cout << "Shorter index is = " << indexShorter << endl;
    mergedVector.insert(mergedVector.end(), longer->begin() + indexLonger, longer->begin() + longer->size());
    mergedVector.insert(mergedVector.end(), shorter->begin() + indexShorter, shorter->begin() + shorter->size());

    return mergedVector;

}

float findMedian2(vector<int>& mergedVector){
    float median;
    if ((mergedVector.size() % 2) == 0){
        int rightIndex, leftIndex;
        rightIndex = mergedVector.size() / 2;
        leftIndex = rightIndex - 1;
        median = (mergedVector.at(leftIndex) + mergedVector.at(rightIndex)) / 2.0;

    } else{
        median = mergedVector.at(floor(mergedVector.size() / 2.0));
    }
    return median;
}