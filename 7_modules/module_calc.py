def add(a,b):
	return (a+b)

def sub(a,b):
	return (a-b)
	
def mul(a,b):
	return (a*b)
	
def div(a, b):
    if b == 0:  # Handling division by zero error
        return "Division by zero is not allowed"
    return a / b  # Use `/` for floating-point division
