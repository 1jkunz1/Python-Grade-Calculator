#First function 'updown'
def updown(x,y):
    if 0 < x < 40:
        newscore = ((y-1)*(25) / (4)) + x
        if newscore > 58:
            newscore = 58
    if 40 <= x < 60:
        newscore = ((y-1)*(20) / (4)) + x
        if newscore > 73:
            newscore = 73
    if 60 <= x < 70:
        newscore = ((y-1)*(15) / (4)) + x
        if newscore > 78:
            newscore = 78
    if 70 <= x < 80:
        newscore = ((y-1)*(10) / (4)) + x
        if newscore > 85:
            newscore = 85
    if 80 <= x < 90:
        newscore = ((y-1)*(8) / (4)) + x
        if newscore > 90:
            newscore = 90
    return newscore

#Second function with the kind score
def kind(x,y):
    if 0 < x < 40:
        newscore = ((y-1)*(25) / (4)) + x
        if newscore > 58:
            newscore = 58
    if 40 <= x < 60:
        newscore = ((y-1)*(20) / (4)) + x
        if newscore > 73:
            newscore = 73
    if 60 <= x < 70:
        newscore = ((y-1)*(15) / (4)) + x
        if newscore > 78:
            newscore = 78
    if 70 <= x < 80:
        newscore = ((y-1)*(10) / (4)) + x
        if newscore > 85:
            newscore = 85
    if 80 <= x < 90:
        newscore = ((y-1)*(8) / (4)) + x
        if newscore > 90:
            newscore = 90
    if newscore < x:
        newscore = x
    return newscore

#open the file with the exam data
with open('Exam1.txt', 'r') as file:
    mylist= file.readlines()
    #Strip all whitespace
    mylist = [i.rstrip() for i in mylist[0:]]
    #split the newly stripped list
    newlist= [i.split(',') for i in mylist[0:]]
    name= [i[0].strip() for i in newlist]
    original_score= [i[1].strip() for i in newlist]
    redem_points= [i[2].strip() for i in newlist]
    x=map(int, original_score)
    y=map(int, redem_points)
    scores=zip(x,y)
    finalupdown= [updown(i[0], i[1]) for i in scores[0:]]
    finalkind= [kind(i[0], i[1]) for i in scores[0:]]
    students=zip(name, original_score, redem_points, finalupdown, finalkind)
    ourstring=str(students).strip('[]')

#Finally write the scores to our new file
f=open('RedExam1', 'r+')
f.write(ourstring)

    


        
        
        
        
        
        
        

        
