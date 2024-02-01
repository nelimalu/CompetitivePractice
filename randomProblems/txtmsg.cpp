#include <iostream>
#include <string>

using namespace std;


string convert(string input) {

		if (input == "CU")
			return "see you";
		if (":-)" == input)
			return "I'm happy";
		if (":-(" == input)
			return "I'm unhappy";
		if (";-)" == input)
			return "wink";
		if (":-P" == input)
			return "stick out my tongue";
		if ("(~.~)" == input)
			return "sleepy";
		if ("TA" == input)
			return "totally awesome";
		if ("CCC" == input)
			return "Canadian Computing Competition";
		if ("CUZ" == input)
			return "because";
		if ("TY" == input)
			return "thank-you";
		if ("YW" == input)
			return "you're welcome";
		if ("TTYL" == input)
			return "talk to you later";
		
		return input;

}


int main() {
	string input;

	do {
		cin >> input;
		cout << convert(input) << endl;
	} while (input != "TTYL");


	return 0;
}