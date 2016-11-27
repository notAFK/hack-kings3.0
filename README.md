## Inspiration
Social media is one the most important drivers of the current world and research has shown that what people do and how they behave on social media can and has been used as a good indicator of the trends in an economy.

## What it does
Using sentiment analysis on tweets collected out of customer-driven companies we output a graph showing the trend of the company, share price over time axis.  

## How we built it
We built a recurrent neural network that looks at tweets over a certain time period in the past with the objective of predicting the trend of the share price in the present.

## Challenges we ran into
Twitter API is restrictive with their API usage but for the purpose of a demo we think we are within reasonable boundaries. The biggest challenge in itself is the accuracy of the model which is highly dependable on a variety of factors. Research papers [1] [2] [3] [4] [5] show that the public mood (which can be captured from large-scale Twitter feeds) is a valuable indicative of the future of a brand, although further research needs to be taken in order to evaluate many more factors that can indeed affect the investment decisions and make a robust model out of.

## Accomplishments that we're proud of
A pipeline from the twitter provided training data through a complex algorithm that will hopefully output a graph that is as close as possible to actual trends. We are aware of the multiple severe points of consideration that need to be taken into account in order to significantly improve the model but we consider that a prototype that relates to the workings of famous research teams is what matters for now.

## What we learned
How to properly structure a complex project with many components that need to constantly collaborate with each other and how to best split the work to parallelize it as effective as possible. Neither of us were familiar with finance until now and we worked though a challenging plan that we found brought some particular insight into how the market works and how banks the economy operate in this modern world.

## What's next for Tweetpredict
Hopefully having access to more curated data and more powerful hardware to run the algorithm on, as well as a better way to graph the results and present them against other predicting algorithms around the world.

[1] https://arxiv.org/pdf/1010.3003v1.pdf    
[2] https://pdfs.semanticscholar.org/4ecc/55e1c3ff1cee41f21e5b0a3b22c58d04c9d6.pdf   
[3] http://eprints.lincoln.ac.uk/11274/1/ASONAM%202012.pdf   
[4] https://arxiv.org/pdf/1607.01958.pdf   
[5] http://cs229.stanford.edu/proj2011/ChenLazer-SentimentAnalysisOfTwitterFeedsForThePredictionOfStockMarketMovement.pdf   


more information over here https://devpost.com/software/tweetpredict
