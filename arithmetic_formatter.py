def arithmetic_arranger(problems, show_answers = False):
    # Check for too many problems
    if len(problems) > 5:
        return 'Error: Too many problems.'

    # Lists holding the formatted parts of the problems
    first_line = []
    second_line = []
    dashes = []
    answers = []

    for problem in problems:
        # divide the problem into unique components
        parts = problem.split()
        if len(parts) != 3:
            return 'Error: Invalid problem format.'

        num1, operator, num2 = parts

        # Validate the operands
        if not (num1.isdigit() and num2.isdigit()):
            return 'Error: Numbers must only contain digits.'

        if len(num1) > 4 or len(num2) > 4:
            return 'Error: Numnbers cannot be more than four digits.'

        # Calculate the width for formatting
        width = max(len(num1), len(num2)) + 2

        # Format each part
        # Format each part
        first_line.append(num1.rjust(width))
        second_line.append(operator + ' ' + num2.rjust(width - 2))
        dashes.append('-' * width)

        # Calculate the answer
        if show_answers:
            if operator == '+':
                answer = str(int(num1) + int(num2))
            else:
                answer = str(int(num1) - int(num2))
            answers.append(answer.rjust(width))
        
        # Join the lines and add four spaces between them
    arranged_problems = '\n'.join(['    '.join(line) for line in [first_line, second_line, dashes]])

    if show_answers:
        arranged_problems += '\n' + '    '.join(answers)

    return arranged_problems

print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')
arithmetic_arranger(["3801 - 2", "123 + 49"], True)