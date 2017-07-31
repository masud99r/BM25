__author__ = 'Nick Hirakawa'


from math import log

k1 = 1.5
k2 = 1.5
b = 0.75
R = 0.0


def score_BM25(n, f, qf, r, N, dl, avdl,df):
	K = compute_K(dl, avdl)
	first = log( ( (r + 0.5) / (R - r + 0.5) ) / ( (n - r + 0.5) / (N - n - R + r + 0.5)) )
	second = ((k1 + 1) * f) / (K + f)
	third = ((k2+1) * qf) / (k2 + qf)
	return first * second * third
def score_BM25_formula(n, f, qf, r, N, dl, avdl, df):
	# f is raw term freq, make it sublinear tf scaling
	f = 1.0 + log(f)
	upper_doc = (k1 + 1) * f
	lower_doc = k1 * ((1 - b) + b * (float(dl) / float(avdl))) + f
	doc_weight = (upper_doc * 1.0) / lower_doc

	upper_query = (k2 + 1) * qf
	lower_query = k2 + qf
	query_weight = (upper_query * 1.0) / lower_query
	#qterm_idf = 1.0 + log(float(N)/float(df)) # method 1
	qterm_idf = 1.0 + log((1.0 + float(N))/(1.0 + float(df))) #smoothed idf. method 2
	calculated_doc_score = qterm_idf * doc_weight * query_weight
	return calculated_doc_score

def compute_K(dl, avdl):
	return k1 * ((1-b) + b * (float(dl)/float(avdl)) )