def add_item_to_dict(dictionary, key, value):
    # 원본 딕셔너리를 변경하지 않기 위해 복사본을 만듭니다.
    new_dict = dictionary.copy()
    
    # 복사된 딕셔너리에 새로운 키와 값을 추가합니다.
    new_dict[key] = value
    
    # 새로운 딕셔너리를 반환합니다.
    return new_dict


my_dict = {'name': 'Alice', 'age': 25}
result = add_item_to_dict(my_dict, 'country', 'USA')
print(result)
