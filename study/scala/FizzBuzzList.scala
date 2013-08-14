// -*- Coding: utf-8-unix -*-

object FizzBuzzList
{

  def fizzbuzz( n:Int ) = { 
    1 to n
  } map {
    case n if n % 15 == 0 => "FizzBuzz"
    case n if n % 3  == 0 => "Fizz"
    case n if n % 5  == 0 => "Buzz"
    case n                => n.toString 
  } foreach { e => 
    println( e )
  }

  def main( args:Array[String] ):Unit = {
    fizzbuzz(100)
  }
}

