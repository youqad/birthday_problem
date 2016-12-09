from quicktions import Fraction
import numpy as np
import matplotlib.pyplot as plt
 
 
N = 365

n_max = 400
x = range(1, n_max)
plt.xlim(1, n_max)
plt.ylim(0, 1)

special_ycoord = [[0.5, 0.95], [0.5, 0.95]]
 
special_xcoord = [[],[]]



def p3():
    global N
    
    n=1
    
    is_n_even = False
    
    N_n = N
    
    
    TermsSum = [Fraction(N)]
    
    lenTermsSum = 1
    
    while True:
        yield float(1-Fraction(sum(TermsSum),N_n))
        #yield TermsSum, sum(TermsSum), N_n
        
        n+=1
        is_n_even = not is_n_even
        
        
        for i in range(lenTermsSum):
            TermsSum[i] = Fraction(TermsSum[i], Fraction((n-2*i)))
            TermsSum[i] *= n*(N-n+i+1)
        
        N_n *= N
        
        if is_n_even:
            TermsSum.append(Fraction(Fraction(TermsSum[-1]*2),Fraction((N-(n-(n/2-1))+1)*n)))
            lenTermsSum +=1


 
def p4():
    global N
    
    n=1
    
    is_n_not_multiple3 = 1
    
    is_nminus3j_even = [False]
    
    N_n = N
    
    
    TermsSum = [[Fraction(N)]]
    
    lenTermsSum = 1
    
    while True:
        yield float(1-Fraction(sum([i for j in TermsSum for i in j]),N_n))
        #yield TermsSum, sum([i for j in TermsSum for i in j]), N_n
        
        n+=1
        is_n_not_multiple3 = (is_n_not_multiple3 + 1) % 3
        
        for j in range(lenTermsSum):
            is_nminus3j_even[j] = not is_nminus3j_even[j]
        
        for j in range(lenTermsSum):
            for i in range(len(TermsSum[j])):
                TermsSum[j][i] = Fraction(TermsSum[j][i], Fraction(n-2*i-3*j))
                TermsSum[j][i] *= n*(N-n+i+2*j+1)
        
        N_n *= N
        
        for j in range(lenTermsSum):
            if is_nminus3j_even[j]:
                TermsSum[j].append(Fraction(Fraction(TermsSum[j][-1]*2),Fraction((N-(n-((n-3*j)/2-1)-2*j)+1)*(n-3*j))))

        
        if not is_n_not_multiple3:
            k = N-(n-2*(n/3-1))+1
            TermsSum.append([Fraction(Fraction(TermsSum[-1][0]*6),Fraction(k*(k+1)*2*n))])
            is_nminus3j_even.append(True)
            lenTermsSum +=1
        


def special_plot(x,y,num):
    global special_xcoord, special_ycoord
    
    if not special_ycoord[num] or len(special_xcoord[num])>=len(special_ycoord[num]):
        return y
    
    if y >= special_ycoord[num][len(special_xcoord[num])]:
        special_xcoord[num].append(x)
    
    return y
     

num = 0
P_3 = p3() 
y_3 = [special_plot(i, next(P_3), num) for i in x]

plt.plot(x, y_3, 'b.-')
plt.title('Graphe de la suite $(p_n)_{n≥0}$')
plt.ylabel('$p_n$')
plt.xlabel('$n$')
plt.grid(True)
 
for i, t in enumerate(special_xcoord[num]): 
    plt.plot([t,t],[0,special_ycoord[num][i]], color ='red', linewidth=3.5, linestyle="--")
    plt.scatter([t,],[special_ycoord[num][i],], 50, color ='red')
    
    plt.annotate(r'$n^{(3)}_{'+str(special_ycoord[num][i])+'}='+str(t)+'$',
                xy=(t, special_ycoord[num][i]), xycoords='data',
                xytext=(-110, 0), textcoords='offset points', fontsize=16,
                arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=-.2")) 



num=1
P_4 = p4() 
y_4 = [special_plot(i, next(P_4), num) for i in x]

plt.plot(x, y_4, 'g.-')
plt.title('Graphe de la suite $(p_n)_{n≥0}$')
plt.ylabel('$p_n$')
plt.xlabel('$n$')
plt.grid(True)
 
for i, t in enumerate(special_xcoord[num]): 
    plt.plot([t,t],[0,special_ycoord[num][i]], color ='red', linewidth=3.5, linestyle="--")
    plt.scatter([t,],[special_ycoord[num][i],], 50, color ='red')
    
    plt.annotate(r'$n^{(4)}_{'+str(special_ycoord[num][i])+'}='+str(t)+'$',
                xy=(t, special_ycoord[num][i]), xycoords='data',
                xytext=(-110, 0), textcoords='offset points', fontsize=16,
                arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=-.2")) 
                
                


special_xcoord.append([1, n_max])
special_ycoord.append([0,1])

plt.xticks([i for j in special_xcoord for i in j])
plt.yticks([i for j in special_ycoord for i in j])
 
 
plt.plot(x, y_3, color="blue", linewidth=2.5, linestyle="-", label="Problème des trois anniversaires")
plt.plot(x, y_4, color="green",  linewidth=2.5, linestyle="-", label="Problème des quatre anniversaires")

plt.legend(loc='bottom right', frameon=False) 
 
plt.show()


    
