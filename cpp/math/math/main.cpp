//
//  main.cpp
//  math
//
//  Created by Menai, Alex on 3/29/17.
//  Copyright (c) 2017 Menai, Alex. All rights reserved.
//

#include <iostream>
#include "permutations.h"
using namespace std;

int main(int argc, const char * argv[]) {
    // insert code here...
    const string input_string="abcdefg";
    vector<string> P;
    P=permute(input_string);
    cout << "expected number of permutations: " << factorial(input_string.size()) << endl;
    for (int i=0; i < P.size(); ++i){
        cout << P[i] << endl;
        
    }
    return 0;
}
