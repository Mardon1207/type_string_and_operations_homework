def main(x,y):
    """
    Given two integers x, y return the "(x+y)*2={answer}" string.
    Args:
        x: int
        y: int
    Returns:
        str: return answer.
    """
    return "("+x+"+"+y+")"+"*""2"+"="+s
x=int(input())
y=int(input())
s=(x+y)*2
x=str(x)
y=str(y)
s=str(s)
print(main(x,y))