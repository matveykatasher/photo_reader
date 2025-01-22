# photo_reader

 — это консольная программа на Python, которая предоставляет информацию об изображениях, включая такие параметры, как разрешение, формат, размер файла, модель телефона и объектив. Поддерживаются изображения в популярных форматах, включая **HEIC**, **JPEG**, **PNG** и другие.

---

## Функциональные возможности
- Получение информации о разрешении, формате, размере и цветовой модели изображения.
- Извлечение EXIF-данных, таких как:
  - **Модель телефона** (например, iPhone 12 Pro).
  - **Модель объектива** (например, iPhone 12 Pro Max back dual camera 13mm f/1.8).
- Поддержка формата **HEIC** с использованием библиотеки `pyheif`.

---

##Использование

1)Запустите скрипт:

python photo_info.py
Перетащите изображение в окно консоли и нажмите Enter.

---
Пример вывода для изображения:

Перетащите изображение в это окно и нажмите Enter:
"example.heic"
Информация о фото 'example.heic':
 - Формат: HEIC
 - Разрешение: 3024x4032 пикселей
 - Режим: RGB
 - Размер файла: 1245.67 КБ
 - Модель телефона: iPhone 16 Pro
 - Модель объектива: iPhone 16 Pro Max back dual camera 13mm f/1.8

---
##Поддерживаемые форматы

-HEIC (High Efficiency Image Coding)
-JPEG
-PNG
-TIFF
