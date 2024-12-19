It had to happen eventually: one's and zero's are the language spoken by traditional modern computers. All information that we see and use in a computer is encoded and represented as a sequence of them. Not only is this information encoded, but also computation can in general be done at a binary level. This requires a different way of thinking though; in this section we will learn think about binary problems too!

For any type, whether they be whole numbers, decimal values, or even strings of text, there are operations that determine how we can compute with them. We add, subtract, multiply, and divide with numbers. Strings of text can be appended, split, and more. Similarly, Booleans have their own set of operations that work together to create *Boolean Algebra*. The rules and systems of computing with logical boolean values.

First we should define what values fit in the boolean type:


> [!Definition] All Possible Boolean Values
> 1. true
> 2. false

That's it. No really, there aren't any more. In different worlds, we may refer to these values differently. In building circuit, we often refer to these as 1 and 0, sometimes we use shorthand for T and F respectively, but they all represent the same core concept. In this book, since we are using C#, we will use the built in representation `true` and `false`.


Now we need to talk about the key operators for us to compute Boolean expressions with:


> [!Definition] Primary Boolean Operators
> All possible boolean operations can be defined using combination of the three base Boolean operations:
> 1. `NOT`
> 	   - Symbol: Represented with `!` in C#.
> 	   - Behavior: Reverses the truth value of a Boolean; !true becomes false, !false becomes true.
> 	   - Type Signature: $$NOT: Boolean \rightarrow Boolean$$
> 1. `AND`
> 	   - Symbol: Represented by `&&` in C#.
> 	   - Behavior: Returns true only if **BOTH** operands are true. Otherwise it returns false.
> 	   - Type Signature: $$AND: (Boolean, Boolean) \rightarrow Boolean$$
> 1. `OR`
> 	   - Symbol Represented by `||` in C#.
> 	   - Behavior: Returns true if **EITHER** operand is true. Otherwise it returns false.
> 	   - Type Signature: $$OR: (Boolean, Boolean) \rightarrow Boolean$$

(NOTE: These should be split up)
(NOTE: be sure to explain the words input and output and tie that to expressions)
(NOTE: specify the order of operations)

> [!Note] Type Signatures Denote Input -> Output Types, not Behavior
> Notice that both `AND` and `OR` have the same type signature! This may feel unintuitive, but it's important to note that a type signature exists to tell you and the computer what kind of thing(s) go in, and what kind of thing comes out. Not the way the specific value will be decided. That is why we separate the behavior from the type signature above.

Speaking of behavior: it feels a bit unfair that we have this precise way to talk about the types of inputs and outputs of an operator or expression, but we just throw around vague sentences about how they compute. Let's fix that:

For Boolean Expressions, we have this magical thing called a *Truth Table* to describe operator behavior:

| A     | B     | A `&&` B |
| ----- | ----- | -------- |
| false | false | false    |
| false | true  | false    |
| true  | false | false    |
| true  | true  | true     |
We read the columns as follows:

| input value A     | input value B     | result of operator with input value 1 and input value 2 |
| ----------------- | ----------------- | ------------------------------------------------------- |
| First value of A  | First value of B  | result of FirstA `operator` FirstB                      |
| First value of A  | Second value of B | result of FirstA `operator` SecondB                     |
| Second value of A | First value of B  | result of SecondA `operator` FirstB                     |
| Second value of A | Second value of B | result of SecondA `operator` SecondB                    |
Since Booleans consist of only two possible values, we define their behavior by taking every possible combination of inputs, and showing what their output is. This allows us to systematically solve problems with them too! Let's go over the other two truth tables and then let's talk about how we can use them to compute values.

| A     | B     | A \|\| B |
| ----- | ----- | -------- |
| false | false | false    |
| false | true  | true     |
| true  | false | true     |
| true  | true  | true     |
The table for `NOT` is a little different though: `NOT` only takes a single input. Therefore we only need a single input column, also cutting the number of possible output values in half:

| A     | `NOT` A |
| ----- | ------- |
| false | true    |
| true  | false   |

