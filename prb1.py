# in question no string methods should be used to get output
# but i used str() to convert integers into str and join() to join these strings into one 
def main(n):
    if n in range(1,151):
        for i in range(1, n+1):
            # end = "" will print the int in a single line without spaces
            print(i, end = "")

    
if __name__ == "__main__":
    n = int(input("n:"))
    main(n)
