#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ifstream in;
    string value;
    int totalCals = 0;
    vector<int> inputs;

    in.open("input.txt");

    while(!in.fail()) {
        getline(in, value);

        if (value == "") {
            inputs.push_back(totalCals);
            totalCals = 0;
        } else {
            totalCals += stoi(value);
        }
    }

    sort(inputs.rbegin(), inputs.rend());

    cout << "How many total Calories is that Elf carrying? " << inputs.at(0) << endl;
    cout << "How many Calories are those Elves carrying in total? " << inputs.at(0) + inputs.at(1) + inputs.at(2) << endl;

}