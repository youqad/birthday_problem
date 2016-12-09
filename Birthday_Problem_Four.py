from quicktions import Fraction
import numpy as np
import matplotlib.pyplot as plt
 
 
N = 365

n_max = 400
x = range(1, n_max)
plt.xlim(1, n_max)
plt.ylim(0, 1)

special_ycoord = [0.5, 0.95]
 
special_xcoord = []
 
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
        


def special_plot(x,y):
    global special_ycoord, special_xcoord
    
    if not special_ycoord or len(special_xcoord)>=len(special_ycoord):
        return y
    
    if y >= special_ycoord[len(special_xcoord)]:
        special_xcoord.append(x)
    
    return y
     





P_4 = p4() 
plt.plot(x, [special_plot(i, next(P_4)) for i in x], 'g.-')
plt.title('Graphe de la suite $(p_n)_{n≥0}$')
plt.ylabel('$p_n$')
plt.xlabel('$n$')
plt.grid(True)
 
for i, t in enumerate(special_xcoord): 
    plt.plot([t,t],[0,special_ycoord[i]], color ='red', linewidth=3.5, linestyle="--")
    plt.scatter([t,],[special_ycoord[i],], 50, color ='red')
    
    plt.annotate(r'$n_{'+str(special_ycoord[i])+'}='+str(t)+'$',
                xy=(t, special_ycoord[i]), xycoords='data',
                xytext=(-110, 0), textcoords='offset points', fontsize=16,
                arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=-.2")) 

special_xcoord.extend([1, n_max])
special_ycoord.extend([0,1])

plt.xticks(special_xcoord)
plt.yticks(special_ycoord)

 
# plt.legend()
# plt.legend(bbox_to_anchor=(0.80, 0.4), loc=2, borderaxespad=0.)
 
plt.show()


    
