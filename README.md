# Amnezia IP List Converter

English version: [README.en.md](README.en.md)

Скрипт для преобразования JSON/списка IP-подсетей в формат `ip-list.json`, который можно использовать в Amnezia.

## Что делает

Преобразует входные данные в массив объектов:

```json
[
    {
        "hostname": "1.2.3.0/24",
        "ip": ""
    }
]
```

## Поддерживаемые входные форматы

- файл с подсетями по одной строке;
- JSON-массив строк:
  - `["1.2.3.0/24", "5.6.7.0/24"]`;
- JSON-массив объектов с полем `hostname`:
  - `[{"hostname":"1.2.3.0/24"}]`.

## Требования

- Python 3.9+.

## Установка

Локальная установка из папки проекта:

```bash
python -m pip install .
```

Установка в режиме разработки:

```bash
python -m pip install -e .
```

Установка напрямую из GitHub:

```bash
python -m pip install "git+https://github.com/<user>/<repo>.git"
```

## Использование

Без установки (запуск скрипта напрямую):

```bash
python amnezia-ip-convert.py input.json output-ip-list.json
```

После установки (через CLI-команду):

```bash
amnezia-ip-convert input.json output-ip-list.json
```

Где:
- `input.json` — исходный файл с IP-адресами/подсетями;
- `output-ip-list.json` — файл в формате Amnezia JSON.

## Структура проекта

- `amnezia-ip-convert.py` — запуск без установки;
- `amnezia_ip_convert.py` — основной модуль конвертера;
- `README.md` — документация на русском;
- `README.en.md` — документация на английском;
- `.gitignore` — исключения для Git;
- `LICENSE` — лицензия MIT.

