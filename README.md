Code-Snippets
=============


Graphite Apache Log Parser (Employer Challenge)
-----------------------------------------------
Graphs http status code counts (1xx, 2xx, 3xx, 4xx, 5xx) over time. Parses Apache .log file, sends data to carbon and graphs with Graphite.


Movie Review Sentiment Analysis (Stanford NLP coursera.org)
-----------------------------------------------------------

Classifies movie reviews as positive or negative with ~80% accuracy. Uses multinomial naive bayes classifer with bag of words assumption and Laplace smoothing.

"Bag of words" - there is one positive and one negative dictionary. The positive dictionary contains counts of all words from positive training movie reviews and same for negative.

During classification in test set, the dictionaries are used to compute for each word the probability of positive, and then multiplies all these probabilities. Same for negative. Based on this, positive or negative is the output.

Notes: For run-time purposes, it was necessary to use addition of logarithms was used instead of multiplication. Also, there initial problems of underflow solved by a similar method using log.


C# Treeview function (1st co-op)
--------------------------------

The treeview function contains some logic to update a treeview full of element nodes (event log folders and event message items). It works by comparing the data stored in objects with the treeview object. For example, if an event source object is deleted, the function will remove the corresponding treeview event source item.

The recent files functions users to quickly see and open the 6 most recent files under File >> Recent Files in the menu bar.