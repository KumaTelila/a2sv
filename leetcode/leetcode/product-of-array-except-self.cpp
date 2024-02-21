class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int sz = nums.size();
        int v[sz];
        v[0] = 1;
        for(int i = 1; i<sz; i++){
           v[i] = v[i-1]*nums[i-1];
        }
        int suf = 1;
        for(int i = sz-1; i>=0; i--){
           v[i] = v[i]*suf;
           suf = suf*nums[i];
        }
        vector<int>v1;
        for(auto i: v){
            v1.push_back(i);
        }
        return v1;
        
    }
};