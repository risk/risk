// コンパイル : g++ templateMethod.cpp -o templateMethod.bin && ./templateMethod.bin

#include <iostream>
#include <string>

class Action
{
public:

	virtual std::string getName() = 0;
	
	virtual void play() = 0;
	virtual void eat() = 0;
	virtual void sleep() = 0;

	virtual void day(Action* target)
	{
		std::cout << target->getName() << "の一日" << std::endl;

		target->play();
		target->eat();
		target->sleep();
		target->play();
		target->eat();
		target->sleep();
		target->play();
		target->eat();
		target->sleep();

		std::cout << "おわり" << std::endl;
	}
};


class RenokunAction
	: public Action
{
public:

	virtual std::string getName()
	{
		return "レノくん";
	}

	virtual void play()
	{
		std::cout << "とうちゃんに絡む" << std::endl;
	}
	virtual void eat()
	{
		std::cout << "キャットフードまじうまい" << std::endl;
	}
	virtual void sleep()
	{
		std::cout << "クッションは俺のもの" << std::endl;
	}
};


class KouchanAction
	: public Action
{
public:

	virtual std::string getName()
	{
		return "こうちゃん";
	}

	virtual void play()
	{
		std::cout << "レノくんを揉む" << std::endl;
	}
	virtual void eat()
	{
		std::cout << "ごはんおいしいですもぐもぐ" << std::endl;
	}
	virtual void sleep()
	{
		std::cout << "布団は聖域である" << std::endl;
	}
};




int main()
{
	RenokunAction renokun;
	KouchanAction kouchan;

	renokun.day(&renokun);
	kouchan.day(&kouchan);

	return 0;
}
