# Boolean Laws Demonstration

This module demonstrates various Boolean algebra laws with simple examples.

## Identity Law
- **A + 0 = A**
- **A \* 1 = A**

## Null Law
- **A + 1 = 1**
- **A \* 0 = 0**

## Idempotent Law
- **A + A = A**
- **A \* A = A**

## De Morgan's Law
- **¬(A + B) = ¬A \* ¬B**
- **¬(A \* B) = ¬A + ¬B**

## Commutative Law
- **A + B = B + A**
- **A \* B = B \* A**

## Associative Law
- **(A + B) + C = A + (B + C)**
- **(A \* B) \* C = A \* (B \* C)**

## Distributive Law
- **A \* (B + C) = A \* B + A \* C**
- **A + (B \* C) = (A + B) \* (A + C)**

## Absorption Law
- **A + (A \* B) = A**
- **A \* (A + B) = A**

# Example Usage

```python
# Define some boolean values
A = True
B = False

# Using Identity Law
identity_example = A or False  # Should return A (True)

# Using Null Law
null_example_or = A or True  # Should return True
null_example_and = A and False  # Should return False

# ..and so on for other laws.
```