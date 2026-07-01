import requests

class New_location():
    """Работа с новыми локациями и запись place_id в файл """

    def create_new_location_and_record_id(self):
        """Создание новых локаций"""
        place_id_all = str()
        for i in range(5):

            base_url = "https://rahulshettyacademy.com"
            key = "?key=qaclick123"
            post_resource = "/maps/api/place/add/json"

            """Создание новой локации"""
            post_url = base_url + post_resource + key
            print(post_url)
            json_for_new_location = {
                "location": {
                    "lat": -38.383494,
                    "lng": 33.427362
                }, "accuracy": 50,
                "name": "Frontline house",
                "phone_number": "(+91) 983 893 3937",
                "address": "29, side layout, cohen 09",
                "types": [
                    "shoe park",
                    "shop"
                ],
                "website": "http://google.com",
                "language": "French-IN"

            }

            result_post = requests.post(post_url, json = json_for_new_location)
            print(result_post.text)
            print("Статус код :" + str(result_post.status_code))
            assert 200 == result_post.status_code
            print("Создана новая локация!!!")

            check_post = result_post.json()
            place_id = check_post.get("place_id")
            print(f"Place_id новой локации: {place_id}")

            place_id_all+=place_id+'\n'
            print(place_id_all)

        """Запись id в файл"""
        fw = open('place_id.txt', 'w')
        fw.write(place_id_all)
        fw.close()
        print(f"\nВ файл записан новый id: {place_id_all}\n")


        """Чтение файла place_id"""
        fr = open('place_id.txt', 'r')
        place_id_text = fr.read()
        print(f"Содержимое файла place_id: \n{place_id_text}")
        fr.close()

        """Проверка создания новой локации по place_id из файла"""

        for n in range(5):
            get_resource = "/maps/api/place/get/json"
            get_url = base_url + get_resource + key + "&place_id=" + str(place_id_text.split()[n])
            print(get_url)
            result_get = requests.get(get_url)
            print(result_get.text)
            print("Статус код :" + str(result_get.status_code))
            assert 200 == result_get.status_code
            print("Проверка создания новой локации прошла успешно!!!\n")

new_place_id = New_location()
new_place_id.create_new_location_and_record_id()
