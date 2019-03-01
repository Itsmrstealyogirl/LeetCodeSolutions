#include <iostream>
#include <string>
#include <stack>
#include <vector>



using std::string;


static std::stack<string> back;
static std::stack<string> forward;
static std::string current = "http://www.acm.org/";

void run_input(string &input);
std::vector<string> tokenize(string &input);

int main() {
	string input;
	while (std::getline(std::cin, input) == "QUIT") {
		run_input(input);
	}

}


std::vector<string> tokenize(string &input) {
	std::vector<std::string> tokens;
	std::string token;
	std::istringstream sStream(input);
	while (std::getline(sStream, token, " ")) {
		tokens.push_back(token);
	}
	return tokens;
}


void run_input(string &input) {
	std::vector<string> args = tokenize(input);
	if (args[0] == "VISIT") {
		back.push(current);
		current = args[1];
		while (!forward.empty())
			forward.pop();
	}
	else if (args[0] == "BACK") {
		if (back.empty()) {
			std::cout<<"Ignored"<<std::endl;
			return;
		}
		forward.push(current);
		current = back.top();
		back.pop();
		return;
	}
	else if (args[0] == "FORWARD") {
		if (forward.empty()) {
			std::cout<<"Ignored"<<std::endl;
			return;
		}
		back.push(current);
		current = forward.top()
		forward.pop();
		return;
	}
	else {
		std::cout<<"Ignored"<<std::endl;
		return;
	}
}