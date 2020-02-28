#Programmer: Zhaoyang Dai
#Section: 22C:016:A06
#ID: 00719596
def gradeDistribution(examScores):
    def a(x):                      #define a functions contain the score from 0 to 10
        return 0<=x<=10
    def b(x):                      #from 10 to 20, excluding 10
        return 10<x<=20
    def c(x):                      #from 20 to 30, excluding 20
        return 20<x<=30
    def d(x):                      #from 30 to 40, excluding 30
        return 30<x<=40
    def e(x):                      #from 40 to 50, excluding 40
        return 40<x<=50
    def f(x):                      #from 50 to 60, excluding 50
        return 50<x<=60
    def g(x):                      #from 60 to 70, excluding 60
        return 60<x<=70
    def h(x):                      #from 70 to 80, excluding 70
        return 70<x<=80
    def i(x):                      #from 80 to 90, excluding 80
        return 80<x<=90
    def j(x):                      #from 90 to 100, excluding 90
        return 90<x<=100
    first = len(filter(a,examScores))          #count numbers of the exam score 
    second = len(filter(b,examScores))         #in each range
    third = len(filter(c,examScores))
    forth = len(filter(d,examScores))
    fifth = len(filter(e,examScores))
    sixth = len(filter(f,examScores))
    seventh = len(filter(g,examScores))
    eighth = len(filter(h,examScores))
    ninth = len(filter(i,examScores))
    tenth = len(filter(j,examScores))
    #return the number of grades in each range to a list
    return [first,second,third,forth,fifth,sixth,seventh,eighth,ninth,tenth]