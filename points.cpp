#include <set>
#include <vector>
#include <utility>

using namespace std;

void points(int m, vector<pair> segments) {
    set<int> excluded;
    for (segment : segments) {
        if (excluded.contains(segment.first) && excluded.contains(segment.second))
            ;
        else {
            for (int i = segment.first; i <= segment.second; i++) {
                excluded.insert(i);
            }
        }
    }
    if (m - excluded.size() == 0) {
        cout<<"0"<<endl;
        return;
    }
    cout<<to_string(m - excluded.size())<<endl;
    for (i = 1; i <= m; i++) {
        if (!excluded.contains(i))
            cout<<to_string(i)<< " ";
    }
    cout<<endl;
}
