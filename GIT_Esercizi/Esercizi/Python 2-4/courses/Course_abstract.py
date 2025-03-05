from abc import ABC
from abc import abstractmethod
from courses.course import Student
class CourseAB(ABC):
    def __init__(self) -> None:
        super().__init__()
    @abstractmethod
    def register_student(self, student: Student):
        for group in self.groups:
            pass