Now that we have precise definitions for how our operations work, let's cover one more important piece before we dive into solving problems: Order of Operations!

In traditional algebra, we have PEMDAS to denote ordering over the many operations. With our current expressions, we will have something a bit different:

> [!Definition] Boolean Algebra Order of Operations
> 1. Parenthesis: Yes that's right, we use parenthesis to choose the order we apply things, just like regular algebra.
> 2. NOT: We consider this our inverse operation, we look at this like multiplying by negative 1, (if I wrote -7 - 8, you intrinsically apply the negative to 7 before continuing, this is the same for NOT in boolean algebra).
> 3. AND: To draw an allegory, AND is effectively boolean multiplication, and as such it will go before the others...
> 4. OR: Similar to AND being multiplication, OR is the equivalent to addition with our logical values. Therefore it follows AND.
> 
> This gives us: Parenthesis before NOT, before AND, before OR. Or PNAO (P*uh*-NOW) for short.
> 

### Solving Boolean Expressions

Say I give you the boolean expression:
>  `true and (false or (true and not true)) or true`

How should you go about solving it?
Let's start by using order of operations to break down the order of terms we're solving:

First, let's group some of the values and start giving them letters to represent what their value is so it's not so hard to look at:
- A = `(true and (false or (true and not true)))`
- B = `true`
Meaning our expression now looks like
- `A or B`

This means that, after we evaluate A, we can use the `OR` table to get our answer.

Let's evaluate A first:
1. A = `(true and (false or (true and not true)))`
2. A = C `and` D
3. C = `true`
4. D = `(false or (true and not true))`

We're one step closer, let's continue on to solve D, once solved we can use the `AND` table to solve for A.

1. D = E `or` F
2. E = `false`
3. F = `(true and not true)`

Again, one step closer, E is already an atomic value so we need not simplify further, however F is next so that we can solve for D, and therefore A.

1. F = G `and` H
2. G = `true`
3. H = `not true`

Now we have a complete operator where all values are simplified and known! H!

Let's plug it into our truth table for `not` so we can solve for H!

| X     | `NOT` X |
| ----- | ------- |
| false | true    |
| true  | false   |
Because the value we are feeding into `NOT` is `true`, we know H = `not true` = `false`.

This means we can rewrite F = G `and` H = `true and false`
which if we check our `AND` table, we will find that `true and false` = `false`. Now we can solve for D, since all terms have been simplified to their atomic values.

D = E `or` F = `false or false`
Which when we consult our truth table for `or` gives us: D = `false`.

We're close to finishing now! Our values that are not simplified are: A. 

A = C `and` D = `true and false`, which again when we look at what `AND` returns when given `true,false` for its inputs, we get `false`.

For our last part, we combine our original terms, now simplified:

answer = A `or` B = `false or true`. Which when we check our `OR` truth table, we see that `false or true` = `true`. Making our final answer:
>  `true and (false or (true and not true)) or true` = `true`

Notice this took a long time. But really once you get used to using the truth tables and ordering expressions using PNAO it's more of a formatting and ordering problem. The table is telling you what values go where.

This is precisely what a computer does as well, this follows the exact order of steps the computer will take when evaluating an expression like this, even down to substituting and solving for smaller expressions until it reaches a value. Later in your degree you may learn about call stacks, which handle this process.


> [!seealso] SHORTCUT
> Notice how in the beginning, our terms, A `or` B was really A `or true`. If we look at the `OR` truth table we see that any time that `true` is present as an input to `OR`, it simplifies to `true`. By practicing and becoming familiar with how these operators work, you too can find shortcuts to solving these problems.
> 
> This is commonly referred to as *short-circuit evaluation*, which C# will do with Boolean expressions when it can.
> 

Now that our primer on boolean expressions has been wrapped up, be sure to do the practice problems *by hand*. Learning happens with practice, which unfortunately can't be short-circuit evaluated.

In our next section we'll talk about a more familiar type system: NUMBERS
### Practice Problems and Examples

(TODO)


## Examples
```csharp
true && false // this simpliefies to false. and is the boolean multiplication
true || false // this simplifies to true. or is the boolean addition
```
