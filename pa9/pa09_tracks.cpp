#include <iostream>

using namespace std;
int main(void) {
	int n;
	cin >> n;
	// 작업시작시간, 정비 소요시간을 입력 받을 배열 할당 
	// arr 배열에는 작업 시작시각, 작업 끝시각을 저장 
	int arr[10000][2];
	for(int i=0; i<n; i++) {
		int a;
		int b;
		cin >> a >> b;
		arr[i][0] = a; 
		arr[i][1] = a+b;
	}
	// m:작업 시작시각 중 가장 작은 수 
	// M:작업 끝시각 중 가작 큰 수 
	int m = arr[0][0];
	int M = arr[0][1];
	for(int i=0; i<n; i++) {
		if(arr[i][0]<m)
			m = arr[i][0];
		if(arr[i][1]>M)
			M = arr[i][1];
	}
	// r:m 에서 M 까지 반복하면서 그 시각에 작업 중인 건 수를
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
