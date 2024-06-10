from nada_dsl import *

def nada_main():
    # Define the party providing the input
    party1 = Party(name="Party1")
    
    # Create a secret integer input for the number of terms to compute in the Fibonacci sequence
    n = SecretInteger(Input(name="n", party=party1))
    
    # Initialize the first two Fibonacci numbers and the counter
    fib1 = SecretInteger(0)
    fib2 = SecretInteger(1)
    i = SecretInteger(2)  # Start from the third term
    
    # Loop to calculate the Fibonacci sequence up to the nth term
    while i <= n:
        new_fib = fib1 + fib2
        fib1 = fib2
        fib2 = new_fib
        i = i + SecretInteger(1)
    
    # Compute the golden ratio as the ratio of the last two Fibonacci numbers
    golden_ratio = fib2 / fib1
    
    # Return the computed golden ratio as the output
    return [Output(golden_ratio, "golden_ratio_output", party=party1)]

# Note: This code defines the structure and computation for the Nada program.
# It doesn't execute the program itself; execution would occur within the Nillion Network environment.
