from scipy.stats import chisquare
import scipy

#op de plaats van de X frequentie vrouwelijke hashtag invoeren
#op de plaats van de Y frequentie mannelijke hashtag invoeren
#het is vereist dat de mannelijke en vrouwelijke hashtag hetzelfde zijn

def signi():
    X = 
    Y = 
    observed = scipy.array([X,Y])
    verwacht = (X+Y)/2
    print(verwacht)
    expected = scipy.array([verwacht])
    result = chisquare(observed,expected)
    print(result)

if __name__ == "__main__":
    signi()
        
