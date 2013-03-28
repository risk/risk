// g++ chain.cpp -o chain.bin && ./chain.bin

#include <iostream>
#include <string>

class Responsible
{
public:

	Responsible* next_;

public:

	Responsible()
		: next_(0)
	{
	}


	Responsible& setNext(Responsible* next)
	{
		next_ = next;
		return (*next_);
	}

	virtual void run(int a)
	{
		if(check(a)){
			process(a);
		}
		else if(next_){
			next_->run(a);
		}
	}

	virtual bool check(int a) = 0;
	virtual void process(int a) = 0;


	virtual void clear()
	{
		if(next_){
			next_->clear();
		}
		delete next_;
	}
};

class Fizz
	: public Responsible
{
public:

	virtual bool check(int a)
	{
		return ((a % 3) == 0);
	}

	virtual void process(int a)
	{
		std::cout << "fizz" << std::endl;
	}
};

class Buzz
	: public Responsible
{
public:

	virtual bool check(int a)
	{
		return ((a % 5) == 0);
	}

	virtual void process(int a)
	{
		std::cout << "buzz" << std::endl;
	}
};

class Year
	: public Responsible
{
public:

	virtual bool check(int a)
	{
		return ((a % 7) == 0);
	}

	virtual void process(int a)
	{
		std::cout << "year" << std::endl;
	}
};

class Other
	: public Responsible
{
public:

	virtual bool check(int a)
	{
		return true;
	}

	virtual void process(int a)
	{
		std::cout << a << std::endl;
	}
};

int main()
{
	Fizz entry;
	entry
		.setNext(new Buzz)
		.setNext(new Year)
		.setNext(new Other);

	for(int i = 1; i < 20; ++i) {
		entry.run(i);
	}

	entry.clear();

	return 0;
}
