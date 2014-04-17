Python-Grade-Calculator
=======================

Discrete Structures Programming Assignment 

Goal was to create a quick grade-calculation script. 

	
Your	instructor	has	decided	to	administer	a	“redemption	exam”	to	allow	students	to	
boost	their	grade	on	their	first	exam.		She	has	decided	on	a	method	that	increases	a	
student’s	score	based	on	their	performance	on	the	redemption	exam	as	well	as	their	
original	score	on	the	exam.		There	will	also	be	a	maximum	final	score	(depending	on	
the	scale,	of	course).		Here	is	a	summary:	
	
• For	students	whose	original	score	on	the	exam	is	below	a	40	(i.e.	in	the	
interval	[0,40)),	a	student	may	earn	a	maximum	of	25	additional	points,	
which	will	be	added	to	their	initial	score.		The	maximum	final	score	in	this	
situation	is	58.	
• For	students	whose	original	score	on	the	exam	is	between	40	and	60	(i.e.	in	
the	interval	[40,60)),	a	student	may	earn	a	maximum	of	20	additional	points,	
which	will	be	added	to	their	initial	score.		The	maximum	final	score	in	this	
situation	is	73.	
• For	students	whose	original	score	on	the	exam	is	in	the	60s	(i.e.	in	the	
interval	[60,70)),	a	student	may	earn	a	maximum	of	15	additional	points,	
which	will	be	added	to	their	initial	score.		The	maximum	final	score	in	this	
situation	is	78.	
• For	students	whose	original	score	on	the	exam	is	in	the	70s	(i.e.	in	the	
interval	[70,80)),	a	student	may	earn	a	maximum	of	10	additional	points,	
which	will	be	added	to	their	initial	score.		The	maximum	final	score	in	this	
situation	is	85.	
• For	students	whose	original	score	on	the	exam	is	in	the	80s	(i.e.	in	the	
interval	[80,90)),	a	student	may	earn	a	maximum	of	8	additional	points,	
which	will	be	added	to	their	initial	score.		The	maximum	final	score	in	this	
situation	is	90.	
	
The	redemption	exam	will	consist	of	5	questions,	and	the	number	of	points	earned	
will	be	determined	by	the	following	formula:	
	
Points	added	=	(#	questions	correct	–	1)	x	MAX	ADDITIONAL	POINTS/4	
	
Notice	that	this	formula	may	produce	negative	values,	meaning	that	if	a	student	
takes	this	redemption	exam,	their	score	could	DECREASE.		Your	instructor	has	not	
decided	whether	or	not	to	allow	for	that	possibility.		The	number	of	questions	
correct	must	be	an	integer	in	the	interval	[0,5],	and	should	be	verified.		The	original	
score	can	be	any	number	in	the	interval	[0,100].		The	result	should	be	a	float.	
	
Your	assignment	is	to	write	a	computer	program	to	address	the	following:	
	
1. Write	a	program	that	opens	a	text	file	containing	exam	score	data,	which	will	
be	called	Exam1.txt.		This	information	will	be	stored	in	the	following	format:	
	NAME,	ORIGINAL	SCORE,	REDEMPTION	SCORE	
	
2. The	program	calculates	two	values	and	adds	them	to	the	data:	
a. 	a	final	score	based	on	the	criteria	described	above,	with	scores	able	to	
increase	or	decrease,	depending	on	student	performance	(UPDOWN).	
b. a	final	score	based	on	the	criteria	described	above,	with	scores	only	
increasing	or	staying	the	same,	but	not	decreasing	(KIND).	
3. The	program	writes	this	data	to	a	text	file,	called	RedExam1.txt.		The	file	
should	contain	the	information	in	the	following	format:	
	
NAME,	ORIGINAL	SCORE,	REDEMPTION	SCORE,	UPDOWN,	KIND	
	
	
The	following	sample	data	can	be	used	to	test	your	program:	
	
Mouse	Mickey,	45,	1	
Duck	Donald,	68,	5	
Jetson	Elroy,	85,	2	
Doo	Scooby,	74,	4	
Chief	Master,	53,	0	
Am	I	Will,	82,	5	
	
The	result	should	be	a	file	consisting	of	the	following	(I	hope	I	calculated	these	
things	correctly!		Please	check	my	work…that’s	why	I	want	to	automate	this!):	
	
Mouse	Mickey,	45,	1,	45,	45	
Duck	Donald,	68,	5,	78,	78	
Jetson	Elroy,	85,	2,	87,	87	
Doo	Scooby,	74,	4,	81.5,	81.5	
Chief	Master,	53,	0,	48,	53	
Am	I	Will,	82,	5,	90,	90	
	
	
What	does	this	have	to	do	with	discrete	structures?	If	you	have	been	paying	
attention	in	class,	you	will	realize	that	this	is	exactly	what	your	instructor	has	
decided	to	do.		To	show	your	appreciation,	you	can	help	her	with	the	calculations	
involved	in	determining	the	final	score.		And	you	can	benefit	from	the	experience	of	
writing	programs	that	use	logic,	calculations	based	on	conditional	statements,	etc…		
Do	not	include	any	sneaky	code	(like	checking	to	see	if	the	name	is	yours,	and	then	
changing	your	grade	using	a	different	algorithm!).
