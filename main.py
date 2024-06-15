import Lesson1.exercise as e1
import Lesson2.exercise as e2
import Lesson3.exercise as e3
import Lesson4.exercise as e4
import Lesson5.exercise as e5
import Lesson6.exercise as e6
import Lesson7.exercise as e7
import Lesson1.tutorial as t1
import Lesson2.tutorial as t2
import Lesson3.tutorial as t3
import Lesson4.tutorial as t4
import Lesson5.tutorial as t5
import Lesson6.tutorial as t6
import Lesson7.tutorial as t7

def main():
    exercises = [e1, e2, e3, e4, e5, e6, e7]
    tutorials = [t1, t2, t3, t4, t5, t6, t7]
    for exer in exercises:
        exer.entry()
    for tuto in tutorials:
        tuto.entry()


if __name__ == "__main__":
    main()