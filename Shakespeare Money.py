import Tkinter as tk
import random
import time

space="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890@. "
splen=len(space)
#print splen,"Hi"


def find_dupes(st):
    seen=[]
    for i in range(len(st)):
        if i in seen:
            k=gen_population(1,len(i))[0]
            if k not in st:
                st[i]=k
            else:
                st[i]=k[::-1]
        seen.append(i)
    return st


def create_pairs(tar,p):
    pai=[]
    selected=[]
    pop_score={}
    #print len(p),"CreatePairs"
    for i in p:
        #print len(pop_score)
        pop_score[i]=calculate_fitness(tar,i)
    pi=[]
    #print len(pop_score),"After pop score"
    l=pop_score[max(pop_score, key=pop_score.get)]
    #print len(pop_score),"pop score"
    p = sorted(pop_score, key=pop_score.get)
    #print len(p),"After sorting ascending"
    p=p[::-1]
    print p,len(p)
    while (len(pai)*2)<len(p):
        #print len(pai)
        if len(pi)==2:

            pai.append(pi)

            pi=[]
            continue
        for i in p:
            if len(pi)==2:
                break
            if i not in selected:
                k=random.randint(0,l)
                if k<=pop_score[i]:
                    pi.append(i)
                    selected.append(i)
    #print pai
    return pai

    #print find_dupes(pai)





def calculate_fitness(target,member):
    score=0
    for i in range(len(target)):
        if target[i]==member[i]:
            score+=1
    return int((float(score)/len(target))*100)

print calculate_fitness("hello","hdnld")

def gen_population(size,leng):
    pop=[]
    while len(pop)<size:
        arc=""
        for j in range(leng):
            k=random.randint(0,splen-1)
            #print k
            arc+=space[k]
        if arc not in pop:
            pop.append(arc)
    return pop


def crossover(pai,pop,tar):
    po=[]
    for i in pai:

        t=i
        x=t[0]
        y=t[1]
        tl=random.randint(0,len(x)-1)
        l=len(x)/2
        t1=x[:l]+y[l:]
        t2=x[l:]+y[:l]
        t3= y[:l] + x[l:]
        t4= y[l:] + x[:l]
        t5 = x[:tl] + y[tl:]
        t6 = x[tl:] + y[:tl]
        t7 = y[:tl] + x[tl:]
        t8 = y[tl:] + x[:tl]
        for j in range(1,len(x),2):
            t9=x[:j]+y[j]+x[j+1:]
            t10=y[:j]+x[j]+y[j+1:]
            x=t9
            y=t10
        txf={}
        txf[t1]=calculate_fitness(tar,t1)
        txf[t2] = calculate_fitness(tar, t2)
        txf[t3] = calculate_fitness(tar, t3)
        txf[t4] = calculate_fitness(tar, t4)
        txf[t5] = calculate_fitness(tar, t5)
        txf[t6] = calculate_fitness(tar, t6)
        txf[t7] = calculate_fitness(tar, t7)
        txf[t8] = calculate_fitness(tar, t8)
        txf[t9] = calculate_fitness(tar, t9)
        txf[t10] = calculate_fitness(tar, t10)

        for i in range(15-len(txf)):
            tmp=""
            tmp=gen_population(1,len(tar))[0]
            txf[tmp]=calculate_fitness(tar,tmp)
        p = sorted(txf, key=txf.get)
        p=p[::-1]
        #print p
        flag=0
        for i in p:
            if flag >=2:
                break
            if i not in po:
                po.append(i)
                flag+=1


    #print len(po),"Cross"
    po=find_dupes(po)
    return po

def mutations(pop,mutation):
    po=[]
    for i in pop:
        t=i
        for j in range(len(t)):
            k = random.randint(0, 100)
            if k <= mutation:
                x = random.randint(0, splen - 1)
                t = t[:j] + space[x] + t[j + 1:]
        po.append(t)
    #print len(po),"Mut"
    po = find_dupes(po)
    return po

def Algo():
    #print "Run algo"

    population=int(populationE.get())
    mutation=int(mutationE.get())
    target=targetE.get()
    length=len(target)
    init_pop=gen_population(population,length)
    best_fitness=1
    best_phrase=""
    pop=init_pop
    k=1

    while best_fitness<100:
        avg=0
        pairs = create_pairs(target, pop)
        pop=crossover(pairs,pop,target)
        pop=mutations(pop,mutation)
        print len(pop),"After all"
        for i in pop:
            c=calculate_fitness(target,i)
            avg+=c
            if c>best_fitness:
                best_fitness=c
                best_phrase=i
        avgf = float(avg) / len(pop)
        BestP=tk.Label(w,text=best_phrase)
        BestP.place(relx=0.14,rely=0.7)
        Generations=tk.Label(w,text=str(k))
        Generations.place(relx=0.15,rely=0.8)
        BestF = tk.Label(w, text=str(best_fitness))
        BestF.place(relx=0.16, rely=0.9)
        avgf = tk.Label(w, text=str(avgf))
        avgf.place(relx=0.25, rely=0.9)
        #time.sleep(0.1)
        w.update()
        k+=1














w= tk.Tk()
w.title("Genetic Algorithm")
w.geometry("1270x720")


heading=tk.Label(w,text="Genetic Algorithm Example")
heading.place(relx=0.43,rely=0.01)


settings=tk.Label(w,text="Set your variables")
settings.place(relx=0.1,rely=0.4)

targetL=tk.Label(w,text="Target String:")
targetE=tk.Entry(w)
targetL.place(relx=0.08,rely=0.45)
targetE.place(relx=0.14,rely=0.45)

populationL=tk.Label(w,text="Population:")
populationE=tk.Entry(w)
populationL.place(relx=0.08,rely=0.5)
populationE.place(relx=0.135,rely=0.5)

mutationL=tk.Label(w,text="Mutation:")
mutationE=tk.Entry(w)
mutationL.place(relx=0.08,rely=0.55)
mutationE.place(relx=0.128,rely=0.55)

B=tk.Button(w,text="Run",command=Algo)
#input.bind('<Return>',print_entry)
B.place(relx=0.09,rely=0.6)
BP=tk.Label(w,text="Best Text:")
BP.place(relx=0.08,rely=0.7)
gen=tk.Label(w,text="Generations:")
gen.place(relx=0.09,rely=0.8)
gen=tk.Label(w,text="Fitness:")
gen.place(relx=0.1,rely=0.9)
w.mainloop()

