from pathlib import Path

def get_cats_info(path):
    if Path(path).exists():
        with open(path, "r", encoding='utf-8') as file: # opening a file
            raw_lines= file.readlines() # extracting lines from the file 
            lines = [el.strip() for el in raw_lines] # removing /n from the lines 
            cats=[] # creating an empty dict 
            for el in lines: # iterating through each line in lines 
                cat={} # creating a dict for each cat
                id=el.split(',')[0] # assigning first element fo id
                name = el.split(',')[1] # assigning second element fo name
                age = el.split(',')[2] # assigning third element fo age
                cat["id"]=id # adding id value with "id" key to our previously created dict 
                cat["name"]=name  # adding name value with "name" key to our previously created dict 
                cat["age"] = age  # adding age value with "age" key to our previously created dict 
                cats.append(cat) # adding each dict with cat info to our list 
            return cats
    else:
        print(f"The file with path {path} cannot be found")
        return 1
    
if __name__ == "__main__": 
    cats_info = get_cats_info("cats.txt")
    print(cats_info) 