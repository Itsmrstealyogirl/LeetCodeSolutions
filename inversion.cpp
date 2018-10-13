long maxInversions(vector<int> prices) {
	long count = 0;

	for (int i = 0; i < prices.size(); i++) {
		long count_left = 0;

		for (int l_index = i-1; l_index >=0; l_index--) {
			if (prices[l_index] >  prices[i])
				count_left++;
		}

		long count_right = 0;
		for (int r_index = i+1; r_index < prices.size(); r_index++) {
			if (prices[r_index] < prices[i])
				count_right++;
		}

		count += (count_left*count_right); 
	}

	return count;
}