#include<bits/stdc++.h>

using namespace std;

void merge_sorted_array(vector<int>&num1,int m,vector<int>&num2,int n){
    int a = m - 1;
    int b = n - 1;
    int k = (m + n) - 1;
    
    while(a>=0){
        if(num1[a]>num2[b]){
            num1[k] = num1[a];
            k--;
            a--;
        }
        else if(num1[a]<num2[b]){
            num1[k] = num2[b];
            k--;
            b--;
        }
    }
    while(k>m){
        num1[k] = num2[b];
        k--;
        b--;
    }
}

int main(){
    vector<int>arr = {1,4,10,0,0,0};
    vector<int>arr2 = {2,5,6};
    merge_sorted_array(arr,3,arr2,3);
    for(int n:arr){
        cout<<n<<endl;
    }
    return 0;
}