import time
import sys

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
    print("Welcome to the \"Kaggle-Python\" searching system, you can search for the explaination of each part in the \"Python\" course.")
    exercises = {"1":e1, "2":e2, "3":e3, "4":e4, "5":e5, "6":e6, "7":e7}
    tutorials = {"1":t1, "2":t2, "3":t3, "4":t4, "5":t5, "6":t6, "7":t7}
    ans = input("\nWhich do you want? Tutorials or exercises?(e/t)")
    if ans == "t":
        num = input("\nWhich lesson?(1~7)")
        tutorials[num].entry()
    elif ans == "e":
        num = input("\nWhich lesson?(1~7)")
        exercises[num].entry()
    else:
        print("\nI\'m sorry, I think there is nothing like it in my project.")
        print("\nPlease find it somewhere else...")
    print("\nThanks for using my \"Kaggle-Python\" searching system!!")
    time.sleep(1)
    sys.exit()


if __name__ == "__main__":
    main()