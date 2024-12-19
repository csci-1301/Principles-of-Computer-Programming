Level 0: values.

In the journey of programming you will learn many concepts. These may range in complexity from simple to complex, but generally speaking, no matter what you type, you’ll always eventually end up back at a value.


> [!DEFINITION] Value
> Values are representations of data which cannot be simplified further, and belong exclusively to some type

Similar to evolution and its inevitable path to crustaceans, when running code, a lot of what it will do is take more complex bodies of code, and simplify it until all of its limbs are simple values it can operate on.


> [!DEFINITION] Operation
> Operations are computations which cannot be performed on a set number of values of a given type.

Now, these words all sound great, however let’s get into some of the basics you’re going to be seeing a lot of.


> [!example] Values
> ```csharp
> 8 // this is the number 8
> “Hello” // this is the string “Hello”
> True // this is the Boolean value True
> ```

Notice that with each value, we associate a defining group it belongs to. This is its [[Types (Programming)|type]]. For now, trust me when I say that for any value you can define, it belongs to one and only one type.

While is may seem obvious to describe a value by its type, and C# will explicitly make you denote what type things are, you’ll come to find that there’s some room for confusion later on.

Again I’ll ask you to trust me: keeping the types of your values in mind will not only make you the coolest programmer this side of the Mississippi, but it will save you tens and eventually hundreds of hours of debugging and problem solving that can be spent doing better things. Like thinking about types!

Now that’s enough of a tangent, let’s return to today’s meat and potatoes: values and what we can do with them. We’ve defined them, so let’s go over some examples.


> [!Defining terms] Return
> When we say “ *returns* a type, such as returning a Boolean. We can often think of this as if that expression, and later functions, were simplified there in our code.
> In other words, when we say that an expression returns a boolean, we are saying that teh expression, when simplified, becomes a boolean.




> [!example] operating with booleans
> ```csharp
>  true || false // the Boolean “OR” operation, returns true
>  // Reads as: "true OR false"
>  // Think of it as: "Is either value true? Yes, so the result is true"
>
>  true && true // the Boolean “AND” operation, returns true 
>  // Reads as: "true AND true"
>  // Think of it as: "Are both values true? Yes, so the result is true"

These examples use two Booleans. Does a “single input” operation exist for Booleans? Yes: ! (No really, that’s not a typo) (Technically there are two, but more on that in the next chapter)


> [!example] ! : Negation (not)
> When we talk about if someone is lying or maybe they’re wrong, we can say that they said something that’s not true. Similarly in code we write:
> ```Csharp 
> !true // the Boolean "NOT" operation, returns false
> // Reads as: "NOT true"
> // Think of it as: "If we flip true, it becomes false"
> ```


Notice we use these operations to combine different values. Remember how we said before that an operation takes some number of values and some number of types? Well let’s dig into these a bit to see how we might define them with a little more precision:


> [!Definition] || (OR)
> OR takes two Booleans and returns a single Boolean as its result

Notice we don’t say it takes two Boolean values: this is for two reasons:
1. We can generally refer to values as their types if we aren’t using them yet
2. Operations technically take anything which *evaluates* to something of that type.


> [!Definition] Evaluation
> Evaluation refers to the incremental process of simplifying terms until they become values. 

Evaluation, the computation of our code is the heart of how our programs work. Without it we’d be left with a useless bunch of lines that would look like gibberish to most. But what is it that we are evaluating? Well often, it’s an expression, so to speak.


> [!Definition] Expression
> Expressions are a combination of either
> -  operations and values, 
> - or operations and other expressions, 
 >
 >which can be computed until they become a single atomic value. Expressions are usually referred to by the resulting values type; so a *Boolean expression*, like `false || false`, is an expression which will evaluate to become an atomic Boolean value (in this case: false).
 >

Now we’re introducing a lot of definitions, and we notice that a lot of these terms have associated types and behaviors. Let’s define a standard **syntax** for talking about these things. This syntax will be what is known as an *informal type signature*.


> [!example] Type signature
> saying that the operator `OR` takes in two Boolean’s and returns (simplifies to) a Boolean is clunky. Instead we can write this like so:
> $$OR : (Bool, Bool) \rightarrow Bool$$
> while it may not seem much better at first blush, with time, this format will make talking about code much easier. Another example is `NOT`:
> $$NOT: Bool \rightarrow Bool$$

So for a bit of a recap: 

Values are the simplest unit of data we deal with. They hold associated types, which we use to not just describe what kind of data a value is, but also allow us to talk about how we can simplify it. Simplifying is the cornerstone of computation, to the chagrin of most algebra students, and we call combinations of unsimplified operations and terms expressions. And to cap it all off, now we have a new way to represent how all of that looks with a brand new language called a type signature. Is all that clear? It is? Good! Now we can start talking about the real fun stuff: [[booleans]]




## TODO
(NOTE: I should add exercises for them to try here, ideally in the form we would give an understanding quiz the week after this reading was due)
(NOTE: I think in general, having students compute expressions by hand as kind of the algebra of programming would be very helpful. It lets us teach them some Boolean algebra and stuff like modulus as well, which are very needed where is all the precision information for doubles can be mostly tossed)
(NOTE: it may be a good idea to start giving students tables to compute in. Like the top row is the original expression and each row below is empty for them to fill out. Then we play mind games by having extra rows or something. Idk. This is to get them used to the ideas so we can have them track state at different levels. So maybe it would be confusing if the state tables simplify at different rates than the expression tables. But maybe we can signify which line of code the simplification occurs at when we introduce state and how it changes. I like the latest the best)

Type of exercise:
What is the type signature of the following expression:
