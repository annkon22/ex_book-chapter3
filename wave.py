from math import cos, radians

#createe a string with spaces proportional to cosine 
#of x in degrees

def make_dot_string(x):
    numspaces = int(20 * cos(radians(x)) + 20) #scale
    #to 0 - 40 spaces
    st = " " * numspaces + "o"  #place
    # "o" after the spaces
    return st

def main():
    for i in range(0, 1800, 12):
        s = make_dot_string(i)
        print(s)
    
main()


