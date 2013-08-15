#include <iostream>
#include <list>
#include <boost/foreach.hpp>
#include <boost/format.hpp>
#include <sys/time.h>

const int number_max = 10000;

int main()
{
	struct timeval start, end;
	std::list<int> prime;

	gettimeofday(&start, NULL);

	std::vector<bool> numbers(number_max + 1, false);

	for(int i = 1; i < number_max; ++i) {
		if(numbers[i]) {
			continue;
		}

		if(i != 1) {
			for(int remove = i; remove < number_max; remove += i) {
				numbers[remove] = true;
			}
		} 
		prime.push_back(i);
	}

	gettimeofday(&end, NULL);

	BOOST_FOREACH(const int& p, prime) {
		std::cout << p << ", ";
	}
	std::cout << std::endl;

	int result = ((end.tv_sec - start.tv_sec) * 1000000 + end.tv_usec) - start.tv_usec;
	std::cout
		<< boost::format("result : %d usec") % result
		<< std::endl;

	return 0;
}
