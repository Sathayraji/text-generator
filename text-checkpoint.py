{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "class grade_calculator:\n",
    "   def __init__(self):\n",
    "      self.__roll_number = 0\n",
    "      self._Name = \"\"\n",
    "      self.__marks_obtained = []\n",
    "      self.__total_marks = 0\n",
    "      self.__percentage = 0\n",
    "      self.__grade = \"\"\n",
    "      self.__result = \"\"\n",
    "   def setgrade_calculator(self):\n",
    "      self.__roll_number = int(input(\"Enter Roll Number: \"))\n",
    "      self.__Name = input(\"Enter Name: \")\n",
    "      print(\"Enter 5 subjects marks: \")\n",
    "      for n in range(5):\n",
    "         self.__marks_obtained.append(int(input(\"Subject \" + str(n + 1) + \": \")))\n",
    "   def Total(self):\n",
    "      for i in self.__marks_obtained:\n",
    "         self.__total_marks += i\n",
    "   def Percentage(self):\n",
    "      self.__percentage = self.__total_marks / 5\n",
    "   def calculateGrade(self):\n",
    "      if self.__percentage >= 90:\n",
    "         self.__grade = \"0\"\n",
    "      elif self.__percentage >= 80:\n",
    "         self.__grade = \"A+\"\n",
    "      elif self.__percentage >= 70:\n",
    "         self.__grade = \"A\"\n",
    "      elif self.__percentage >= 60:\n",
    "         self.__grade = \"B+\"\n",
    "      elif self.__percentage >= 50:\n",
    "         self.__grade = \"B\"\n",
    "      elif self.__percentage >= 40:\n",
    "         self.__grade = \"C\"\n",
    "      else:\n",
    "         self.__grade = \"F\"\n",
    "   def Result(self):\n",
    "      count = 0\n",
    "      for x in self.__marks_obtained:\n",
    "         if x >= 40:\n",
    "            count += 1\n",
    "      if count == 5:\n",
    "         self.__result = \"PASS\"\n",
    "      elif count >= 3:\n",
    "         self.__result = \"COMP.\"\n",
    "      else:\n",
    "         self.__result = \"FAIL\"\n",
    "   def showgrade_calculator(self):\n",
    "      self.Total()\n",
    "      self.Percentage()\n",
    "      self.calculateGrade()\n",
    "      self.Result()\n",
    "      print(self.__roll_number, \"\\t\", self.__Name, \"\\t\", self.__total_marks, \"\\t\",          self.__percentage, \"\\t\", self.__grade, \"\\t\",\n",
    "         self.__result)\n",
    "def main():\n",
    "   gc = grade_calculator()\n",
    "   gc.setgrade_calculator()\n",
    "   gc.showgrade_calculator()\n",
    "if __name__ == \"__main__\":\n",
    "   main()"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
