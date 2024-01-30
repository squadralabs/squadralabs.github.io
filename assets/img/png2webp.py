from PIL import Image
import os


def resize_and_convert_to_webp(folder="."):
    # Obtén la lista de archivos en el directorio actual
    files = os.listdir(folder)

    # Itera sobre los archivos en el directorio actual
    for file in files:
        if file.endswith(".png"):
            # Construye las rutas de entrada y salida
            input_path = os.path.join(folder, file)
            output_path = os.path.join(folder, os.path.splitext(file)[0] + ".webp")

            # Abre la imagen
            img = Image.open(input_path)

            # Redimensiona la imagen a 300x300
            # resized_img = img.resize((300, 300))

            # Guarda la imagen redimensionada en formato WebP en el mismo directorio
            img.save(output_path, "WEBP")

            print(f"{file} procesado con éxito.")


# Llama a la función para redimensionar y convertir a WebP en el directorio actual
# resize_and_convert_to_webp("tools/")
# resize_and_convert_to_webp("sq/")
# resize_and_convert_to_webp("services/")
resize_and_convert_to_webp("hero/")
