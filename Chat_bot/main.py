
import csv
from dotenv import load_dotenv
import os

from chatbot import ChatBot


load_dotenv()

BOT_NAME = os.getenv("BOT_NAME", "PythonBot")



bot = ChatBot(BOT_NAME)


def analyze_students():
    required_columns = ["name", "python", "math", "english"]
    file_path = os.path.join(os.path.dirname(__file__), "students.csv")

    try:
        with open(file_path, "r", newline="", encoding="utf-8-sig") as file:
            reader = csv.DictReader(
                line for line in file if line.strip()
            )

            if reader.fieldnames is None:
                print("students.csv is empty or does not contain a header row.")
                return

            reader.fieldnames = [
                (header or "").strip().lower()
                for header in reader.fieldnames
            ]

            missing_columns = []
            for column in required_columns:
                if column not in reader.fieldnames:
                    missing_columns.append(column)

            if missing_columns:
                print(
                    "Missing required columns in students.csv: "
                    + ", ".join(missing_columns)
                )
                return

            students = []

            for row_number, row in enumerate(reader, start=2):
                if all(
                    value is None or str(value).strip() == ""
                    for value in row.values()
                ):
                    continue

                try:
                    name = row["name"].strip()
                    if not name:
                        raise ValueError("student name is empty")

                    marks = []
                    for subject in required_columns[1:]:
                        mark = row[subject]
                        if mark is None or not mark.strip():
                            raise ValueError(f"{subject} mark is empty")
                        marks.append(int(mark.strip()))

                except (AttributeError, TypeError, ValueError) as e:
                    print(
                        f"Skipping invalid data on CSV row {row_number}: {e}"
                    )
                    continue

                average = sum(marks) / len(marks)

                student = {
                    "name": name,
                    "average": average,
                    "highest": max(marks),
                    "lowest": min(marks)
                }

                students.append(student)

        if not students:
            print("No student records found.")
            return

        print("\n========== STUDENT SUMMARY ==========")

        for student in students:
            print(f"\nName: {student['name']}")
            print(f"Average: {student['average']:.2f}")
            print(f"Highest mark: {student['highest']}")
            print(f"Lowest mark: {student['lowest']}")

        class_averages = [
            student["average"] for student in students
        ]

        print("\n========== CLASS SUMMARY ==========")
        print(f"Students: {len(students)}")
        print(f"Class average: {sum(class_averages) / len(class_averages):.2f}")
        print(f"Highest average: {max(class_averages):.2f}")
        print(f"Lowest average: {min(class_averages):.2f}")

    except FileNotFoundError:
        print("students.csv file not found.")

    except OSError as e:
        print("File error:", e)

    except UnicodeError as e:
        print("Could not read students.csv as UTF-8:", e)

    except csv.Error as e:
        print("Invalid CSV data in students.csv:", e)



def start_chat():

    print("=" * 40)
    print(f"Welcome! I am {BOT_NAME}")
    print("Type 'bye' to exit.")
    print("Type 'history' to see old chats.")
    print("Type 'students' to analyze marks.")
    print("=" * 40)

    while True:

        user_message = input("\nYou: ").strip()

        if not user_message:
            print("Please type something.")
            continue

        # exit
        if user_message.lower() == "bye":
            bot.add_message("user", user_message)

            reply = "Goodbye! Have a nice day."
            print(f"{BOT_NAME}: {reply}")

            bot.add_message("bot", reply)
            break

        # history
        elif user_message.lower() == "history":
            bot.show_history()
            continue


        elif user_message.lower() == "students":
            analyze_students()
            continue


        else:
            bot.add_message("user", user_message)

            reply = bot.get_reply(user_message)

            print(f"{BOT_NAME}: {reply}")

            bot.add_message("bot", reply)



if __name__ == "__main__":
    start_chat()
