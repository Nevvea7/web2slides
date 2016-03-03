import urllib
import urllib2
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
sys.path.append('./html2text')
import html2text
from html2text import HTML2Text

ALLAN_NOTES_LINK = "http://cs.nyu.edu/~gottlieb/courses/os202/class-notes.html"

SLIDE_STARTER = {'#', '##', '###'}

def main():
	h = HTML2Text(baseurl=ALLAN_NOTES_LINK)
	web_pg = getHTML(ALLAN_NOTES_LINK)
	md = h.handle(web_pg)
	w = open('tmp', 'w')
	w.write(md)
	w.close
	divideToLectures('tmp')

def divideToLectures(md):
	lecture_no = 0
	rlines = open(md, 'r').readlines()

	f = open('lecture-%d.html' % lecture_no, 'w')
	printHeadings(f)
	lines = 0
	consec_empty_lines = 0
	for l in rlines:
		#l = str(l)
		# if there are 3 consecutive empty lines then new slide
		if len(l) == 0:
			consec_empty_lines += 1
			if consec_empty_lines == 2:
				newPage(f)
			continue

		if l.startswith("Start Lecture #"):
			printEndings(f)
			f.close()
			lecture_no += 1
			f = open('lecture-%d.html' % lecture_no, 'w')
			printHeadings(f)
			lines = 0

		if l.startswith('!['):
			lines += 5

		sp = l.split()
		if lines >= 13 or (len(sp) > 0 and sp[0] in SLIDE_STARTER):
			newPage(f)
			lines = 0

		f.write(l)
		lines += 1
	printEndings(f)
	f.close()

def newPage(f):
	f.write("\n_Contents generated from: " + ALLAN_NOTES_LINK + "_\n")
	f.write('---\n')

def printHeadings(f):
	h = open('headings', 'r')
	for l in h:
		f.write(l)

def printEndings(f):
	e = open('endings', 'r')
	for l in e:
		f.write(l)


def getHTML(link):
	aResp = urllib.urlopen(link)
	web_pg = aResp.read()
	#web_pg = web_pg
	return web_pg


main()