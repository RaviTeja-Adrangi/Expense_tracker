class Expense:
  def __init__(self,name,amount,category):
    self.name = name
    self.amount = amount
    self.category = category

  def __repr__(self) -> str:
    return f"<Expense : {self.name} , ₹{self.amount},{self.category} >"
  