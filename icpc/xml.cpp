#include <iostream>
#include <string>
#include <stack>


using std::stack;
using std::string;

class tag 
{
public:
	string name;
	bool type;
}

static stack<string> open_tags;
bool xml_check(string &str);

int main(int argc, char const *argv[])
{
	string input;
	while (getline(std::cin, input) != "")
	{
		if (xml_check(input))
			std::cout<<"valid"<<std::endl;
		else
			std::cout<<"invalid"<<std::endl;
	}
	
	/* code */
	return 0;
}


bool xml_check(string &str) 
{
	bool tag = 0;
	for (int i = 0; i < str.size(); i++) 
	{
		if ((int)str[i] < 32 || (int)str[i] > 127)
			return 0;
		if (str[i] == '>')
			return 0;
		if (str[i] == '<') {
			if (check_valid_tag(str, i))
				continue;
			else
				return 0;
		}

	}
}

bool check_valid_tag(string &str, int &i) 
{
	tag new_tag;
	while (i < str.size()) 
	{
		if (str[i] == '>')
			if (new_tag.name.size() > 0)
				open_tags.push(new_tag);
	}
}