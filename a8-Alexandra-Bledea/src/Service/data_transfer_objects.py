

class AverageStudentsStatistic:

    def __init__(self, student_id_a, student_name_a, discipline_id_a, discipline_name_a, average_a):
        """
        :param student_id_a: the id of the student
        :param student_name_a: the name of the student
        :param discipline_id_a: the id of the discipline
        :param discipline_name_a: the name of the discipline
        :param average_a: the average grade which a student have at each discipline at which he received grades
        """
        self._student_id_a = student_id_a
        self._student_name_a = student_name_a
        self._discipline_id_a = discipline_id_a
        self._discipline_name_a = discipline_name_a
        self._average_a = average_a

    @property
    def student_id_a(self):
        return self._student_id_a

    @property
    def student_name_a(self):
        return self._student_name_a

    @property
    def discipline_id_a(self):
        return self._discipline_id_a

    @property
    def discipline_name_a(self):
        return self._discipline_name_a

    @property
    def average_a(self):
        return self._average_a

    def __str__(self):
        """
        :return: the string form of the statistic
        """
        return str(self.student_id_a).rjust(7) + ' | ' + str(self.student_name_a).rjust(20) + ' | ' \
               + str(self.discipline_id_a).rjust(9) + ' | ' + str(self.discipline_name_a).rjust(20) + ' | ' \
               + str(format(self.average_a, ".3f")).rjust(5)


class AverageDisciplineStatistic:

    def __init__(self, discipline_id_a, discipline_name_a, average_a):
        """
        :param discipline_id_a: represents the id of the discipline
        :param discipline_name_a: represents the name of the discipline
        :param average_a: average grade
        """
        self._discipline_id_a = discipline_id_a
        self._discipline_name_a = discipline_name_a
        self._average_a = average_a

    @property
    def discipline_id_a(self):
        return self._discipline_id_a

    @property
    def discipline_name_a(self):
        return self._discipline_name_a

    @property
    def average_a(self):
        return self._average_a

    def __str__(self):
        """
        :return: the string form of the statistic
        """
        return str(self.discipline_id_a).rjust(9) + ' | ' + str(self.discipline_name_a).rjust(20) + ' | ' \
               + str(format(self.average_a, ".3f")).rjust(5)


class GeneralAverageStudentsStatistic:

    def __init__(self, student_id_ga, student_name_ga, average_ga):
        """
        :param student_id_ga: the id of the student
        :param student_name_ga: the student's name
        :param average_ga: general average of the student
        """
        self._student_id_ga = student_id_ga
        self._student_name_ga = student_name_ga
        self._average_ga = average_ga

    @property
    def student_id_ga(self):
        return self._student_id_ga

    @property
    def student_name_ga(self):
        return self._student_name_ga

    @property
    def average_ga(self):
        return self._average_ga

    def __str__(self):
        """
        :return: the string form of the statistic
        """
        return str(self.student_id_ga).rjust(7) + ' | ' + str(self.student_name_ga).rjust(20) + ' | ' \
               + str(format(self.average_ga, ".3f")).rjust(5)
