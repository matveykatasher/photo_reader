# file: photo_info.py

import os
import pyheif
from PIL import Image
from PIL.ExifTags import TAGS


def get_exif_data(image):
    """Получает EXIF-данные изображения."""
    try:
        exif_data = image._getexif()
        if not exif_data:
            return {}
        return {TAGS.get(tag): value for tag, value in exif_data.items() if tag in TAGS}
    except Exception:
        return {}


def open_heic_image(file_path):
    """Открывает HEIC-изображение и конвертирует его в объект Pillow."""
    heif_file = pyheif.read(file_path)
    image = Image.frombytes(
        heif_file.mode,
        heif_file.size,
        heif_file.data,
        "raw",
        heif_file.mode,
        heif_file.stride,
    )
    return image


def get_image_info(file_path):
    """Получает и выводит информацию о фото."""
    try:
        # Проверяем, существует ли файл
        if not os.path.exists(file_path):
            print("Файл не найден. Проверьте путь.")
            return

        # Определяем формат файла
        extension = os.path.splitext(file_path)[1].lower()

        # Открываем изображение в зависимости от формата
        if extension == ".heic":
            img = open_heic_image(file_path)
            format = "HEIC"
        else:
            img = Image.open(file_path)
            format = img.format

        # Получаем основную информацию об изображении
        width, height = img.size
        mode = img.mode
        exif_data = get_exif_data(img)

        # Получаем размер файла
        file_size = os.path.getsize(file_path) / 1024  # Размер в КБ

        # Извлекаем модель телефона и объектива из EXIF
        camera_model = exif_data.get("Model", "Не указано")
        lens_model = exif_data.get("LensModel", "Не указано")

        # Выводим информацию
        print(f"Информация о фото '{os.path.basename(file_path)}':")
        print(f" - Формат: {format}")
        print(f" - Разрешение: {width}x{height} пикселей")
        print(f" - Режим: {mode}")
        print(f" - Размер файла: {file_size:.2f} КБ")
        print(f" - Модель телефона: {camera_model}")
        print(f" - Модель объектива: {lens_model}")

    except Exception as e:
        print(f"Произошла ошибка при обработке файла: {e}")


def main():
    """Основная функция программы."""
    print("Перетащите изображение в это окно и нажмите Enter:")
    file_path = input().strip('"')  # Убираем кавычки, если они есть
    get_image_info(file_path)


if __name__ == "__main__":
    main()
