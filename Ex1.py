class Students:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks  

    def get_average(self):
        sum_marks = sum(self.marks)
        average = sum_marks / len(self.marks)
        return average

s1 = Students("John", [90, 85, 76])
print("Hello", s1.name, "Your Average Marks is :", s1.get_average())

#We can do this also by this code!

class Students:
    def __init__(self, name, sub1, sub2, sub3):
        self.name = name
        self.sub1 = sub1  # Assuming that 'sub1' is the marks of the first subject
        self.sub2 = sub2  # Assuming that 'sub2' is the marks of the second subject
        self.sub3 = sub3  # Assuming that 'sub3' is the marks of the third subject

    def get_total(self):
        total = self.sub1 + self.sub2 + self.sub3
        return total

    def get_Average(self):
        avg = self.get_total() / 3
        return avg

s1 = Students("John", 90, 85, 76)
print("Hello", s1.name, "Your Average Marks is :", s1.get_Average())




  
