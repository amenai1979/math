//
//  primes.cpp
//  testing
//
//  Created by Menai, Alex on 3/16/17.
//  Copyright (c) 2017 Menai, Alex. All rights reserved.
//

#include <stdio.h>
#include <math.h>
using namespace std;

bool is_prime(int n){
    //bool result = false;
    for (int i=n-1; i>1 ; i--){
        //cout << i << "  " << n%i << endl;
        if (n%i==0){
            return false;
            //break;
        }
    }
    return true;
}