class Category:

  def __init__(self, name):
    self.ledger = []
    self.name = name
    self.balance = 0.0

  def __str__(self):
    header = self.name.center(30, "*") + '\n'
    categoryList = ""

    for item in self.ledger:
      lineDescription = "{:<23}".format(item["description"])
      lineAmount = "{:>7.2f}".format(item["amount"])
      categoryList += f'{lineDescription[:23]}{lineAmount[:7]}\n'

    total = "Total: {:.2f}".format(self.balance)

    return header + categoryList + total

  def deposit(self, amount, description=""):
    self.ledger.append({"amount": amount, "description": description})
    self.balance += amount

  def withdraw(self, amount, description=""):
    if self.balance - amount >= 0:
      self.ledger.append({"amount": -1 * amount, "description": description})
      self.balance -= amount

      return True
    else:
      return False

  def get_balance(self):
    return self.balance

  def check_funds(self, amount):
    return self.balance >= amount

  def transfer(self, amount, category):
    if self.check_funds(amount):
      self.withdraw(amount, "Transfer to " + category.name)
      category.deposit(amount, "Transfer from " + self.name)

      return True
    else:
      return False


def create_spend_chart(categories):
  header = "Percentage spent by category\n"
  totals = []
  descriptions = []
  descriptionAjusted = []
  descriptionsLength = []
  spentPercentage = []
  maxLength = 0
  categoryList = ""

  for category in categories:
    descriptions.append(category.name)
    descriptionsLength.append(len(category.name))
    spent = 0
    for item in category.ledger:
      if item["amount"] < 0:
        spent += abs(item["amount"])
    totals.append(round(spent, 2))

  total = round(sum(totals), 2)
  maxLength = max(descriptionsLength)

  for value in totals:
    spentPercentage.append(int((((value / total) * 10) // 1) * 10))

  for value in reversed(range(0, 101, 10)):
    categoryList += str(value).rjust(3) + '|'
    for percent in spentPercentage:
      if percent >= value:
        categoryList += " o "
      else:
        categoryList += "   "
    categoryList += " \n"

  for description in descriptions:
    descriptionAjusted.append(description.ljust(maxLength))

  footer = "    " + "-" * ((3 * len(categories)) + 1) + '\n'

  for x in zip(*descriptionAjusted):
    footer += "    " + "".join(map(lambda s: s.center(3), x)) + " \n"

  return (header + categoryList + footer).rstrip('\n')
