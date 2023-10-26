class StudyTimetable:
    def __init__(self):
        self.days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
        self.courses = ['IT Y1', 'IT Y2', 'IT Y3', 'IT Y4']
        self.timetable = {day: {course: ['Class'] for course in self.courses} for day in self.days_of_week}

    def add_class(self, day, course, unit):
        if day in self.days_of_week and course in self.courses:
            self.timetable[day][course].append(unit)
            return True
        else:
            return False

    def get_timetable(self):
        return self.timetable

    def display_timetable(self):
        for day, courses in self.timetable.items():
            print(day)
            for course, units in courses.items():
                print(f"  {course}: {', '.join(units)}")

# Create a study timetable
timetable = StudyTimetable()

# Add classes to the timetable
timetable.add_class('Monday', 'IT Y1', 'Unit 1')
timetable.add_class('Monday', 'IT Y2', 'Unit 2')
timetable.add_class('Tuesday', 'IT Y1', 'Unit 3')
timetable.add_class('Tuesday', 'IT Y3', 'Unit 4')
timetable.add_class('Wednesday', 'IT Y2', 'Unit 5')
timetable.add_class('Wednesday', 'IT Y4', 'Unit 1')

# Display the timetable
timetable.display_timetable()
