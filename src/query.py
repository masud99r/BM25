__author__ = 'Nick Hirakawa'

from invdx import build_data_structures
from rank import score_BM25
from rank import score_BM25_formula
import operator


class QueryProcessor:
	def __init__(self, queries, corpus):
		self.queries = queries
		self.index, self.dlt = build_data_structures(corpus)

	def run(self):
		results = []
		for query in self.queries:
			results.append(self.run_query(query))
		return results

	def run_query(self, query):
		query_result = dict()
		for term in query:
			if term == "NONE":
				continue
			if term in self.index:
				doc_dict = self.index[term] # retrieve index entry # THE TRICKS
				#print("DF of term="+str(term)+" is="+str(len(doc_dict)))
				doc_freq = len(doc_dict)
				for docid, freq in doc_dict.iteritems(): #for each document and its word frequency
					score = score_BM25_formula(n=len(doc_dict), f=freq, qf=1, r=0, N=len(self.dlt),dl=self.dlt.get_length(docid), avdl=self.dlt.get_average_length(), df =doc_freq) # calculate score
					if docid in query_result: #this document has already been scored once
						query_result[docid] += score
					else:
						query_result[docid] = score
		return query_result