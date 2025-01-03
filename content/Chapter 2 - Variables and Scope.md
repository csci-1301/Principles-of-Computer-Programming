---
title: Ch. 2 - Variables and Scope
draft: false
aliases:
  - variables
  - scope
---

If we were to take the work we've done so far and try to write a program, we couldn't do much with it. See, we've done a lot of work in simplifying values, which don't get me wrong, is important! However, notice even when describing some of the more hands on approaches in evaluating booleans, we ended up in a situation where we had to *label* things. This chapter will dive into this idea of labeling and remembering values, exploring
1. how we *bind* values to a label so that they become *reusable*,
2. whether these bindings are *permanent* or *variable*,
3. and how we define *where* we can use them.

---
## Defining Our Terms

First, we introduce what we call these labeling/bindings: *variables*. 

>[!abstract] Variables
>>[!Definition]
>>A *Variable* is a reserved space in memory used to store a value of some type.
>
>When we want to label a value in programming, we usually create a variable for it. We refer to giving a value to this variable as *binding* or *assigning* the value to it.
>>[!example]
>>```csharp
>> int x = 7; // reads: create an int variable called x, and assign 7 to it.
>>```
>
>Notice that we use the `=` symbol here. In C# `=` is used for *assignment*, where is `==` is used to check for *equality*.

Now you may have noticed that we use the word *variable*. This seemingly implies that the value held can, well, vary. This is true! C#'s variables may be re-assigned/bound by default. To cover cases where this is not desired, the const keyword is used.

>[!example] 
>```csharp
>int x = 7;
>x = 15; // this is valid
>// However...
>const int y = 7;
>y = 0; // this will cause an error
>```

Now you may notice, we now have this idea that a variable's value can change throughout the execution of your program. After line 1, `x == 7` would return `true`, however after line 2 it would return `false`.  This means if I hand you this code and ask: "What value does x have", both 7 and 15 would be valid answers. To handle this, when we talk about code, we need to be specific about where in our program we are referring to. This allows us to talk about our code in different *states*.

>[!abstract] State
>>[!Definition]
>>Program *state* is the set of *bindings* at a given point of execution.
>
>We can refer to the set of variables and their current values as our *bindings*.
>>[!example]
>>Given the following program
>>```csharp
>>int x = 37;
>>int y = 12;
>>bool isBigger = false;
>>
>>isBigger = x <= y;
>>
>>x = 12
>>isBigger = x <= y; 
>>```
>>After line 1 runs, 37 is bound by x.
>>After line 2, 12 is bound by y.
>>Depending on if we check after line 3 or line 8 runs, isBigger will be either false or true respectively.
>>
>>To handle this we introduce using a table to track the program state:
>>
>>
| after line # runs | x   | y   | isBigger |
| ----------------- | --- | --- | -------- |
| 1                 | 37  | dne | dne      |
| 2                 | 37  | 12  | dne      |
| 3                 | 37  | 12  | false    |
| 5                 | 37  | 12  | false    |
| 7                 | 12  | 12  | false    |
| 8                 | 12  | 12  | true     |

This let's us talk about what the data in our program is like at any point, which, now that this can change wildly line per line, seems pretty handy to me. This also let's us do something nice: we can now look at how this data changes to *better understand* what our code is doing. Instead of a bunch of expressions we try to follow, we can also look at how the state of our program changes over time to better understand how it works. This is incredibly useful when debugging code, where we often end up programming behavior wrong, and the only way to see that is to find that our stored values are off!

**EXERCISE: fill out the program state line by line here.**

**EXERCISE: given the following prompt and code, fill out a state table to find where the implementation is wrong.**

Now there may be some question about how this works under the hood. Well, notice that when we define a variable, we must give it a type. This is important: *Programming languages use types not only to define what kind of value something will be, but also how much space it will take*. So when we create a variable, C# first looks at the type, remember an int is a 32bit whole number, right? Well, C# will find a 32-bit chunk of memory and reserve it for your variable. We also need to name it: this name is how C# finds the variable in memory, this is how it determines its *address*.

However, this raises a question: if we are reserving space in memory for these variables, how/when are they ever freed? 

The how: C# uses a complicated piece of software, called a garbage collector, to detect when a variable will not be used again in the program, and will release the reservation of the memory thereafter.

