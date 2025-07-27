def student_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key.capitalize()}: {value}")

student_info(name="sejal", age=17, roll_number="h240536")