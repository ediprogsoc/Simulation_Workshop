import numpy as np
import matplotlib.pyplot as plt

def montyHallGraph(outcomes):
    x = np.cumsum(outcomes)
    plt.plot(x,x/np.array(range(1,len(x)+1)))
    plt.xlabel("Number of trial games")
    plt.ylabel("Cumulative average of 'should_switch'")
    plt.show()

def showDist(original_distribution, final_distribution):
    maxVal = max(max(original_distribution),max(final_distribution))
    bins = np.linspace(0,maxVal,50)
    plt.hist(original_distribution,bins,alpha=0.3,label='Start G = ' + str(round(gini(original_distribution),3)))
    plt.hist(final_distribution,bins,alpha=0.3,label='End G = ' + str(round(gini(final_distribution),3)))
    plt.xlabel('Wealth')
    plt.ylabel('Count')
    plt.legend()
    plt.show()