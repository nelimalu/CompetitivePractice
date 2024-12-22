#include <iostream>

using namespace std;

int main() {

	int a, b, n;
	cin >> a;
	cin >> b;
	cin >> n;
	
	int max = a;
	int min = b;
	if (b > a) {
		max = b;
		min = a;
	}

	int count = 0;
	for (int i = 1; i <= min / 2; i++) {
		if (count == n)
			break;
		if (min % i == 0 && max % i == 0) {
			cout << i << " ";
			count++;
		}
	}

	if (count < n && max % min == 0)
		cout << min;


	return 0;
}
