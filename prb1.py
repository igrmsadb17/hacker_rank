# in question no string methods should be used to get output
# but i used str() to convert integers into str and join() to join these strings into one 
def main(n):
    if n in range(1,151):
        L = []
        for i in range(1, n+1):
            L.append(str(i))
        return "".join(L)
    
if __name__ == "__main__":
    n = int(input("n:"))
    x = main(n)
    print(x)
