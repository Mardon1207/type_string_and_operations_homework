def main(x1,x2,x3):
    """
    Given three integers, x1, x2, and x3, return the "[x1, x2, x3]" string.
    Args:
        x1: int
        x2: int
        x3: int
    Returns:
        str: return answer.
    """
    return "["+x1+", "+x2+", "+x3+"]"
x1=int(input())
x2=int(input())
x3=int(input())
x1=str(x1)
x2=str(x2)
x3=str(x3)
print(main(x1,x2,x3))