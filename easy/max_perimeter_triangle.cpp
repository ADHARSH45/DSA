#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    int largestPerimeter(vector<int>& nums) {
        sort(nums.begin(),nums.end());
        
        int n = nums.size() - 1;
        for(int i = n - 2;i>=0;i--){
            if((nums[i] + nums[i + 1])>nums[i + 2]){
                return nums[i] + nums[i + 1] + nums[i + 2];
            }
        }
        return 0;


    }
};

/*
1. sort the input array 
2. check grredly from last so as to find the maximum 
3. whenever a tripplet match return it if noting exits return 0
*/