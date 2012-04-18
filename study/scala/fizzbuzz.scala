// -*- Coding: utf-8-unix -*-

object FizzBuzz
{
  def fizzbuzz( num:Int ):String = {
    
    val fizz: Int => String = { n => if( n % 3 == 0 ) "fizz" else "" }
    val buzz: Int => String = { n => if( n % 5 == 0 ) "buzz" else "" }
    val number: ( Int, String ) => String = { ( n, s ) => if( s.isEmpty ) n.toString else s }

    number( num, fizz( num ) + buzz( num ) )
  }

  def main( args:Array[String] ):Unit = {
    for( i <- 1 to 31 ) println( fizzbuzz( i ) )
  }
}
