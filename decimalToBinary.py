def decimalToBinary(n):
    """
    Parameters
    ----------
    n : {int}
        A Decimal number represented in base-10.

    Returns
    -------
    {str}
        The base-2 Binary translation of the inputted Decimal base-10 number. 
    """
    bit_string = []

    while n > 0:
        print(f"n = {n}\tremainder = {n%2}")    # pretty prints 'n' & the remainder for visualization
        bit_string.append(n % 2)                # collects the remainder when n is divided by 2 for the result
        n //= 2                                 # floor divides n by 2 for the next cycle until it's 0
    
    return ''.join(reversed([str(x) for x in bit_string]))

def main():
    n = int(input("Input a Decimal Number: "))
    print(f"Your Binary Number is: {decimalToBinary(n)}")

main()