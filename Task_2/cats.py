
def get_cats_info(path: str) :
    
    result = []
    try:
        with open(path,'r',encoding='utf-8') as file:
            while True:
                line = file.readline().strip()
                
                if not line:
                    break

                id,name,age = line.split(',') # preparation for cats maping :p
                result.append({
                    'id': id,
                    'name': name,
                    'age': age
                })        
        return result
    
    except FileNotFoundError:
        return 'No file Found'
    

print(get_cats_info('Task_2/cats.txt'))