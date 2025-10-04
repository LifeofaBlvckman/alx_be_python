def safe_divide(numerator, denominator):
    try:
        # Try to convert inputs to floats
        num = float(numerator)
        den = float(denominator)
        
        # Try to perform division
        result = num / den
        return f"The result of the division is {result}"
        
    except ValueError:
        return "Error: Please enter numeric values only."
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
