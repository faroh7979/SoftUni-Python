from unittest import TestCase, main
from project.student import Student


class TestStudent(TestCase):

    def setUp(self):
        self.student_with_c = Student('Klopp', {'Tactic': ['defense', 'offense']})
        self.student = Student('Guardiola')

    def test_correct_initialisation(self):
        self.assertEqual("Klopp", self.student_with_c.name)
        self.assertEqual({'Tactic': ['defense', 'offense']}, self.student_with_c.courses)
        self.assertEqual({}, self.student.courses)

    def test_updating_existing_course_expect_to_adding_new_notes(self):
        result = self.student_with_c.enroll('Tactic', ['Set-pieces', 'Mental'])
        expected_updated_notes = ['defense', 'offense', 'Set-pieces', 'Mental']

        self.assertEqual(result, "Course already added. Notes have been updated.")
        self.assertEqual(expected_updated_notes, self.student_with_c.courses['Tactic'])

    def test_adding_new_course_with_yes_note_expect_to_adding_it(self):
        result = self.student_with_c.enroll('Motivation', ['fun', 'party'], 'Y')
        expected_final_course_state = {'Tactic': ['defense', 'offense'], 'Motivation': ['fun', 'party']}

        self.assertEqual(result, "Course and course notes have been added.")
        self.assertEqual(expected_final_course_state, self.student_with_c.courses)

    def test_adding_new_course_with_blank_note_expect_to_adding_it(self):
        result = self.student_with_c.enroll('Motivation', ['fun', 'party'])
        expected_final_course_state = {'Tactic': ['defense', 'offense'], 'Motivation': ['fun', 'party']}

        self.assertEqual(result, "Course and course notes have been added.")
        self.assertEqual(expected_final_course_state, self.student_with_c.courses)

    def test_adding_new_course_with_no_concrete_note_expect_to_adding_it_with_no_notes(self):
        result = self.student_with_c.enroll('Motivation', ['fun', 'party'], 'N')
        expected_final_course_state = {'Tactic': ['defense', 'offense'], 'Motivation': []}

        self.assertEqual(result, "Course has been added.")
        self.assertEqual(expected_final_course_state, self.student_with_c.courses)

    def test_adding_note_for_existing_course_expect_to_add_it(self):
        result = self.student_with_c.add_notes('Tactic', ['corner', 'penalty'])
        expected_final_course_state = {'Tactic': ['defense', 'offense', ['corner', 'penalty']]}

        self.assertEqual(result, "Notes have been updated")
        self.assertEqual(expected_final_course_state, self.student_with_c.courses)

    def test_adding_note_for_non_existing_course_expect_to_raise_exception(self):

        with self.assertRaises(Exception) as ex:
            self.student_with_c.add_notes('Motivation', ['fun', 'party'])

        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))

    def test_leave_course_when_it_is_enrolled_expect_to_leave_it(self):
        result = self.student_with_c.leave_course('Tactic')
        expected_final_course_state = {}

        self.assertEqual(result, "Course has been removed")
        self.assertEqual(expected_final_course_state, self.student_with_c.courses)

    def test_leave_course_when_it_is_not_enrolled_expect_to_raise_exception(self):

        with self.assertRaises(Exception) as ex:
            self.student_with_c.leave_course('Motivation')

        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))


if __name__ == '__main__':
    main()
