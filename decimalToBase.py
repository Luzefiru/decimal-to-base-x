def decimalToBase(x, n):
    """
    Parameters
    ----------
    x : {int}
        The radix of the numer system to convert to.
    n : {int}
        A Decimal number represented in base-10.

    Returns
    -------
    {str}
        The base-x translation of the inputted Decimal base-10 number. 

    """
    bit_string = []

    while n > 0:
        print(f"n = {n}\tr = {n%x}")            # pretty prints 'n' & the remainder for visualization
        bit_string.append(n % x)                # collects the remainder when n is divided by 'x' for the result
        n //= x                                 # floor divides n by 'x' for the next cycle until it's 0
    
    return ''.join(reversed([str(x) for x in bit_string]))

def main():
    n = int(input("Input a Decimal Number: "))
    x = int(input("Input the base you want to convert to: "))
    print(f"Your base-{x} Number is: {decimalToBase(x, n)}")

main()
