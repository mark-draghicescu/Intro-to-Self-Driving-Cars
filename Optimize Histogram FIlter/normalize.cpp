#include "headers/normalize.h"
using namespace std;

// OPTIMIZATION: Pass variable by reference
vector< vector<float> > normalize(vector< vector <float> > grid) {

  	// OPTIMIZATION: Avoid declaring and defining 				// intermediate variables that are not needed.
	float total;
	int i, j;
	vector<float> row;
	vector<float> newRow;

  	total = 0.0;

	for (i = 0; i < grid.size(); i++)
	{
		row = grid[i];
		for (j = 0; j < row.size(); j++)
		{
			total += row[j];
		}
	}

	vector< vector<float> > newGrid;

	for (i = 0; i < grid.size(); i++) {
		row = grid[i];
		newRow.clear();
		for (j=0; j < row.size(); j++) {
			float newProb = row[j] / total;
			newRow.push_back(newProb);
		}
		newGrid.push_back(newRow);
	}
	return newGrid;
}
