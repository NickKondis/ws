# Negative Binomial Distributions

## What is a Negative Binomial distribution?

In a series of independent trials, where the probability of success is given by p, a Negative Binomial distribution describes the probability of success after X number of trials.  We can determine this probability by:

$$

\begin{align*} 
p(x) = P(X=x) &= P(r^{th}\ \text{success is on}\ x^{th}\ \text{trial}) \\  
&= \binom{x-1}{r-1}p^{r-1}(1-p)^{(x-1)-(r-1)}\times p \\ 
&= \binom{x-1}{r-1}p^r(1-p)^{x-r}, \quad\text{for}\ x=r, r+1, r+2, \ etc 
\end{align*}

$$

Where *p* is the probability of success of each trial, *x* is the number of attempts, and *r* is the total number of successes necessary for overall success.

```{warning}
Negative Binomial distributions must be independent, that is each success must have the same probability of success, often referred to as "with replacement".
```
```{warning}
*r* must be greater than or equal to 2!
```

Let's look at a couple of examples examples...

1. Choose a random card from a full deck of 52 cards, replacing a shuffling the card after each turn.  What is the probability that you will have chosen exactly three spades by the tenth draw?

The probability *p* of each success is 0.25 (13/52), *x* is the number of terms (in this case ten), and *r* is the number of necessary individual successes (in this case 3).

2. Through a fair sided die 5 times.  What is the probability that you will have thrown at least four even numbers by the fifth role?

The probability *p* of each success is 0.5, *x* is the total number of throws (5), and *r* is the number of necessary individual successes (4).

Note, the mathematics of solving the probabilities is beyond the scope of this page.  It is assumed that you will solve the math using technology (symbolab, R, statistics calculator, etc.)


