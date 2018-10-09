#include<iostream>
#include<map>
#include<pair>
#include<vector>

using namespace std;

void bicolorable(vector<pair<int, int>> pairs) {
    map<int, vector<int>> edge_map;
    vector<int> nodes;
    for (auto elem : pairs) {
        if (edge_map.find(elem.first) == edge_map.end()) {
            vector<int> v1; v1.push_back(elem.second);
            edge_map[elem.first] = v1;
            nodes.push_back(elem.first);
        }
        else {
            edge_map[elem.first].push_back(elem.second);
        }

        if (edge_map.find(elem.second) == edge_map.end()) {
            vector<int> v2; v2.push_back(elem.first);
            edge_map[elem.second] = v2;
            nodes.push_back(elem.second);
        }
        else {
            edge_map[elem.second].push_back(elem.first);
        }
    }


    for (auto key : nodes) {
        for (auto connected_node : edge_map[key]) {
            vector<int> v1 = edge_map[key];
            vector<int> v2 = edge_map[connected_node];
            std::sort(v1.begin(), v1.end());
            std::sort(v2.begin(), v2.end());
            std::vector<int> v_intersection;
            std::set_intersection(v1.begin(), v1.end(),
                    v2.begin(), v2.end(), std::back_inserter(v_intersection));
            if (v_intersection.size() > 0) {
                cout<<"NOT BICOLORABLE"<<endl;
                return;
            }
        }
    }

    cout<<"BICOLORABLE"<<endl;
}

