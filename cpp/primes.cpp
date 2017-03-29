//
//  primes.cpp
//  testing
//
//  Created by Menai, Alex on 3/16/17.
//  Copyright (c) 2017 Menai, Alex. All rights reserved.
//

#include <stdio.h>
bool is_prime(int n){
    for (int i=n-1; i>1 ; i--){
        if (n%i==0){
            return false;
        }
    }
    return true;
}