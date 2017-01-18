# Thompson

    the easiest and efficient way to express "the offers that cannot be refused".

# Requirements

1. Python 3.5+
2. [Virtualenv](https://virtualenv.pypa.io/en/stable/)


# Setup

1. `git clone git@github.com:zalando-incubator/thompson-py-poc.git`
2. `cd` into cloned directory and run `virtualenv --python=python3 .`
3. `source bin/activate`
4. `pip install -r requirements.txt`

# Run tests

* Run `./run-py-test.sh`


# Run standalone interpreter

* Run `./json-rel.sh [FILENAME]`
  * Examples are in `./tests/data/` directory.


# Intentions

1. Editing in GUI forms.   
    * No textual-syntax.
    * and can be nicely integrated with GUIs. _(Helps, Hints,
     Discoverbility, Completions...)_
2. Extensible language.
    * Add new building blocks easily, to provide simplest and
      straightforward to express rules.
    * *Never intended* to expose this tiny language directly to
      business-minded users,
    * ..Should provide extensions in functions and GUIs that more
      nicely fits to their use-cases.
3. Self-contained tiny language that can be compiled into optimized code.
    * Can generate optimized JVM bytecodes,
      * Intended to be compiled more efficiently at runtime.
    * Also, unlike many other general-purpose languages,
       * Another design decisions about performance kept in mind,
         * For example, _Parallelization, Caching, Object-Pooling..._
       
# Semantics overview

```ruby
### This is completely imaginary syntax. (looks like Ruby.)
### But I'm NOT going to implement textual syntax,
### It is just a demonstration of semantics of language constructs.


### Value literals and Variables.
x = 42      # number.
pi = 3.14   # also a number. (no distinguish between floats and integers)
are_you_ok = True   # Boolean.
name = "spameggs"   # String.


### Functions/Macros.
adder = {|x, y| x + y}       # Function literal.
three_i_guess = adder(1, 2)  # Invocation.

## Discount 30% on every item that costs more than 100.
## `simplest_discount_rule` is another function
## that takes two function-values as param.
simplest_discount_rule(
    {|item| item.price > 100},
    {|item| item.price *= 0.7})

### Mapped variables and functions.
## No lists nor maps are natively supported,
## But can be provided as _mapped-functions_.
l = make_me_a_list_pls()   ## returns a `java.util.List`.
append(l, 42)              ## appends a item to list.
## `l` in this context, is a _foreign-value_. (also `append` as well.)
## These _foreign-values/functions_ are act like just a black-box.
## Only can be created, accessed and manipulated with another foreign-functions.
    
    
### Conditionals.
if {x > pi} 
    then {'gt'} 
    else {'nah~'}  # Else-clause is optional.

# There's no `else`-clauses for `when` and `unless`.
when {x > pi}
    then {'gt'}
    
unless {x > pi}
    then {'nah~'}
    
## http://clhs.lisp.se/Body/m_case_.htm    
case {x}
    {1} then {'one'}  # series of (condition, then-clause)-pairs.
    {2} then {'two'}
    else {'too big'}  # Else-clause is optional.
    
## http://clhs.lisp.se/Body/m_cond.htm#cond
cond
    {x > pi} then {'gt'}
    {x < pi} then {'lt'}
    else {'nah~'}  # also, optional.    
    
    
### Arithmetic and Logical operators.
3 + 1
4 - 2
2 * 3    # Simple multiplcation.
2 ** 3   # == 8. Power.
7 / 2    # == 3.5. Float division.
7 rem 2  # == 1. Remainder.
7 // 2   # == 3. Integer division.

true and false  # false, of course.
true or false   # true.
not true        # false.
## also `xor` too.


### Equalities and Comparisons.
x != y
x == y   ## deep equality check. with strs, nums and bools.
         ## shallow, ref-id check only when these are function and foreign.

## comparisions are only for numbers.
x < y
x >= y

## nullity checks
is_null(x)
is_not_null(x)


### Scoping rules and Closures.

const the_ultimate_answer = 42

f = {|r|
    2 * pi * r  # Yes, can access _uplevel_ bindings.
    ## In this case, _uplevel_ is the _root_-binding.
}

magic = 1.000031314

g = {
  two_pi = 2 * pi
  {|r|
    magic + (two_pi * r)   # Yes, access to uplevel binding.
    ## Also, the `magic`, another toplevel binding too.
  }
}

h = {
  two_pi = 2 + pi
  my_fun = g()
  my_fun()  # closure refers `two_pi` as `2 * pi` above, 
  ## ..not `2 + pi` in here.
}

```

..this is almost everything. 
(Another constructs or details would be explained later.)


# And...,

## ..to myself,
1. Write a good Java implementation,
    * Which could be easily embeddable/intergrate-able and optimizable.
    * Eg. Object-poolings to reduce-GCs, Parallelization, and JIT compilation, etc.
   
## ..to people who wants use this language,
1. Design and Write mapped-functions to express business-centric rules.
2. Design and Implement a GUI editor for "rule-writers".

