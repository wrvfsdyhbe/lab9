def add(a,b):
    return a + b
def test_add_success():
    assert add(2,3) == 5
def test_add_wrong():
    assert add (2,2) != 5
def get_user_age():
    try:
        age = int(input("Введите ваш возраст: "))
        print(f"ваш возраст:{age}")
    except ValueError:
        print("Ошибка!!! ПОжалуйста введите только числа, а не буквы.")
if __name__=="__main__":
    get_user_age()