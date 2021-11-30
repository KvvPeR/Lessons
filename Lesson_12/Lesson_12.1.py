def typing(arr_models, arr_empty):
    while arr_models:
        print(arr_models)
        item=arr_models.pop()
        arr_empty.append(item)
        print(arr_empty)

#Основной код
arr_models=['Чехол', 'Пенал', 'Ручка', 'Кирпич']
arr_empty=[]
typing(arr_models, arr_empty)