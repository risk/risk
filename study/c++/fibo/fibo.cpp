#include <iostream>

int main()
{
	int befor = 1;
	int now = 1;

	while(now < 100)
	{
		std::cout << now  + befor << std::endl;
		int tmp = befor;
		befor = now;
		now = now + tmp;
	}

	return 0;
}
