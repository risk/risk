#include <iostream>
#include <list>
#include <boost/format.hpp>
#include <sys/time.h>

int main()
{
	struct timeval start, end;
	std::list<int> prime;

	gettimeofday(&start, NULL);

	for(int i = 1; i < 10000; ++i) {
		bool divided = false;
		for(int j = 2; j < i; ++j) {
			if( i % j == 0) {
				divided = true;
				break;
			}
		}
		if(!divided) {
			prime.push_back(i);
		}
	}

	gettimeofday(&end, NULL);

	int result = ((end.tv_sec - start.tv_sec) * 1000000 + end.tv_usec) - start.tv_usec;
	std::cout
		<< boost::format("result : %d usec / count %d") % result % prime.size()
		<< std::endl;

	return 0;
}
