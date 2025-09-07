#include<bits/stdc++.h>
using namespace std;

int three_sum_closest(vector<int>& nums,int target){

    float min_sum = numeric_limits<float>::infinity();
    sort(nums.begin(),nums.end());

    for(int i=0;i<nums.size()-2;i++){
        int left = i + 1;
        int right = nums.size() - 1;

        while (left<right){
            int current_sum = nums[i] + nums[left] + nums[right];
            if(abs(current_sum - target)<abs(min_sum - target)){
                min_sum = current_sum;
            }
            else if(current_sum >target){
                right -= 1;
            }
            else if (current_sum < target){
                left += 1;
            }
            else{
                 return current_sum;
            }
           
        }
        
    }
    return min_sum;

}

int main(){
    vector<int>nums = {-1,2,1,-4};
    int target = 1;
    cout<<three_sum_closest(nums,target);
    return 0;
}