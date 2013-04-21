#include <iostream>

#include <boost/shared_ptr.hpp>
#include <boost/make_shared.hpp>
#include <boost/format.hpp>
#include <boost/thread.hpp>
#include <boost/asio.hpp>
#include <boost/bind.hpp>

class IoService
{
private:

	boost::shared_ptr<boost::asio::io_service> ioService_;
	boost::shared_ptr<boost::asio::io_service::work> work_;

	boost::thread th_;
public:

	IoService()
		: th_(boost::bind(&IoService::serviceThread, this))
	{
	}

	~IoService()
	{
		reset();
	}

	virtual void serviceThread();

	boost::asio::io_service& get()
	{
		return *ioService_;
	}

	void reset()
	{
		work_.reset();
		th_.join();
	}
};

void IoService::serviceThread()
{
	
	ioService_ = boost::make_shared<boost::asio::io_service>();
	work_ = boost::shared_ptr<boost::asio::io_service::work>(
	 	new boost::asio::io_service::work(*ioService_));

	ioService_->run();
}

void print()
{
	std::cout << "hello asio world." << std::endl;
}


int main(int argc, char* argv[])
{
	IoService ioService;

	std::cout << boost::format("hello %d") % "world" << std::endl;

	ioService.get().post( print );

	return 0;
} 
