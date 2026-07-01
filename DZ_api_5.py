import requests
import json
import urllib3

"""Создание списка имён из фильмов с Darth Vader"""
class Star_Wars():
    @staticmethod
    def films_darth_vader():
        """Получение списка полей из персонажа"""
        url_darth = "https://swapi.info/api/people/4/"
        print(f"\nURL персонажа: {url_darth}\n")
        result = requests.get(url_darth, verify=False)
        fields = json.loads(result.text)
        print(f"Список полей персонажа: \n{list(fields)}")
        film = result.json()
        films_info = film.get('films')
        print(f"\nСсылки на фильмы: \n{films_info}")

        """Получение списка полей из фильма"""
        url_film = "https://swapi.info/api/films/1/"
        print(f"\nURL фильма: {url_film}\n")
        result_film = requests.get(url_film, verify=False)
        fields_film = json.loads(result_film.text)
        print(f"Список полей \"film\": \n{list(fields_film)}\n")

        """Получение списка персонажей из фильмов и записание их в файл"""
        movie_character = str()
        for film in films_info:
            result_film = requests.get(film, verify=False)
            film = result_film.json()
            for characters_url in film['characters']:
                result_characters = requests.get(characters_url, verify=False)
                name_characters = result_characters.json()
                movie_character += f"{name_characters['name']} \n"
                print(f"Обновлен список персонажей:\n{movie_character}")

            with open('movie_character.txt', 'a', encoding='utf-8') as file:
                file.writelines(movie_character)
        print(f"Все персонажи из фильмов добавлены!")

        """Чтеине файла и удаление повторяющих персонажей"""
        with open('movie_character.txt', 'r', encoding='utf-8') as file:
            lines = set(file.readlines())

        """Обновление файла"""
        with open('movie_character.txt', 'w', encoding='utf-8') as file:
            file.writelines(lines)

        print(f"\nФайл \"movie_character\" с персонажами записан!")

urllib3.disable_warnings()
films_darth = Star_Wars()
films_darth.films_darth_vader()


