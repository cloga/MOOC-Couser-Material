Toy App of Binomial Distribution Histogram
========================================================
author: Cloga Chen
date: Fri Aug 22 11:27:15 2014

What is Binomal Distributtion
========================================================

In probability theory and statistics, the binomial distribution is the discrete probability distribution of the number of successes in a sequence of n independent yes/no experiments, each of which yields success with probability p. 

The above definition is from [Wikipidia](http://en.wikipedia.org/wiki/Binomial_distribution)

How to get Binomal Distributtion in R
========================================================

In R, you can use **rbinom** function to simulate Binomal Distributtion.


```r
rbinom(100, 30, 0.5)
```

```
  [1] 14 17 12 16 16 10 18 17 20 15 15 14 17 15 12 13 20 15 15 13 12 15 15
 [24] 14 20 14 15 12 18 16 14 18 17 12 17 19 14 18 18  9 13 10 15 14 19 16
 [47] 14 12  9 20 16 13 10 11 16 14 13 13 12 16 16 17 17 16 14 17 13 15 10
 [70] 18 15 13 21 18 11 21 19 13 13 15 12 13 15 17 17 18 12 16 16 15 20 15
 [93] 18 15 12 10 15 16 15 13
```

Plot Binomal Distributtion Sample
========================================================


```r
hist(rbinom(100, 30, 0.5))
```

![plot of chunk unnamed-chunk-2](Presentation-figure/unnamed-chunk-2.png) 

Enjoy my toy app
========================================================

Combine pre knowledge, I create a toy app to simulate Binomal Distributtion, you can slide bar to change size and probablity of Binomal Distributtion.

Please enjoy it：[My toy app](http://cloga.shinyapps.io/Binomial_Distribution_Histogram/)
