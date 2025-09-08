#include<bits/stdc++.h>

using namespace std;

string longest_commn_prefix(vector<string>s){
    auto min_s = min_element(s.begin(),s.end(),[](const string&a,string&b){
        return a.size()>b.size();
    });
   auto max_s = max_element(s.begin(),s.end(),[](const string&a,string&b){
        return a.size()>b.size();
    });
    cout<<*min_s;
    cout<<*max_s;
}
