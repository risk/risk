// -*- Coding: utf-8-unix -*-

object Fibonacci
{
  def main( args:Array[String] ):Unit = {

    def fib[A](l:List[A],prev:Int,now:Int):List[Int] = {
       if( l.isEmpty ) Nil
       else (prev + now) :: fib(l.tail,now, prev + now)
    }

    println( fib( List.range( 0, 10 ), 0 , 1 ) )
  }
}
