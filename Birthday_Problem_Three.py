from quicktions import Fraction
import numpy as np
import matplotlib.pyplot as plt
 
 
N = 365

n_max = 200
x = range(1, n_max)
plt.xlim(1, n_max)
plt.ylim(0, 1)

special_ycoord = [0.5, 0.95]
 
special_xcoord = []
 
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

def special_plot(x,y):
    global special_ycoord, special_xcoord
    
    if not special_ycoord or len(special_xcoord)>=len(special_ycoord):
        return y
    
    if y >= special_ycoord[len(special_xcoord)]:
        special_xcoord.append(x)
    
    return y
     





P_3 = p3() 
plt.plot(x, [special_plot(i, next(P_3)) for i in x], 'b.-')
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

