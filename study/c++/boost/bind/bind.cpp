#include <iostream>

#include <boost/function.hpp>
#include <boost/bind.hpp>

class Sample
{
public:

	void member1()
	{
		std::cout << "call Sample::member1" << std::endl;
	}
	void member2(int a)
	{
		std::cout << "call Sample::member2 a=" << a << std::endl;
	}
	int member3(int a)
	{
		std::cout << "call Sample::member3 return a=" << a << std::endl;
		return a;
	}

};

void function1()
{
	std::cout << "call Sample::function1" << std::endl;
}

void function2(int a)
{
	std::cout << "call Sample::function2 a=" << a << std::endl;
}

int function3(int a)
{
	std::cout << "call Sample::function3 return a=" << a << std::endl;
	return a;
}


int main()
{
	std::cout << "bind test" << std::endl;

	Sample sample;

	boost::function<void()> m1 =
		boost::bind(&Sample::member1, &sample);
	m1();

	boost::function<void(int)> m2 =
		boost::bind(&Sample::member2, &sample, _1);
	m2(10);

	boost::function<int(int)> m3 =
		boost::bind(&Sample::member3, &sample, _1);
	std::cout << "m3 return : " << m3(10) << std::endl;

	boost::function<void()> f1 =
		boost::bind(function1);
	f1();

	boost::function<void(int)> f2 =
		boost::bind(function2, _1);
	f2(20);

	boost::function<int(int)> f3 =
		boost::bind(function3, _1);
	std::cout << "f3 return : " << f3(20) << std::endl;

	return 0;
}
