classroom = ["Michael", "Sahil", "Laethe", "Owen","Isaiah"]
def rollcall(student_name):
    return "is " + student_name + " in the class?"
for student in classroom:
    print(rollcall(student))