/**
*This file is implenmentary of Python format "useful_algorithm"
*Hope I can collect and get more interesting algorithms.
*/

/**
*This is function to find the maximum of the array and return the value.
*/
double max_array = a[0];
int length_array = a.length;
for (int i=0; i<length_array; i++){
	if (a[i]>max_array){
		max_array = a[i];
	}
}


/**
*Compute the average value of the array and return the value.
*/
double sum = 0.0;
int length_array = a.length;
for (int i=0; i<length_array; i++){
	sum = sum + a[i];
double average = sum / N;

/**
*reverse the elements within an array.
*/

for(int i = 0; i < N/2; i++){
	double temp = a[i];
	a[i] = a[N-1-i];
	a[N-1-i] = temp;
}

/**
*Configure a matrix multiplication a[][] * b[][] = c[][]
*/
int N = a.length;
double [][] c = new double [N][N];

for(int i = 0; i < N; i++){
	for (int j = 0; j < N; j++){
		for (int k = 0; k < N; k++){
			c[i][j] += a[i][k] * b[k][j];
		}
	}
}














