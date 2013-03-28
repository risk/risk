// イテレーターのサンプル
// コンパイル : g++ iterator.cpp -o iterator.bin && ./iterator.bin
#include <iostream>
#include <vector>
#include <list>

int main()
{
	std::vector<int> intArray;
	std::list<int> intList;

	// 連番をvectorとlistにつっこむ
	for(int i = 0; i < 10; ++i)
	{
		intArray.push_back(i);
		intList.push_back(i);
	}

	// イテレーターを使ってみる(vector)
	for(std::vector<int>::iterator itr = intArray.begin();
		itr != intArray.end();
		++itr)
	{
		std::cout << *itr << std::endl;
	}

	// イテレーターを使ってみる(list)
	for(std::list<int>::iterator itr = intList.begin();
		itr != intList.end();
		++itr)
	{
		std::cout << *itr << std::endl;
	}

	return 0;

}
