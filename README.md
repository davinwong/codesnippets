Code-Snippets
=============


Graphite Apache Log Parser (Employer Challenge)
-----------------------------------------------
Graphs http status code counts (1xx, 2xx, 3xx, 4xx, 5xx) over time. Parses Apache .log file, sends data to carbon and graphs with Graphite.


Movie Review Sentiment Analysis (Stanford NLP coursera.org)
-----------------------------------------------------------

Classifies movie reviews as positive or negative with ~80% accuracy. Uses multinomial naive bayes classifer with bag of words assumption and Laplace smoothing.

"Bag of words" - one positive and one negative dictionary. The positive dictionary contains counts of all words from positive training movie reviews and same for negative.

During classification in test set, the dictionaries are used to compute the probability of positive for each word, and then multiplies all these probabilities. Same for negative. Based on this, positive or negative is the output.