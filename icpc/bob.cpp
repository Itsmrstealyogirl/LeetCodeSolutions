#include <iostream>
#include <vector>

int main() {
    size_t num_of_inputs;
    std::vector<int> moves;
    std::cin>>num_of_inputs;
    while (num_of_inputs) {
        int blocks[num_of_inputs];
        int sum = 0;
        for (size_t i = 0; i < num_of_inputs; i++) {
            std::cin>>blocks[i];
            sum+= blocks[i];
        }
        sum /= num_of_inputs;
        int move = 0;
        for(size_t i = 0; i < num_of_inputs; i++) {
            if (blocks[i] > sum)
                move += (blocks[i] - sum);
        }
        moves.push_back(move);
        std::cin>>num_of_inputs;
    }

    for (size_t i = 1; i <= moves.size(); i++) {
        std::cout<<"Set #"<<i<<std::endl;
        std::cout<<"The minimum number of moves is "<<moves[i-1]<<"."<<std::endl;
        std::cout<<std::endl;
    }
}
