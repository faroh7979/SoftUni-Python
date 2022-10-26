class Programmer:
    def __init__(self, name: str, language: str, skills: int):
        self.name = name
        self.language = language
        self. skills = skills

    def watch_course(self, course_name: str, new_language: str, skills_earned: int):

        if new_language == self.language:
            self.skills += skills_earned
            return f"{self.name} watched {course_name}"

        else:
            return f"{self.name} does not know {new_language}"

    def change_language(self, the_new_language: str, skills_needed: int):

        if self.skills >= skills_needed:

            if the_new_language != self.language:
                old_language = self.language
                self.language = the_new_language
                return f"{self.name} switched from {old_language} to {the_new_language}"

            else:
                return f"{self.name} already knows {the_new_language}"

        else:
            return f"{self.name} needs {skills_needed - self.skills} more skills"


programmer = Programmer("John", "Java", 50)
print(programmer.watch_course("Python Masterclass", "Python", 84))
print(programmer.change_language("Java", 30))
print(programmer.change_language("Python", 100))
print(programmer.watch_course("Java: zero to hero", "Java", 50))
print(programmer.change_language("Python", 100))
print(programmer.watch_course("Python Masterclass", "Python", 84))
