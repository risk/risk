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

	int i = 2;
	while(i <= number_max) {
		int remove = i * 2;
		while(remove <= number_max) {
			numbers[remove] = true;
			remove += i;
		}

		prime.push_back(i);

		do  {
			++i;
		}
		while(numbers[i]);
	}

	gettimeofday(&end, NULL);

	BOOST_FOREACH(const int& p, prime) {
		std::cout << p << ", ";
	}
	std::cout << std::endl;

	int result = ((end.tv_sec - start.tv_sec) * 1000000 + end.tv_usec) - start.tv_usec;
	std::cout
		<< boost::format("result : %d usec / count %d") % result % prime.size()
		<< std::endl;

	return 0;
}
