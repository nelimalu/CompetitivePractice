#include <iostream>
using namespace std;


void printArray(int arr[], int size) {
	cout << "ARRAY: ";
	for (int i = 0; i < size; i++) {
		cout << arr[i] << " ";
	}
	cout << endl;
}


int main() {
	int num_top;
	int num_left;
	cin >> num_left;
	cin >> num_top;

	int top[num_top];
	int left[num_left];

	for (int i = 0; i < num_left; i++) {
		cin >> left[i];
	}

	for (int i = 0; i < num_top; i++) {
		cin >> top[i];
	}

	//printArray(top, num_top);
	//printArray(left, num_left);


	int collisions = 0;
	for (int x = 0; x < num_top; x++) {
		if (top[x] == -1)
			continue;

		for (int y = 0; y < num_left; y++) {
			if (left[y] == -1)
				continue;

			if (left[y] - y == top[x] - x) {
				collisions++;
				left[y] = -1;
				break;
			}
		}
	}

	cout << collisions << endl;

	return 0;
}