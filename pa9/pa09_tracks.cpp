#include <iostream>

using namespace std;
int main(void) {
	int n;
	cin >> n;
	int arr[10000][2];
	for(int i=0; i<n; i++) {
		int a;
		int b;
		cin >> a >> b;
		arr[i][0] = a;
		arr[i][1] = a+b;
	}
	
	int m = arr[0][0];
	int M = arr[0][1];
	for(int i=0; i<n; i++) {
		if(arr[i][0]<m)
			m = arr[i][0];
		if(arr[i][1]>M)
			M = arr[i][1];
	}
	
	int r = 0;
	for(int i=m; i<M+1; i++) {
		int temp = 0;
		for(int j=0; j<n; j++) {
			if(arr[j][0]<=i && i<arr[j][1])
				temp++;
		}
		if(temp >= r)
			r = temp;
	}
	cout << r;
}
