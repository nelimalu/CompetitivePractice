#include <iostream>
#include <sort>

using namespace std;

int main() {
	int n = 7; // array size
	int a[] = {4,2,5,3,5,8,3};
	cout << sort(a,a+n);
	
	return 0;
}