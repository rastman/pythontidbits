
import os

def getallmatchfiles( datadir,patterin=None,extin=None):
	'''
	:param datadir: input directory where you want to search for files (both with extension and some pattern inside the names)
	:param patterin: the files should contain these patterns (optional)
	:param extin: the extensions you require
	:return:
	'''
	outputf = []
	extcomplete=[]
	if patterin is not None and type(patterin) is not list:
		patterin=[patterin]
	if extin is not None:
		for e in extin:
			if e[0] is not '.':
				e='.'+e
			extcomplete.append(e.upper())
			extcomplete.append(e.lower())
	if os.path.isdir(datadir):
		filesunsorted = [fr for fr in os.listdir(datadir) if os.path.isfile(os.path.join(datadir, fr))]
		if extin is not None:
			filesunsorted = [i for i in filesunsorted if i.endswith(tuple(extin))]
		if patterin is not None:
			filesunsorted = [i for i in filesunsorted if any(substring in i for substring in patterin)]
		myfiles = sorted(filesunsorted)
		for i in range(len(myfiles)):
			outputf.append(os.path.join(datadir, myfiles[i]))
	return outputf
