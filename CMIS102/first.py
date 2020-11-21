value1 = input("number 1: \n")
value2 = input("number 2:\n")

def is_integer(n):
    try:
        int(n)
        return True
    except ValueError:
        return False
 

