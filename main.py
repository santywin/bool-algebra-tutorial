# Boolean Algebra Demonstrations

This file contains interactive demonstrations for various concepts in Boolean Algebra.

## Concepts Covered:
1. **AND Operation**
2. **OR Operation**
3. **NOT Operation**
4. **NAND Operation**
5. **NOR Operation**
6. **XOR Operation**
7. **XNOR Operation**

## Interactive Demonstrations:

### 1. AND Operation
```python
def AND(a, b):
    return a and b

print("AND Operation")
a = True
b = False
print(f'{a} AND {b} = {AND(a, b)}')  # Output: False
```

### 2. OR Operation
```python

def OR(a, b):
    return a or b

print("OR Operation")
a = True
b = False
print(f'{a} OR {b} = {OR(a, b)}')  # Output: True
```

### 3. NOT Operation
```python

def NOT(a):
    return not a

print("NOT Operation")
a = True
print(f'NOT {a} = {NOT(a)}')  # Output: False
```

### 4. NAND Operation
```python

def NAND(a, b):
    return not (a and b)

print("NAND Operation")
a = True
b = True
print(f'{a} NAND {b} = {NAND(a, b)}')  # Output: False
```

### 5. NOR Operation
```python

def NOR(a, b):
    return not (a or b)

print("NOR Operation")
a = False
b = False
print(f'{a} NOR {b} = {NOR(a, b)}')  # Output: True
```

### 6. XOR Operation
```python

def XOR(a, b):
    return a ^ b

print("XOR Operation")
a = True
b = False
print(f'{a} XOR {b} = {XOR(a, b)}')  # Output: True
```

### 7. XNOR Operation
```python

def XNOR(a, b):
    return not (a ^ b)

print("XNOR Operation")
a = True
b = True
print(f'{a} XNOR {b} = {XNOR(a, b)}')  # Output: True
```

# Conclusion
This file provides a simple yet effective demonstration of the basic operations in Boolean Algebra. 
