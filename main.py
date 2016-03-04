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

LINE_SIZE = 75

def main():
	h = HTML2Text(baseurl=ALLAN_NOTES_LINK)
	web_pg = getHTML(ALLAN_NOTES_LINK)
	md = h.handle(web_pg)
	w = open('tmp', 'w')
	w.write(md)
	w.close
	lecture = divideToLectures('tmp')
	lecture_no = lecture[0]
	lecture_titles = lecture[1]
	index_html = open('index.html', 'w')
	printHeadings(index_html)
	index_html.write('## Lecture Notes for OS202\n\n')
	# index_html.write('\n_Contents generated from: ' + ALLAN_NOTES_LINK + '_\n\n')
	line = 0
	for i in range(lecture_no):
		if (line >= 18) :
			newPage(index_html)
			line = 0
		index_html.write('[lecture-%d](lecture-%d.html)\n' % (i, i))
		index_html.write(lecture_titles[i] + '\n\n')
		line += 2
	printEndings(index_html)

def divideToLectures(md):
	lecture_no = 0
	rlines = open(md, 'r').readlines()

	f = open('lecture-%d.html' % lecture_no, 'w')
	printHeadings(f)
	lines = 0
	consec_empty_lines = 0
	lecture_titles = []
	lecture_title = ""
	for rl in rlines:
		rls = [ rl[i:i + LINE_SIZE] for i in range(0, len(rl), LINE_SIZE) ]
		for l in rls:
			# if there are 3 consecutive empty lines then new slide
			if len(l) == 0:
				consec_empty_lines += 1
				if consec_empty_lines == 2:
					newPage(f)
					consec_empty_lines = 0
				continue

			if l.startswith("Start Lecture #"):
				printEndings(f)
				f.close()
				lecture_no += 1
				lecture_titles.append(lecture_title)
				lecture_title = ""
				f = open('lecture-%d.html' % lecture_no, 'w')
				printHeadings(f)
				lines = 0

			if l.startswith('!['):
				lines += 10

			sp = l.split()
			if l.startswith("# "):
				lecture_title += l[2:] + "\t"
			
			if lines >= 20 or (len(sp) > 0 and sp[0] in SLIDE_STARTER):
				
				newPage(f)
				lines = 0

			f.write(l)
			lines += 1
	printEndings(f)
	f.close()
	return [lecture_no, lecture_titles]

def newPage(f):
	f.write("\n _Contents generated from: " + ALLAN_NOTES_LINK + "_\n\n")
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