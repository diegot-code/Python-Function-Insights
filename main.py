
def main():
    # Function with Local Variable
    def add_numbers(a, b):
        result = a + b
        return result

    # Example usage:
    sum_result = add_numbers(3, 5)
    print(sum_result)

    # Function with Default Parameter
    def greet(name, greeting="Hello"):
        message = f"{greeting}, {name}!"
        return message

    # Example usage:
    greeting_message = greet("Alice")
    print(greeting_message)

    # Function with Local and Global Variables
    global_var = 10

    def multiply_by_global(num):
        local_var = 5
        result = num * local_var * global_var
        return result

    # Example usage:
    product = multiply_by_global(2)
    print(product)

    # Function with Variable Number of Parameters
    def calculate_sum(*args):
        total = sum(args)
        return total

    # Example usage:
    result_sum = calculate_sum(1, 2, 3, 4, 5)
    print(result_sum)

    # Function with Local and Parameter Variables
    def power(base, exponent):
        result = base ** exponent
        message = f"{base} raised to the power of {exponent} is {result}"
        return message

    # Example usage:
    power_message = power(2, 3)
    print(power_message)




if __name__ == "__main__":
    main()