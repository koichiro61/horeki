import re
import datetime

horeki_ymd = re.compile(
	r'(?P<nengo>明治|大正|昭和|平成|令和)\s*'\
		'(?P<nen>\d+|元)\s*年(\s*(?P<tsuki>\d+)\s*月)*\s*'\
		'((?P<hi>\d+)\s*日)*')
		
horeki_base = {'明治':1867, '大正':1911, '昭和':1925, '平成':1989, '令和':2018 }

def horeki2seireki(s):
	global horeki_ymd
	global horeki_base
	
	m = re.match(horeki_ymd, s)
	
	if m is None:
		return(datetime.date(datetime.MINYEAR, 1, 1))
	else:
		base = horeki_base[m.group('nengo')]
		if(m.group('nen')) == '元':
			nen = 1
		else:
			nen = int(m.group('nen'))
			
		if m.group('tsuki') == None:
			tsuki = 1
		else:
			tsuki = int(m.group('tsuki'))
			
		if m.group('hi') == None:
			hi = 1
		else:
			hi = int(m.group('hi'))
				
		return datetime.date(base + nen, tsuki, hi)
