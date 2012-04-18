// -*- Coding: utf-8-unix -*-
/**
 * @file   neted_exception.cc
 *
 * @author riskrisk
 *
 * g++ -std=c++0x exception.cc -o nested_exception.bin && nested_exception.bin
 */

#include <stdexcept>
#include <iostream>

using namespace std;

class my_exception : public nested_exception
{
};

int main()
{
	try {
		try {
			try {
				throw 1.0; // throw double
			}
			catch( double& d ) {
				cout << "1st caught: " << d << endl;
				throw my_exception();
			}
		}
		catch( my_exception& ex ) {
			cout << "2nd caught: my_exception(nested_exception)." << endl;
			ex.rethrow_nested();
		}
	}
	catch( double& d ) {
		cout << "3rd caught: " << d << endl;
	}

	return 0;
}
