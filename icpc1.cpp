#include<iostream>
#include<string>
#include<vector>
#include<algorithm>

using namespace std;

int mod;

bool compare(int a, int b) {
    int moda = a % mod;
    int modb = b % mod;

    if (moda == modb) {
        if (a%2 == 0 && b%2 == 0) {
            return a <= b;
        }
        else if (a%2 == 1 && b%2 == 1) {
            return a>=b;
        }
        else {
            return (a%2==1);
        }
    }

    return (moda < modb);
}

void sorticpc(vector<int> values, int m) {
    mod = m;
    cout<<to_string(values.size())<<" "<<to_string(m)<<endl;
    sort(values.begin(), values.end(), compare);
    for (auto elem : values) {
        cout<<to_string(elem)<<endl;
    }
    cout<<"0 0"<<endl;

}

int main() {

}
