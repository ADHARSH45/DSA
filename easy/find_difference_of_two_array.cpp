#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<vector<int>> findDifference(vector<int>& nums1, vector<int>& nums2) {
        unordered_set<int>a(nums1.begin(),nums1.end());
        unordered_set<int>b(nums2.begin(),nums2.end());
        vector<vector<int>>res(2);
        for(int n:a){
            if(b.count(n) == 0){
                res[0].push_back(n);
            }
        }
        for(int k:b){
            if(a.count(k) == 0){
                res[1].push_back(k);
            }
        }
        return res;


    }
};

/*
1. create set for the two arrays to make serch easy.
2. then find set difference between first set and second set and vise versa
*/