class form_one():
    #declare a method that will store the variable
    def __init__(self, student_names):
        self.student_names = []

    def get_students(self, student_names):
        for student in self.student_names:
            student
        print (student)

my_class = ['Dickson', 'Sanderson', 'Flora', 'Scaver']
current_form_one = form_one(my_class)
current_form_one.get_students(my_class)