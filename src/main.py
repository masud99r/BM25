__author__ = 'Nick Hirakawa'


from parse import *
from query import QueryProcessor
import operator


def main():
	qp = QueryParser(filename='../text/queries.txt')
	#qp = QueryParser(filename='../text/query_documents.txt')
	#cp = CorpusParser(filename='../text/corpus.txt')
	#cp = CorpusParser(filename='../text/candidate_methodbody_documents_only.txt')
	cp = CorpusParser(filename='../text/candidate_documents_only.txt')
	qp.parse()
	queries = qp.get_queries()
	cp.parse()
	corpus = cp.get_corpus()
	proc = QueryProcessor(queries, corpus)
	results = proc.run()
	qid = 0
	print len(results)
	for result in results:
		#print result
		#sorted_x = sorted(result.iteritems(), key=operator.itemgetter(1))
		sorted_x = sorted(result.items(), key=operator.itemgetter(1), reverse=True)
		#sorted_x.reverse()
		index = 0
		print sorted_x
		print len(sorted_x)
		for i in sorted_x[:100]:
			tmp = (qid, i[0], index, i[1])
			print '{:>1}\tQ0\t{:>4}\t{:>2}\t{:>12}\tNH-BM25'.format(*tmp)
			index += 1
		qid += 1


if __name__ == '__main__':
	main()