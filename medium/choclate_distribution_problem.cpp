#include<bits/stdc++.h>

using namespace std;

int cdp(vector<int>nums,int student){
    int left = 0;
    int right = student - 1;
    int min_diff = INT_MAX;
    while(right<nums.size()){
        int min_val;
        if(nums[left]<nums[left + 1] && nums[left]<nums[right]) min_val = nums[left];
        else if(nums[left + 1]<nums[right] && nums[left + 1]< nums[left]) min_val = nums[left +1];
        else min_val = nums[right];
        
        int max_val;
        if(nums[left]>nums[left + 1] && nums[left]>nums[right]) min_val = nums[left];
        else if(nums[left + 1]>nums[right] && nums[left + 1]> nums[left]) min_val = nums[left +1];
        else min_val = nums[right];

        min_diff = min(min_diff,max_val - min_val);
        left++;
        right++;
    }
    return min_diff;
}

int main(){

    cout<<cdp({7, 3, 2, 4, 9, 12, 56},3);
    return 0;
}