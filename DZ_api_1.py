import requests

class Categories_and_joke():
    """Создание шуток по категориям"""

    def __init__(self):
        pass

    def output_categories_and_joke(self):
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
        print(f"\nВсего категорий: {len(categories)}")

        """Вывод шуток по каждой категории"""
        print("\nШутки по каждой категории:")
        for i, category in enumerate(categories, 0):
            print(f"\n{i+1} Категория: {category[0].upper()+category[1:].lower()}")
            joke = "https://api.chucknorris.io/jokes/random?category="+str(categories[i])
            i+=1
            print("Статус код :" + str(result.status_code))
            assert 200 == result.status_code
            result = requests.get(joke)
            result.encodinq = 'utf-8'
            print(result.text)
            joke = result.json()
            print(f"Шутка: {joke['value']}")
        print(f"\nКатегории шуток закончились")
        print(f"\nУспешно!!! Мы получили шутки по каждой категории")

categories=Categories_and_joke()
categories.output_categories_and_joke()

