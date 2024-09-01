import time
import math
import random
from datetime import datetime

def main():
    numbers = [1, 2, 3, 4, 5]
    squares = [n ** 2 for n in numbers]
    print(squares)

    words = ["ball", "fuck", "nigga"]
    word_lengths = {word: len(word) for word in words}
    print(word_lengths)

    unique_squares = {n ** 2 for n in [1, 2, 2, 3, 4, 5]}
    print(unique_squares)

    add = lambda x, y: x + y
    print(add(2, 4))

    def my_decorator(func):
        def wrapper():
            print("Something is happening before the function is called.")
            func()
            print("Something is happening after the function is called.")
        return wrapper
    
    @my_decorator
    def say_hello():
        print("Hello!!")

    say_hello()

    def shout(text):
        return text.upper()
    
    def whisper(text):
        return text.lower()
    
    print(shout('Hello'))

    def greet(func):
        greeting = func("""Hi, I am created by a function passed as an argument. """)
        print(greeting)

    greet(shout)
    greet(whisper)

    def create_adder(x):
        def adder(y):
            return x + y
        return adder
    
    add_15 = create_adder(15)
    print(add_15(10))


    def hello_decorator(func):
        def inner1():
            print("Hello, this is before function executed")
            func()
            print("This is after functin executed")
        return inner1
    
    @hello_decorator
    def function_to_be_used():
        print("This is inside the fucntion!!")

    function_to_be_used()

    def calculate_time(func):
        def inner1(*args, **kwargs):
            begin = time.time()

            func(*args, **kwargs)

            end = time.time()
            print("Total time taken in : ", func.__name__, end - begin)
        return inner1

    @calculate_time
    def factorial(num):
        time.sleep(2)
        print(math.factorial(num))
    factorial(10)

    def log_execution_time(func):

        def wrapper(*args, **kwargs):
            start_time = datetime.now()
            print(f"Starting function '{func.__name__}' at {start_time}")

            result = func(*args, **kwargs)

            end_time = datetime.now()
            execution_time = (end_time - start_time).total_seconds()
            print(f"Ending function '{func.__name__}' at {end_time}")
            print(f"Function '{func.__name__}' executed in {execution_time:6f} seconds")
            return result
        return wrapper

    @log_execution_time
    def my_task():
        sleep_time = random.uniform(1, 3)
        time.sleep(sleep_time)
        print(f"Task completed after sleeping for {sleep_time:.2f} seconds")

    my_task()
    
if __name__ == "__main__":
    main()

