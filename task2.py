from data import subjects, teachers

class Teacher:
    def __init__(self, first_name, last_name, age, email, can_teach_subjects):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.can_teach_subjects = can_teach_subjects
        self.assigned_subjects = set()

    def __repr__(self):
        return f"{self.first_name} {self.last_name}, {self.age} років, email: {self.email}"

def create_schedule(subjects, teachers):
    remaining_subjects = subjects.copy()
    schedule = []

    while remaining_subjects:
        best_teacher = None
        subjects_covered = set()

        for teacher in teachers:
            teachable_subjects = teacher['can_teach_subjects'] & remaining_subjects
            if len(teachable_subjects) > len(subjects_covered) or (
                len(teachable_subjects) == len(subjects_covered) and
                (best_teacher is None or teacher['age'] < best_teacher['age'])
            ):
                best_teacher = teacher
                subjects_covered = teachable_subjects

        if not best_teacher:
            return None

        teacher_obj = Teacher(best_teacher['first_name'], best_teacher['last_name'],
                              best_teacher['age'], best_teacher['email'], best_teacher['can_teach_subjects'])
        teacher_obj.assigned_subjects = subjects_covered
        schedule.append(teacher_obj)
        remaining_subjects -= subjects_covered

    return schedule

if __name__ == '__main__':
    schedule = create_schedule(subjects, teachers)

    if schedule:
        print("Розклад занять:")
        for teacher in schedule:
            print(f"{teacher.first_name} {teacher.last_name}, {teacher.age} років, email: {teacher.email}")
            print(f"   Викладає предмети: {', '.join(teacher.assigned_subjects)}\n")
    else:
        print("Неможливо покрити всі предмети наявними викладачами.")
