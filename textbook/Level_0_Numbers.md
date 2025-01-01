Having explored Boolean algebra, now we shall fall onto an area which is hopefully a bit more familiar: numeric types!

There are two primary types of number we will consider in this course:
1. Whole numbers, what we will be referring to as integers,
2. Floating point numbers, of which we will use the double type.

In this chapter we will cover both, showing how computers handle each, along with the operators we need consider when working with them.

## Integers

Working With number in programming can bring so many questions, depending on what you are trying to represent. Sometimes we want to represent real world things like weights, or currency exchanges. These things are fractional in nature, making integers a poor fit. However, many things in the world can be represented instead by whole numbers. How many chapters are in this book? How many sales did we make this year? How many students got above a B on the last assignment? All of these questions are perfect fits for integers.

More formally, we define an integer in C# as:


> [!Definition] Int
> An Int (Integer) is a whole number which is a value between -2,147,483,648 and 2,147,483,647.

Now you may wonder why this range specifically: it represents of the possible integers you can fit in 32 bits of values, centered around 0. Notice that it includes negative numbers, C# similarly has a 32-bit whole number type which represents the natural numbers, that is, only 0 and positive numbers.


> [!Definition] uint (unsigned Int)
> An unsigned int is a positive whole number which is a value between 0 and 4,294,967,295.

You can look at the comprehensive list of integer types supported in C# here: https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/integral-numeric-types. However we only two we require you to know these two.

### Integer Operations

While you may be very familiar with the operators we’re about to dive through, it’s important to keep in mind that the behavior of these will most likely differ subtly from when we typically work with the real numbers.


> [!Definition] Addition/Subtraction
> Addition and subtraction works as you’d expect, returning the result of adding/subtracting two operands.
> - Symbol: Represented by `+`, and `-` in C# respectively.
> - Behavior: Returns the sum/difference as expected *while* the resul fits within the integer type’s range.
> 	- When the resulting value is *less than* the range permits: *underflow* occurs, meaning the result will wrap around to the maximum value. -2,147,483,648 - 1 will return 2,147,483,647.
> 	- When the resulting value is *greater than* the range permits: *overflow* occurs, meaning the result will wrap around from the maximum to the minimum value. I.e. 2,147,483,647 + 1 will return -2,147,483,648
> - Type Signatures $$Add: (int,int) \rightarrow int$$ $$Subtract: (int,int)\rightarrow int$$

The main change to keep in mind is how underflow and overflow work. More formally, one could say:
	If we define Int.MaxValue as the upper range, 2,147,483,647, and Int.MinValue as the lower end, -2,147,483,648. Then if we overflow by n, the resulting value will be Int.MinValue + n. Conversely, if we *underflow* by n, the resulting value will be Int.MaxValue - n.

Let’s do some exercises to test your understanding:

> [!exercise] Overflow
> TODO


> [!Exercise] Underflow
> TODO

Now let’s move on to Multiplication and Division, which we will split up for reasons you will see.


> [!Definition] Multiplication 
> Integer Multiplication works exactly as you would expect: take the product of two terms. 
> - Symbol: Represented by `*` in C#.
> - Behavior: returns the product of two terms.
> 	- Features the same over/underflow problems as Addition/Subtraction
> - Type Signature: $$Mult:(int,int) \rightarrow int$$

Just to check how you are with over/underflow with multiplication, do the following exercises on your own.

> [!exercise] Overflow
> TODO

> [!Exercise] Underflow
> TODO

This is all pretty close to what you’ll have experienced in any algebra course before. However, let’s talk about something a little different: Division


> [!Definition] Integer Division
> - Symbol: Represented by `/` in C#.
> - Behavior: returns the quotient of two terms while the result is a *whole number*
> 	- When the result would normally be a floating point number, it will cut the decimal off.
> - Type Signature: $$Divide: (int,int) \rightarrow int$$

Let’s explore an example to understand this cutoff thing. If we take the following expression:
`32 / 4 `, this evaluates to `8` like you’d expect. However, this becomes untrue when the numerator is not cleanly divided by its denominator.

Take the following expression: `10 / 3`. In normal algebra over the real numbers, this would return 3.333…, however notice the type signature for integer division: it simplifies to an integer. This means we must have some criteria for picking a value that’s appropriate. Some may think of using a rounding algorithm, such as rounding up if the decimal is equal to or greater than .5, otherwise rounding down. However this can be suboptimal for consistencies sake: therefore we simply drop the decimal point *always*. Therefore with integer division, `10/3` returns `3`.

Run through these exercises to check your understanding:


> [!exercise] Integer Rounding 1
> TODO

> [!exercise] Integer Rounding 2
> TODO

> [!exercise] Integer Rounding 3
> TODO

There is one final operator for division we must cover, commonly called the remainder operator. It serves to find the remainder of dividing two values. A common use for it is taking an integer expression and finding a result which fits within a desired range. We’ll discuss this more later when we cover [[Arrays]].


> [!Definition] Remainder (Modulus, Mod)
> - Symbol: Represented by `%` in C#.
> - Behavior: `x % y` returns the remainder of dividing x by y.
> - Type Signature: $$mod: (int,int) \rightarrow int$$

(NOTE, build a method of doing this with an example using the clock analogy)

## Floating-Point

0.1 + 0.2 != 0.3