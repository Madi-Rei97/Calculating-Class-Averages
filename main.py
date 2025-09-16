def calculate_class_averages(classrooms):
    class_averages = {}

    for subject, students in classrooms.items():
        if not students:
                class_averages[subject] = 0
                continue

        count_of_scores = 0
        total_scores = 0

        for scores in students.values():
            count_of_scores += len(scores)

            for score in scores:
                total_scores += score

        class_averages[subject] = total_scores / count_of_scores

    return class_averages