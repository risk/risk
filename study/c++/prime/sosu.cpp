#include <iostream>

int main()
{
	for(int i = 1; i < 100; ++i) {
		bool divided = false;
		for(int j = 2; j < i; ++j) {
			if( i % j == 0) {
				divided = true;
			}
		}
		if(!divided) {
			std::cout << i << std::endl;
		}
	}
	return 0;
}
