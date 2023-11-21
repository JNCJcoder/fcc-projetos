import re


def arithmetic_arranger(problems, solution=False):
  if len(problems) > 5:
    return "Error: Too many problems."

  lineOne = "  "
  lineTwo = ""
  lineThree = "--"
  lineFour = ""

  count = 1

  for question in problems:
    splitQuestion = re.split("\s", question)

    if not splitQuestion[0].isdigit():
      return "Error: Numbers must only contain digits."

    if not splitQuestion[2].isdigit():
      return "Error: Numbers must only contain digits."

    numberOne = int(splitQuestion[0])
    numberTwo = int(splitQuestion[2])

    numberOneDigits = len(str(numberOne))
    numberTwoDigits = len(str(numberTwo))

    if numberOneDigits > 4 or numberTwoDigits > 4:
      return "Error: Numbers cannot be more than four digits."

    maxDigit = max(numberOneDigits, numberTwoDigits)

    operator = splitQuestion[1]

    if operator == '+':
      result = numberOne + numberTwo
    elif operator == '-':
      result = numberOne - numberTwo
    else:
      return "Error: Operator must be '+' or '-'."

    resultDigit = len(str(result))

    lineOne += " " * (maxDigit - numberOneDigits) + str(numberOne)
    lineTwo += operator + " " + " " * (maxDigit -
                                       numberTwoDigits) + str(numberTwo)
    lineThree += "-" * maxDigit
    lineFour += " " * ((maxDigit + 2) - resultDigit) + str(result)

    if count < len(problems):
      lineOne += " " * 4 + "  "
      lineTwo += " " * 4
      lineThree += " " * 4 + "--"
      lineFour += " " * 4

    count = count + 1

  arranged_problems = lineOne.rstrip()
  arranged_problems += "\n" + lineTwo.rstrip()
  arranged_problems += "\n" + lineThree.rstrip()

  if solution == True:
    arranged_problems += "\n" + lineFour.rstrip()

  return arranged_problems
