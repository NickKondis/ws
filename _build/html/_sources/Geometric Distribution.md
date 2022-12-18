# Geometric Distribution

## What is a Geometric distribution?

Geometric distribution is the probability of your first success after X number of trials.  For instance, the probability of getting the first 'heads' after a given number of coin flips.

## Properties of Geometric Distributions

1. Each trial is independent (meaning the outcome of each trial has not effect on the probability of every other trial.
2. The results of each trial have exactly two possible outcomes, typically referred to as *success* and *failure*.
3. Each trial has the same probability (*p*) of success.


The equation for Geometric distribution is given by:

(section-label)=
## Geometric distribution
$$

\begin{align} 
p(x) = P(X=x) &= P(\text first success occurring by the x^{th}\ \text{trial}) \notag \\ 
&= P(1^{st}\ (x-1)\ \text{trials are failures &}\ x^{th}\ \text{trial is success}) \notag \\ 
&= (1-p)^{x-1}p, \quad\text{for}\ x = 1, 2, etc 
\end{align}

$$

Where *p* is the probability of success of each trial, *x* is the number of attempts until the first success.

It is important to note that the term 'geometric' implies an important mathematical property, that the infinite sum of geometric values is given the equation:

(section-label2)=
## Geometric Distribution
$$
\sum\limits_{k=0}^\infty ar^k=a+ar+ar^2+ar^3+\cdots=\dfrac{a}{1-r}=a(1-r)^{-1}
$$


where *r* is the common ratio, the value a term is multiplied by to get to the next term.  For (section-label2, the value of *r* is the same as the probability (*p*).  



```{note}
  The common ratio must be between 1 and -1 (|*r*| < 1).
```
```{note}
Since values of probability (*p*) are necessarily between 0 and 1, the property |*r*| < 1 is necessarily met.
```



Let's look at a couple of examples examples...

```{figure} Heart-Playing-Card-PNG.png
---
height: 200px
name: cards1
---
Card Game 2
```

>Choose a random card from a full deck of 52 cards, replacing a shuffling the card after each turn.  What is the probability that you will draw a "hearts" after 7 trials?

The probability *p* of each success is 0.25 (13/52) and *x* is the number of terms (in this case seven).

```{figure} dice_PNG3.png
---
height: 200px
name: dice
---
Dice Game 2
```

>Throw a fair sided die 8 times.  What is the probability that you will have thrown one even value (on the die)?

The probability *p* of each success is 0.5, *x* is the total number of throws (8).

