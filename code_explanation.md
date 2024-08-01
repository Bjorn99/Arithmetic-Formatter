```markdown
# Arithmetic Formatter: Detailed Code Explanation

## Overview
The `arithmetic_arranger` function formats a list of arithmetic problems vertically and side-by-side. It handles various input errors and can optionally display the answers to the problems.

## Function Definition
```python
def arithmetic_arranger(problems, show_answers=False):
```
- **Parameters**:
  - `problems`: A list of strings, each representing an arithmetic problem (e.g., "32 + 698").
  - `show_answers`: An optional boolean (default is `False`). If `True`, the function will display the answers.

## Error Checking for Problem Count
```python
if len(problems) > 5:
    return 'Error: Too many problems.'
```
- Checks if the number of problems exceeds five. If true, returns an error message.

## Initialization of Lists
```python
first_line = []
second_line = []
dashes = []
answers = []
```
- Creates four empty lists to store different parts of the formatted output:
  - `first_line`: Holds the first operands.
  - `second_line`: Holds the operators and second operands.
  - `dashes`: Holds the lines of dashes for each problem.
  - `answers`: Holds computed answers if `show_answers` is `True`.

## Looping Through Each Problem
```python
for problem in problems:
```
- Starts a loop that iterates over each problem in the `problems` list.

## splitting the Problem
```python
parts = problem.split()
```
- Splits the problem string into its components based on whitespace (e.g., "32 + 698" becomes `['32', '+', '698']`).

## Validation of Problem Format
```python
if len(parts) != 3:
    return 'Error: Invalid problem format.'
```
- Checks if the split parts do not equal three. If true, returns an error message.

## Unpacking the Parts
```python
num1, operator, num2 = parts
```
- Assigns the components of `parts` to `num1`, `operator`, and `num2`.

## Validation of Operator
```python
if operator not in ('+', '-'):
    return "Error: Operator must be '+' or '-'."
```
- Checks if the operator is either '+' or '-'. If not, returns an error message.

## Validation of Operands
```python
if not (num1.isdigit() and num2.isdigit()):
    return 'Error: Numbers must only contain digits.'
```
- Checks if both operands consist only of digits. If not, returns an error message.

## Validation of Operand Length
```python
if len(num1) > 4 or len(num2) > 4:
    return 'Error: Numbers cannot be more than four digits.'
```
- Checks if either operand has more than four digits. If true, returns an error message.

## Calculating Width for Formatting
```python
width = max(len(num1), len(num2)) + 2
```
- Calculates the width needed for formatting, including space for the operator and an extra space.

## Right-Aligning the First Operand
```python
first_line.append(num1.rjust(width))
```
- Right-aligns `num1` within a string of `width` characters and adds it to `first_line`.

## Formatting the Second Operand
```python
second_line.append(operator + ' ' + num2.rjust(width - 2))
```
- Constructs the second line by concatenating the operator, a space, and the right-aligned second operand, and adds it to `second_line`.

## Creating the Dash Line
```python
dashes.append('-' * width)
```
- Creates a string of dashes that matches the calculated width and adds it to `dashes`.

## Calculating Answers (if needed)
```python
if show_answers:
    if operator == '+':
        answer = str(int(num1) + int(num2))
    else:
        answer = str(int(num1) - int(num2))
    answers.append(answer.rjust(width))
```
- If `show_answers` is `True`, calculates the answer based on the operator and appends it to the `answers` list.

## Joining Lines for Output
```python
arranged_problems = '\n'.join(['    '.join(line) for line in [first_line, second_line, dashes]])
```
- Joins the formatted lines with four spaces in between and creates the final output string.

## Appending Answers (if needed)
```python
if show_answers:
    arranged_problems += '\n' + '    '.join(answers)
```
- If `show_answers` is `True`, appends the answers to the arranged problems.

## Returning the Result
```python
return arranged_problems
```
- Returns the complete string containing the formatted arithmetic problems and their answers (if applicable).

## Example Usage
You can call the function with various inputs to see how it formats the arithmetic problems. For example:
```python
print(arithmetic_arranger(["32 + 698", "1 - 9380"], True))
```
This will output the problems formatted vertically along with their answers.
