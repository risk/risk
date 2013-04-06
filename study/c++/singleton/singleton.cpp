// Compile command: g++ singleton.cpp -o singleton.bin && ./singleton.bin

#include <iostream>

// 普通のやつ
class IntSingleton
{
private:

	static int instance_;

public:

	static int& getInstance()
	{
		return instance_;
	}
};
int IntSingleton::instance_ = 0;

// テンプレート版
template <class T>
class Singleton
{
public:

	static T& getInstance()
	{
		static T instance_;
		return instance_;
	}
};


int main()
{
	// 普通のやつ実験
	{
		int& a = IntSingleton::getInstance();
		++a;
		std::cout << "a(IntSingleton) = " << a << std::endl;
	}

	{
		int& b = IntSingleton::getInstance();
		++b;
		std::cout << "b(IntSingleton) = " << b << std::endl;
	}

	{
		int& c = IntSingleton::getInstance();
		++c;
		std::cout << "c(IntSingleton) = " << c << std::endl;
	}


	// テンプレートのやつ実験
	{
		int& a = Singleton<int>::getInstance();
		++a;
		std::cout << "a(int) = " << a << std::endl;
	}

	{
		short& a = Singleton<short>::getInstance();
		++a;
		std::cout << "a(short) = " << a << std::endl;
	}

	{
		int& b = Singleton<int>::getInstance();
		++b;
		std::cout << "b(int) = " << b << std::endl;
	}

	{
		short& b = Singleton<short>::getInstance();
		++b;
		std::cout << "b(short) = " << b << std::endl;
	}

	{
		int& c = Singleton<int>::getInstance();
		++c;
		std::cout << "c(int) = " << c << std::endl;
	}

	{
		short& c = Singleton<short>::getInstance();
		++c;
		std::cout << "c(short) = " << c << std::endl;
	}

	// 最後に三個とも出してみる
	std::cout << "IntSingleton = " << IntSingleton::getInstance() << std::endl;
	std::cout << "Singleton<int> = " << Singleton<int>::getInstance() << std::endl;
	std::cout << "Singleton<short> = " << Singleton<short>::getInstance() << std::endl;

	return 0;
}
