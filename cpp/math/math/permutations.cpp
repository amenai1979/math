//
//  permutations.cpp
//  math
//
//  Created by Menai, Alex on 3/29/17.
//  Copyright (c) 2017 Menai, Alex. All rights reserved.
//

#include "permutations.h"
#include <string>
#include <vector>
using namespace std;

//string mylist="abc";
string remove_character(string s, char q){
    string result;
    for (int i=0; i<s.size();i++){
        if(s[i] != q){
            result+=s[i];
        }
    }
    return result;
}


int factorial(int n){
    int f=1;
    for(int i=1;i<=n;i++){
        f*=i;
    }
    return f;
}

vector<string> permute(string inputlist){
    //int number_of_permutations = factorial(mylist.length());
    vector<string> permutations;
    for(int i=0;i < inputlist.size();i++){
        string l = inputlist;
        char e=inputlist[i];
        if(l.size()==1){
            permutations.push_back(l);
        }
        else{
        l=remove_character(l,e);
        vector<string> P;
        P=permute(l);
            for (int i=0;i<P.size();i++){
            permutations.push_back(P[i]+e);
            }
        //return permutations;
        }
    }
    return permutations;
}