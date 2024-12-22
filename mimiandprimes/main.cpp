#include <iostream>

using namespace std;

int gcd(int a, int b) {
    int res = min(a, b);

    while (res > 1) {
        if (a % res == 0 && b % res == 0)
            break;
        res--;
    }
    return res;
}


int factorization(int value, int divisor) {
	int k = value;
	while (k % divisor == 0) {
		k /= divisor;
		if (k == 1)
			return divisor;
	}
	return k;
}


int main() {

	int num_values;
	cin >> num_values;

	int k;
	int inp;
	cin >> k;
	for (int i = 1; i < num_values; i++) {
		cin >> inp;
		k = gcd(k, inp);
	}

	// cout << k << endl;

	int end_value = factorization(k, 2);
	// cout << end_value << endl;
	for (int i = 3; i * i < k; i += 2) {
		end_value = factorization(k, i);
	}

	if (end_value == 1)
		cout << "DNE" << endl;
	else
		cout << end_value << endl;


	return 0;
}



