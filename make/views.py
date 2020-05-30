from django.shortcuts import render
def home(request):
    return render(request,'index.htm')
def add(request):
    x=request.POST['n1']
    y=request.POST['n2']
    n=list(x)
    m=list(y)
    def same(x,y):
        h=list()
        k=list()
        c=x.copy()
        d=y.copy()
        for i in range(0,len(x)):
            for j in range(0,len(d)):
               if x[i]==d[j]:
                   h.append(i)
                   del d[j]
                   break
        c=[i for j,i in enumerate(c) if j not in h ]
        return len(c)+len(d)
    v=same(n,m)
    def flame(v):
        t=list("flames")
        p = list("flames")
        while len(t)<v:
           t.extend(t)
        for i in range(0,5):
            n = t[v-1]
            del t[0:v]
            p.remove(n)
            if n in t:
                t.remove(n)
            while len(t)<v:
                t.extend(p)
        return p[0]
    d={'f':"Friends",'l':"love",'a':"Affection",'m':"Marriage",'e':"Enemies",'s':"Sister"}
    i=flame(v)
    c=d[i]


    return render(request,'result.htm',{'res':c})





    





    



# Create your views here.
