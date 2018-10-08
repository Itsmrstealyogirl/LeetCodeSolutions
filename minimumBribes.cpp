void funct(vector<int> q) {
    int ind_sum = 0;
    for (int i = 0; i < q.size(); i++) {
        if(q[i]-1 - i >2) {
            std::cout<<"Too chaotic"<<std::endl;
            return;
        if(q[i]-1 > i) {
            ind_sum += (q[i]-1 - i);
            i += q[i]-1 - i
        }
        }
    }
    std::cout<<ind_sum<<endl;
}

void swap(vector<int> &arr, int i, int j) {
    int temp = arr[i];
    arr[i] = arr[j];
    arr[j] = temp;
}

int minSwaps(vector<int> arr) {
    
}
