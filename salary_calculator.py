from pathlib import Path

def total_salary(path):
    
    if Path(path).exists():
        with open(path, "r", encoding='utf-8') as file: # opening a file
            raw_lines= file.readlines() # extracting lines from the file 
            lines = [el.strip() for el in raw_lines] # removing /n from the lines 
            salaries=[] # creating an empty list 
            for el in lines: # iterating through each line in lines 
                salary=el.split(',')[1] # since we know that salary is devided by a comma we can discard the coma and everything before
                salaries.append(int(salary)) # adding a salary to our previously created list converting it to a number
            total_sum = sum(salaries) # calculating total sum 
            avg_salary = sum(salaries) / len(salaries) # calculating average sum
            salary_info=[total_sum,avg_salary] # creating a list with total and average sum
            return tuple(salary_info) # returning total and average sums in a tuple
    else:
        print(f"The file with path {path} cannot be found")
        return 1


if __name__ == "__main__":  
    total, average = total_salary("salaries.txt")
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
    
    



