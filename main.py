import requests, json

# Задача 1 Кто самый умный супергерой
url = requests.get('https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json')
superheroes_list = json.loads(url.text)

supaheroes = {}
for i in superheroes_list:
    supa_name = i.get('name')
    supa_stats = i.get('powerstats')
    supaheroes.update({supa_name: supa_stats.get('intelligence')})

smartest_hero = []
supahero = ['Hulk', 'Captain America', 'Thanos']
for x in supaheroes.items():
    name, intellect = x
    if name in supahero:
        smartest_hero.append(list(x))
smartest_hero.sort(reverse=True)
print(f'Вывод задачи №1:\nСамый умный герой из троицы, это - {smartest_hero[0][0]}')

# Задача №2 Список файлов на Яндекс диск
class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }

    def upload(self, file_path: str):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        upload_url = self._yandex_link(file_path)
        response = requests.put(upload_url, data=open(file_path, 'rb'), headers=self.get_headers())
        if response.status_code == 201:
            print(f'Загрузка файла - {file_path} произошла успешно!')

    def _yandex_link(self, path):
        uri = 'https://cloud-api.yandex.net/v1/disk/resources/upload/'
        params = {'path': path, 'overwrite': True}
        response = requests.get(uri, headers=self.get_headers(), params=params)
        # print(response.json())
        return response.json()['href']

if __name__ == '__main__':
    path_to_file = ['hello_world.txt', 'hellNO_word.txt', 'Hasta_La_vista_baby.txt']
    # Введите сюда свой ТОКЕН:
    token = ...
    uploader = YaUploader(token)
    for file in path_to_file:
        result = uploader.upload(file)