#include <iostream>

using namespace std;

int possibleAfter(int k, int n, int currentSum, int currentLength, int lastElement) {
	if (currentLength == k - 1) {
		if (currentSum + lastElement <= n)
			return 1;
		else
			return 0;
	}

	int max_possible = (n - currentSum) / (k - currentLength);

	int min_possible;
	if (currentLength == 0)
		min_possible = 1;
	else {
		if (max_possible < lastElement)
			return 0;

		if (currentLength == k - 1)
			min_possible = n - currentSum;
		else
			min_possible = lastElement;
	}

	int possibilities = 0;
	for (int i = min_possible; i <= max_possible; i++)
		possibilities += possibleAfter(k, n, currentSum + i, currentLength + 1, i);

	return possibilities;
}

int main() {
	int n;
	int k;
	cin >> n;
	cin >> k;

	if (n == k || k == 1)
		cout << 1 << endl;
	else
		cout << possibleAfter(k, n, 0, 0, 0) << endl;;

	return 0;
}