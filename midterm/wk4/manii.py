from utilities.calculator import add as add, subtract as minus, multiply as multiply, divide as divide
from utilities.st_op import reverse_string, capitalize_string, lowercase_string, uppercase_string

print("Using calculator.py:")
print("Addition:", add(10, 5))
print("Subtraction:", minus(10, 5))
print("Multiplication:", multiply(10, 5))
print("Division:", divide(10, 5))

sample_string = "hello World"
print("\nUsing string_operations.py:")
print("Original:", sample_string)
print("Reversed:", reverse_string(sample_string))
print("Capitalized:", capitalize_string(sample_string))
print("Lowercase:", lowercase_string(sample_string))
print("Uppercase:", uppercase_string(sample_string))
