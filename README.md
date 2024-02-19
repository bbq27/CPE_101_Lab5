# CPE_101_Lab5

Lab 5
Due: 2/16/24
Motivation
This lab asks that you continue to develop new functions, primarily on lists. Some of these
functions may require that you approach the problem using the fold pattern instead of the more
specific map and filter patterns.
In addition, this lab first introduces two functions that we will define for a class to facilitate
testing. In particular, these functions will allow comparison for equality (to verify, for instance,
that the result of a function matches the expected value) and enable more readable output when a
test fails.
Course Learning Objectives
This lab continues to address the following course learning objectives.
• Create a set of unit tests to verify the expected behavior of a function.
• Operate in a networked computing environment.
• Using the syntax, and with an introductory understanding of the semantics, of a
programming language, create a solution to a problem as a fully functioning and well-
tested program.
• Analyze, informally, the execution of a program of moderate size and complexity based
on a mental model of computation.
Lab Tasks
There are six separate tasks listed below. For all but the first two tasks you are expected to add a
function (or more) to the provided lab5.py file and to add your test cases (unit tests) to the
lab5_tests.py file.
Setup
1. Download the given py files to your computer.
2. Create a Project for Lab5 in PyCharm.
3. Transfer the py files to your PyCharm.
Design Recipe
For each of the following tasks, be sure to follow the design recipe when developing the
function.
• Briefly state the purpose of the function, including input and output.
• Identify the representation of the data to be used in the computation.
• Name and template the function.
• Do computation by hand and write tests.
• Complete the function implementation.
Task 1
In Python, when an object is compared to another value using ==, the default behavior is check if
the two values are actually the same object (this is typically referred to as reference
equality because an object value is really a reference to the object so both operands must refer to
the same object for the check to return True). This default behavior complicates testing functions
that return objects because the value returned is often a newly constructed object.
Fortunately, it is possible to change how an object should be compared to another value. That is
to say, we can define what it means for an object to be considered equal to (or not) another value.
(Now, as an aside, there is much debate about the right way to do this, but our goal here is
simply to provide a useful mechanism to check for equality in our test cases, for which there is
less ambiguity.) This can be done by defining the __eq__ function within a class.
If you define the __eq__ function in a class, then that function will be called when == is used
on an object of that class's type (there is some additional complexity underlying this, but it
is not important for our testing objective). As such, the __eq__ can define what it means for
an object to be equal to some other value (e.g., they may be considered equal only when
each of their attributes is equal).
You will modify the data.py and data_tests.py files.
• Time.__eq__(self, other : Any) -> bool
Modify the definition of the Time class to add the __eq__ function. This function will
take two arguments: self (the target of the call, much like with __init__)
and other (the other operand, of type Any (from the typing module) indicating that this
value may be of any type). The function must return True only when other is of
type Time (i.e., type(other) == Time) and the hour, minute, and second attributes
in self are equal to the corresponding attributes in other.
• Tests
Modify data_tests.py to test that your implementation of __eq__ behaves as expected.
You can do so by using assertEqual to compare two Time objects (or assertNotEqual
to verify a negative test). Consider, carefully, the sorts of tests that you might want/need
to verify that this function behaves properly.
Task 2
When writing functions that return objects (or functions in general) it is not uncommon to make
a mistake. This is why we write tests. Fortunately, when a test fails the testing framework will
print the expected and actual values so that we can compare them to gain some insight into what
the mistake may be. Unfortunately, the default format used when an object is printed is cryptic
and unhelpful.
In a manner similar to defining our own notion of equality, we can define what the string
representation of an object should be by defining the __repr__ function in the class.
As before, modify the data.py and data_tests.py files.
• Time.__repr__(self) -> str
Modify the definition of the Time class to add the __repr__ function. This function will
take one argument: self (the target of the call, much like with __init__). The function
must return a string that represents the object; it is recommended that this string include
the values of the attributes (each can be converted to a string using the str() function
and strings can be combined using the + operator). A common approach is to build a
string that matches the syntax used to create such an object.
• Tests
Modify data_tests.py to test that your implementation of __repr__ behaves as
expected.
Task 3
time_add
Define a function named time_add that takes two parameters each of type Time. This function
must return a newly created Time object that represents the sum of the two input times, but such
that the number of seconds and minutes remain in the range 0-59. (no need to check range for
hour)
Your solution must include at least two unit tests.
Task 4
is_descending
Define a function named is_descending that takes a single parameter of type list[float] and
that returns True if and only if the elements within the list are in strictly descending order (i.e,
each element, but the first, is less than the previous).
Your solution must include at least two unit tests.
Task 5
largest_between
Define a function named largest_between that takes three parameters: the first is of type
list[int] (a list of numbers), the second (lower) and third (upper) are both of type int and are
intended to represent two indexes. This function must return the index of the largest value in the
input list that appears between the two provided indexes. More specifically, the function must
examine the values at indexes from lower (inclusive; i.e., the value at index lower will be
considered as long as it is <= upper) to upper (inclusive; i.e., the value at index upper will be
considered as long as it is >= lower) to find the largest value.
Potential issues: If lower > upper, then the range of indexes to consider is empty. Your function
should return None in this case (as such, what should the function's return type be?). The function
must still return a value when either lower or upper is out of bounds (despite Python's support for
them, negative indexes will be considered out of bounds); you can decide what the function will
return in this case (perhaps None or the largest value after adjusting the indexes to the smallest or
largest valid index, as appropriate). Document your decision and be sure to test this behavior.
Your solution must include at least two unit tests.
Task 6
furthest_from_origin
Define a function named furthest_from_origin that takes a single parameter of type
list[Point] (the Point class is included in the provided files) and that returns the index of the
point furthest from the origin (the point at 0,0). If the list is empty, then the function returns
None.
Consider how you might use the previous function to implement this function.
Your solution must include at least two unit tests.
