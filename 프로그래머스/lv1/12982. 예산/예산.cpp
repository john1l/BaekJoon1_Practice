#include <iostream>
#include <stdio.h>
#include <string>
#include <vector>
#include <algorithm> 
using namespace std;

int solution(vector<int> d, int budget) {

    sort( d.begin() , d.end()) ; 
    int sumv = 0; 
    for( int  i = 0 ; i < d.size() ; ++i ){\
        if ( sumv + d[i] <= budget ) {
            sumv += d[i] ; }
        else {
            return i ;  } 
}
    
}