
import requests

class Delete_location():
    """Работа с новыми локациями и запись place_id в файл """

    def delete_location_and_record_id(self):
        """Путь локаций"""
        base_url = "https://rahulshettyacademy.com"
        key = "?key=qaclick123"

        """Чтение файла place_id"""
        fr = open('place_id.txt', 'r')
        place_id_text = fr.read()
        print(f"Содержимое файла place_id: \n{place_id_text}")
        fr.close()

        """Удаление выборочной локации"""
        for n in range(1,4,2):
            delete_resource = "/maps/api/place/delete/json"
            delete_url = base_url + delete_resource + key
            print(delete_url)
            json_for_delete_new_location = {
                "place_id": place_id_text.split()[n]
            }
            print(place_id_text.split()[n])
            result_delete = requests.delete(delete_url, json=json_for_delete_new_location)
            print(result_delete.text)
            print("Статус код :" + str(result_delete.status_code))
            assert 200 == result_delete.status_code
            print("Удаление новой локации прошла успешно!!!")
            check_status = result_delete.json()
            check_status_info = check_status.get("status")
            print("Сообщение: " + check_status_info)
            assert check_status_info == "OK"
            print("Сообщение верно")

            """Проверка удаления локаций по place_id из файла и отсеивание существующих"""
        place_id_left=str()
        place_id_delete=str()
        for n in range(5):
            get_resource = "/maps/api/place/get/json"
            get_url = base_url + get_resource + key + "&place_id=" + str(place_id_text.split()[n])
            print(get_url)
            result_get = requests.get(get_url)
            print(result_get.text)
            print("Статус код :" + str(result_get.status_code))

            if 404 == result_get.status_code:
                id_delete=place_id_text.split()[n]
                place_id_delete+=id_delete+'\n'
                print(place_id_delete)
            elif 200 == result_get.status_code:
                id_left=place_id_text.split()[n]
                place_id_left+=id_left+'\n'
                print(place_id_left)

        """Запись id в файл"""
        fw = open('place_id_left.txt', 'w')
        fw.write(place_id_left)
        fw.close()
        print(f"Существующие локации: \n{place_id_left}")
        print("\nИспытания завершены")

delete_place_id = Delete_location()
delete_place_id.delete_location_and_record_id()