**Example of program with comments denoting when each variable can now be freed**

C# also recognizes that it can be nice to have manual control over this as well, providing tools to allow us to control where a variable will be available explicitly, rather than letting the garbage collector take all the fun from us. It does so using the concept of define *scopes*.

>[!abstract] Scope
>>[!Definition]
>>Program *scope* hold boundaries of code, with a defined *start* and *end*, where any new entries to the programs state are cleared once execution crosses the *end*.
>
>This means that any variable, or other binding, we create within a specific scope is *only* accessible within, and *inaccessible* from the outside.
>>[!example]
>>In C#, we use *curly braces* `{}` to define the bounds of scope.
>>```csharp
>>{
>>int x = 17;
>>x > 1; // this works
>>}
>>
>>{
>>int y = 18
>>y = x; // this doesn't, x doesn't exist outside of the scope it belongs to
>>}
>>```

## Using Variables With Expressions
- remember an expression evaluates to a value!
	- When assigning -> evaluate on the right before storing on the left
	- Must evaluate to the correct type!
- When we use variables, it actually evaluates to… the value it holds!
	- Therefor -> we can use variables in expressions freely!

To understand how we can use variables with expressions, and vice versa, first let's recall our definition of an expression:

>[!Definition]
> An *expression* is a set of values and operators which evaluate to become a single value.

Notice that we say *values and operators*, well it turns out the important part is actually the second half: *which evaluate to a single value*. Well remember: Variables exist to store a single value of some type! What do you think happens when we use a variable in code?

```csharp
int x = 32;

int y = x; // how does this work?
```

When we use a variable in code, the program will substitute the value held there in the code. For our intents, this means that we evaluate the variable and it results in the value stored there.
The order of steps in our code:
1. Create an integer variable x, store 32 in it.
2. Create a variable y
	1. evaluate x (to 32)
	2. store the result in y.

This allows us to do two things:
1. update our definition of an expression to: 
>[!Definition]
>An *expression* is a set of operators and/or entities which combine to evaluate to a single value.

2. and define the behavior of *assignment*/*binding*:
>[!abstract] Assignment
>>[!Definition]
>>Before we *assign* or *bind* a value to a variable, the expression is fully evaluated.
>
>>[!example]
>>This means that in the following statement
>>```csharp
>> int x = 32 + 7
>>```
>>The order of actions performed are:
>>1. create an `int` sized box, called by `x`, in memory
>>2. evaluate `32 + 7` to `39`
>>3. store `39` in `x`
>
> This hopefully makes intuitive sense: An expression isn't a known value, it just evaluates to one. So you must evaluate it before you can store its resulting value.

This seems great! However, a question that may have crossed your mind is: what happens when you try to store an expression of the wrong type in a variable?

Well if you run the following code:
```csharp
int x = "hello";
```

You get an error: 
```csharp
error CS0029: Cannot implicitly convert type 'string' to 'int'
```

Try reading this error and try to understand it from the error alone. When programming, it's incredibly common to lose sight of what an error tells us. Here it tells us precisely what is wrong: It's trying to convert the string to be used in the integer variable. Since this cannot be done, you get an error. 

This is a component of *type safety*, which ensures that we are using values and expressions which fit the types we say we are working with. This is desirable in programming in the same way that when you ask someone for a pen, you don't want them to hand you a loofa. We want our code to work predictably, getting values or objects of the type we expect is paramount.

This is great for talking about how we store values, but what about when we want to use them? Well we can combine these things:

```csharp
// let's represent a rectangle!
int length = 5;
int width = 7;

int rectangle_area = length * width;
```

Remember from our description earlier, line 5 executes in the following order:
1. Create an integer sized and shaped box called by `rectangle_area`.
2. Evaluate length to the int `5`
3. Evaluate width to the int `7`
4. evaluate `7 * 5`
5. store `35` in `rectangle_area`

That's a lot of stuff for one line of code! Notice, when we evaluate expressions that the first step seems to be evaluate all of the variables, and then continue based on the rules of the types. This means that we can update our order of operations for *all* types:

>[!Definition]
> For all expressions of any type, evaluating variables precedes *any other operation*.


---
CONCLUSION SUMMARY PRACTICE PROBLEMS