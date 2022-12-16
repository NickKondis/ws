# Geometric Distribution

## What is a Geometric distribution?

Geometric distribution is the probability of your first success after X number of trials.  The equation for Geometric distribution is given by:

$$

\begin{align} 
p(x) = P(X=x) &= P(\text first success occurring by the x^{th}\ \text{trial}) \notag \\ 
&= P(1^{st}\ (x-1)\ \text{trials are failures &}\ x^{th}\ \text{trial is success}) \notag \\ 
&= (1-p)^{x-1}p, \quad\text{for}\ x = 1, 2, etc 
\end{align}

$$






Suppose that a sequence of independent Bernoulli trials is performed, with p=P("success") for each trial. Define the random variable X to give the number of trial at which the first success occurs. Then X has a geometric distribution with parameter p. The probability mass function of X is given by
p(x)=P(X=x)=P(1st success on xth trial)=P(1st (x−1) trials are failures & xth trial is success)=(1−p)x−1p,for x=1,2,3,…(3.4.1)