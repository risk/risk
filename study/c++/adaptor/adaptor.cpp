// コンパイル: g++ adaptor.cpp -o adaptor.bin && ./adaptor.bin

#include <iostream>

class TalkInterface
{
public:

	virtual void say() = 0;
};

class Renokun
{
public:

	void catSay()
	{
		std::cout << "とうちゃん、飯くれよ" << std::endl;
	}
};

class RenokunAdaptor
	: public TalkInterface
	, private Renokun
{ 
public:

	virtual void say()
	{
		catSay();
	}
};

int main()
{
	TalkInterface* interface = new RenokunAdaptor();
	interface->say();
	delete interface;
	return 0;
}

