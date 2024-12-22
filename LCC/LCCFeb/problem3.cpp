#include <iostream>

using namespace std;

int move(int x, int y, int value, int last_cookie, int depth, int** grid, int rows, int cols, int limit) {
	if (depth == limit) {
		value += grid[y][x];
		return value;
	}

	int neighbours[] = {-1, -1, -1, -1};

	if (x - 1 >= 0)
		neighbours[0] = grid[y][x - 1];
	if (x + 1 < cols)
		neighbours[1] = grid[y][x + 1];
	if (y - 1 >= 0)
		neighbours[2] = grid[y - 1][x];
	if (y + 1 < rows)
		neighbours[3] = grid[y + 1][x];

	int highest = 0;
	//cout << "AAA" << endl;
	int a;

	if (grid[y][x] > last_cookie) {
		a = move(0, 0, value + grid[y][x], grid[y][x], depth + 1, grid, rows, cols, limit);
		if (a > highest)
			highest = a;
	}

	int movement[4][2] = {
		{-1, 0},
		{1, 0},
		{0, -1},
		{0, 1}
	};

	for (int i = 0; i < 4; i++) {
		if (neighbours[i] >= 0) {
			a = move(x + movement[a][0], y + movement[a][1], value, last_cookie, depth + 1, grid, rows, cols, limit);
			if (a > highest)
				highest = a;
		}
	}

	//cout << "BBB" << endl;


	//cout << highest << endl;
	return highest;
}


int main() {

	int rows, cols, limit;
	cin >> rows;
	cin >> cols;
	cin >> limit;

	int **grid = new int*[rows];

	for (int row = 0; row < rows; row++) {
		grid[row] = new int[cols];
		for (int col = 0; col < cols; col++) {
			cin >> grid[row][col];
		}
	}
	cout << move(0, 0, 0, 0, 0, grid, rows, cols, limit) << endl;

	
	return 0;
}
