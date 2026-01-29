#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <set>
#include <cmath>
#include <iomanip>

using namespace std;

void showVector(vector<string> &words)
{
    for (string &word : words)
    {
        cout << word << endl;
    }
}

void applyDiscount(vector<string> &words, int discount)
{
    set<char> digits = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'};

    for (string &word : words)
    {
        if (word[0] == '$')
        {
            int i = 1;
            bool price = 1;
            while (i < word.size())
            {
                // cout << "Looking at word: " << word << endl;
                if (digits.contains(word[i]) == 0)
                {
                    // cout << "Not a legit price: " << word << " " << word[i] << endl;
                    price = 0;
                    break;
                }
                i++;
            }

            if (price && word.size() > 1)
            {
                string new_price;
                double float_price = stod(word.substr(1, word.size() - 1));
                // cout << "Float price before discount: " << float_price << endl;
                float_price = float_price * (1 - (discount / 100.0));

                // cout << "OG Price: " << word << "Dicounted float price: " << float_price << endl;

                ostringstream oss;
                oss << fixed << setprecision(2) << float_price;
                word = '$' + oss.str();
            }
        }
    }
}
vector<string> splitSentence(string &sentence)
{
    vector<string> words;
    string word;
    stringstream ss(sentence);

    while (ss >> word)
    {
        words.push_back(word);
    }

    // showVector(words);
    return words;
}
string mergeWords(vector<string> words)
{
    string new_sentence;

    for (int i = 0; i < words.size(); i++)
    {
        if (i == words.size() - 1)
        {
            new_sentence += words[i];
        }
        else
        {
            new_sentence += words[i] + " ";
        }
    }

    return new_sentence;
}
string discountPrices(string sentence, int discount)
{
    vector<string> words = splitSentence(sentence);
    applyDiscount(words, discount);
    string new_sentence = mergeWords(words);
    // showVector(words);
    return new_sentence;
}


int main(){
    discountPrices("Ya Bomboclart curry goat cost $100 ? Rahtid gimme $60 dolla worth", 50);
    return 0;
}
