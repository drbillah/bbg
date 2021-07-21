#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 16:19:59 2019

@author: masum
"""

import csv

mygene = {}
goterm = {}
flag = 0
with open('/home/masum/Documents/goat/bbg/analysis/proteins.fasta.tsv') as tsvfile:
  reader = csv.reader(tsvfile, delimiter='\t')
  for row in reader:
      geneID = row[0]
      mygene[geneID] = 0
      try:
          annotation = row[13]
          if annotation:
              goterm[geneID] = annotation
      except:
          flag = 0 
          
print(len(mygene)) # Number of gene Annotated by InterProScan
print(len(goterm)) # At least 1 GO (GeneOntology) term
