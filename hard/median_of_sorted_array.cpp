#include<bits/stdc++.h>

using namespace std;

float median_of_sorted_array(vector<int>num1,vector<int>num2){
    vector<int>res;
    int i=0,j=0;
    while(i<num1.size() && j<num2.size()){
        if(num1[i]<num2[j]){
            res.push_back(num1[i]);
        
            i++;
        }
        else if(num1[i]>num2[j]){
            res.push_back(num2[j]);
        
            j++;
        }
    }
    while(i<num1.size()){
       res.push_back(num1[i]);
        i++;
     
    }
    while(j<num2.size()){
        res.push_back(num2[j]);
        j++;
       
    }

    if(res.size() % 2 != 0){
        return res[(0 + res.size()) / 2.0];
    }
    else{
        int mid = (0 + res.size()) / 2;
        return (res[mid-1] + res[mid]) / 2.0;
    }

}

int main(){
    vector<int>n1 = {1,2};
    vector<int>n2 = {3,4};
    cout<<median_of_sorted_array(n1,n2);
    return 0;
}