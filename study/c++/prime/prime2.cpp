#include <iostream>
#include <list>

#include <boost/foreach.hpp>

int main()
{
	
	std::list<int> sosu;
	for(int i = 1; i < 10000; ++i) {
		bool divided = false;
		BOOST_FOREACH(int& s, sosu) {
			if( s != 1 && i % s == 0) {
				divided = true;
			}
		}
		if(!divided) {
			sosu.push_back(i);
		}
	}

	BOOST_FOREACH(int& i, sosu) {
		std::cout << i << std::endl;
	}

	return 0;
}
