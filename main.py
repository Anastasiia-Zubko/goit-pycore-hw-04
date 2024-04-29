from salary_calculator import total_salary
from cats_processing import get_cats_info
from directory_visualisation import print_directory
from cli import main
from pathlib import Path


print("Task 1:\n")
total, average = total_salary("salaries.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")

print("\nTask 2:\n")
cats_info = get_cats_info("cats.txt")
print(cats_info)

print("\nTask 3:\n")
path = Path("/Users/anastasiiazubko/Python/goit-pycore-hw-04")
print(f"Structure of directory with path: {path}\n")
print_directory(path)

print("\nTask 4:\n")

main()