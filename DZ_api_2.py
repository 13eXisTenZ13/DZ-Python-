import requests

class Categories_and_joke():
    """Запрос от пользователя для получение шутки по категории"""

    def __init__(self):
        pass


    def output_categories_and_user_joke(self):
        dostup_cat=str("animal, career, celebrity, dev, explicit, fashion, food, history, money, movie, music, political, religion, science, sport, travel")
        print(f"Доступные категории шуток: \n{dostup_cat}")

        """Запрос у пользователя категории"""
        user_category=input("\nВведите категорию, на которую хотите получить шутку: ")

        """Вывод категорий шуток"""
        url = "https://api.chucknorris.io/jokes/categories"
        print(url)
        result = requests.get(url)
        print("Статус код :" + str(result.status_code))
        assert 200 == result.status_code
        print("Мы получили категории шуток")
        result.encodinq = 'utf-8'
        print(result.text)
        categories=result.json()
        print(f"Всего категорий: {len(categories)}")

        """Вывод шутки по запрошеной категории"""

        if user_category in categories:
            print("\nШутка по запрошеной категории")
            joke = "https://api.chucknorris.io/jokes/random?category="+str(user_category)
            print("Статус код :" + str(result.status_code))
            assert 200 == result.status_code
            result = requests.get(joke)
            result.encodinq = 'utf-8'
            print(result.text)
            
            """Вывод только шутки"""
            joke = result.json()
            print(f"\nШутка: {joke['value']}")
            print(f"\nУспешно!!! Мы получили шутку по выбранной категории")

        else:
            print("\nВы ввели несуществующую категорию.")

categories=Categories_and_joke()
categories.output_categories_and_user_joke()

