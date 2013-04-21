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
IoService global_ioService;

void IoService::serviceThread()
{
	
	ioService_ = boost::make_shared<boost::asio::io_service>();
	work_ = boost::shared_ptr<boost::asio::io_service::work>(
	 	new boost::asio::io_service::work(*ioService_));

	ioService_->run();
}

namespace asio = boost::asio;
using boost::asio::ip::tcp;

class TcpCallback
{
private:

	bool accepted_;
	bool connected_;

public:

	TcpCallback()
		: accepted_(false)
		, connected_(false)
	{
	}

	virtual bool isAccepted()
	{
		return accepted_;
	}
	virtual bool isConnected()
	{
		return connected_;
	}

	virtual void onConnect(const boost::system::error_code& error)
	{
		std::cout << "onConnect" << std::endl;

		if(error)
		{
			std::cout << "connect failed - " << error.message() << std::endl;
		}
		else
		{
			connected_ = true;
			std::cout << "connected" << std::endl;
		}
	}

	virtual void onAccept(const boost::system::error_code& error)
	{
		std::cout << "onAccept" << std::endl;

		if(error)
		{
			std::cout << "accept failed - " << error.message() << std::endl;
		}
		else
		{
			accepted_ = true;
			std::cout << "accepted" << std::endl;
		}
	}
};

typedef boost::shared_ptr<TcpCallback> TcpCallback_ptr;
typedef boost::shared_ptr<tcp::acceptor> Acceptor_ptr;
class TcpSocket
{
private:

	tcp::socket socket_;
	TcpCallback_ptr callback_;
	Acceptor_ptr acceptor_;

	std::string ip_;
	int port_;

public:

	TcpSocket(const int port, TcpCallback_ptr callback = TcpCallback_ptr())
		: socket_(global_ioService.get())
		, callback_(callback)
		, port_(port)
	{
		// コールバックが存在しない場合は、デフォルトを詰めておく
		if(!callback_)
		{
			callback_ = boost::make_shared<TcpCallback>();
		}

		acceptor_ = boost::shared_ptr<tcp::acceptor>(
			new tcp::acceptor(
				global_ioService.get(),
				tcp::endpoint(tcp::v4(), port_)));
	}
	
	TcpSocket(
		const std::string& ip,
		const int port,
		TcpCallback_ptr callback = TcpCallback_ptr())
			: socket_(global_ioService.get())
			, callback_(callback)
			, ip_(ip)
			, port_(port)
	{
		// コールバックが存在しない場合は、デフォルトを詰めておく
		if(!callback_)
		{
			callback_ = boost::make_shared<TcpCallback>();
		}
	}

	virtual bool accept()
	{
		boost::system::error_code error;
		acceptor_->accept(socket_, error);

		if(error)
		{
			std::cout << "accept failed - " << error.message() << std::endl;
			return false;
		}

		// accepted
		return true;
	}

	virtual void acceptAsync()
	{
		acceptor_->async_accept(
			socket_,
			boost::bind(&TcpCallback::onAccept, callback_, asio::placeholders::error));
	}

	virtual bool connect()
	{
		boost::system::error_code error;
		socket_.connect(
			tcp::endpoint(asio::ip::address::from_string(ip_), port_),
			error);
		if(error)
		{
			std::cout << "connect failed - " << error.message() << std::endl;
			return false;
		}
		// connected
		return true;
	}

	virtual void connectAsync()
	{
		socket_.async_connect(
			tcp::endpoint(asio::ip::address::from_string(ip_), port_),
			boost::bind(&TcpCallback::onConnect, callback_, asio::placeholders::error));
	}

};


void serverThread()
{ 
	TcpSocket socket(40000);
	if(socket.accept())
	{
		std::cout << "server thread accepted" << std::endl;
	}
	else
	{
		std::cout << "server thread accept failed" << std::endl;
	}
}

void asyncServerThread()
{
	TcpCallback_ptr callback = boost::make_shared<TcpCallback>();
	TcpSocket socket(40000, callback);
	socket.acceptAsync();

	while(!callback->isAccepted())
	{
		boost::this_thread::sleep(boost::posix_time::milliseconds(100));
	}
}

void clientThread()
{
	TcpSocket socket("127.0.0.1", 40000);
	if(socket.connect())
	{
		std::cout << "client thread connected" << std::endl;
	}
	else
	{
		std::cout << "client thread connect failed" << std::endl;
	}
}

void asyncClientThread()
{ 
	TcpCallback_ptr callback = boost::make_shared<TcpCallback>();
	TcpSocket socket("127.0.0.1", 40000, callback);
	socket.connectAsync();

	while(!callback->isConnected())
	{
		boost::this_thread::sleep(boost::posix_time::milliseconds(100));
	}
}

int main(int argc, char* argv[])
{
	std::cout << "async server start" << std::endl;
//	boost::thread server(boost::bind(serverThread));
	boost::thread server(boost::bind(asyncServerThread));
	std::cout << "async server start OK" << std::endl;

	std::cout << "sleep in" << std::endl;
	boost::this_thread::sleep(boost::posix_time::seconds(1));
	std::cout << "sleep out" << std::endl;

	std::cout << "async client start" << std::endl;
//	boost::thread client(boost::bind(clientThread));
	boost::thread client(boost::bind(asyncClientThread));
	std::cout << "async client start OK" << std::endl;

	client.join();
	server.join();

	return 0;
} 
