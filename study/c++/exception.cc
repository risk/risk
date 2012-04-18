// -*- Coding: utf-8-unix -*-
/**
 * @file   exception.cc
 *
 * @author riskrisk
 *
 * g++ -std=c++0x exception.cc -o exception.bin && exception.bin
 */


#include <stdexcept>
#include <iostream>

using namespace std;

void user_unexpected()
{
 	throw;
}

void not_runtime_error_throw() throw( runtime_error, bad_exception )
{
	throw invalid_argument( "throw invalid_argument." );
}

int main()
{
	set_unexpected( user_unexpected );

	// runtime_error以外をthrow
	try {
		not_runtime_error_throw();
	}
	catch( runtime_error& ex ) {
		cout << "caught: " << ex.what() << endl;
	}
	catch( bad_exception ex ) {
		cout << "caught: bad_exception." << endl;
	}

	return 0;
}
