import sys
import getopt
import os
import math

class NaiveBayes:
  class TrainSplit:
    """Represents a set of training/testing data. self.train is a list of Examples, as is self.test. 
    """
    def __init__(self):
      self.train = []
      self.test = []

  class Example:
    """Represents a document with a label. klass is 'pos' or 'neg' by convention.
       words is a list of strings.
    """
    def __init__(self):
      self.klass = ''
      self.words = []


  def __init__(self):
    """NaiveBayes initialization"""
    self.FILTER_STOP_WORDS = False
    self.stopList = set(self.readFile('../data/english.stop'))
    self.numFolds = 10
    
    self.dictp = {}
    self.dictn = {}

    self.docsp = 0
    self.docsn = 0
    self.tokensp = 0
    self.tokensn = 0

    self.v = 0
  
  def classify(self, words):
    """ 
      * This is the "Bag of Words" algorithm.
      * 'words' is a list of words to classify.
      * Returns 'pos' or 'neg' classification.
    """
    pos = 0.0
    for i in range( len(words) ):

      if words[i] in self.dictp:
        a = self.dictp[words[i]]
        
      if words[i] not in self.dictp:
        a = 0

      pos += abs( math.log10(float(a) + 1) - math.log10(self.tokensp + self.v) )

    pos *= float( self.docsp ) / (self.docsp + self.docsn)

    neg = 0.0
    for i in range( len(words) ):

      if words[i] in self.dictn:
        b = self.dictn[words[i]]
        
      if words[i] not in self.dictn:
        b = 0

      neg += abs( math.log10(float(b) + 1) - math.log10(self.tokensn + self.v) )

    neg *= float(self.docsn) / (self.docsp + self.docsn)

    if pos >= neg:
      return 'neg'
    if pos < neg:
      return 'pos'
  

  def addExample(self, klass, words):
    """
     * Train model on an example document with label klass ('pos' or 'neg') and
     * words, a list of strings.
     * Returns nothing
    """
    if klass == 'pos':
      
      #document increment
      self.docsp += 1
      
      for i in range( len(words) ):

        #vocab increment
        if words[i] not in self.dictp and words[i] not in self.dictn:
          self.v += 1

        #in vocab -> increment count of word
        if words[i] in self.dictp:
          self.dictp[ words[i] ] += 1

        #not in vocab -> add to vocab
        if words[i] not in self.dictp:
          self.dictp[ words[i] ] = 1

        #token increment
        self.tokensp += 1

    if klass == 'neg':
      
      #document increment
      self.docsn += 1
      
      for i in range( len(words) ):

        #in vocab -> increment count of word
        if words[i] not in self.dictp and words[i] not in self.dictn:
          self.v += 1

        #have it, increment
        if words[i] in self.dictn:
          self.dictn[ words[i] ] += 1

        #not in vocab -> add to vocab
        if words[i] not in self.dictn:
          self.dictn[ words[i] ] = 1

        #token increment
        self.tokensn += 1
