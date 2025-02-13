from PIL import Image
import os

# Configuración
INPUT_FOLDER = "clients/hd"  # Carpeta de entrada con imágenes PNG
OUTPUT_FOLDER = "clients/webp"  # Carpeta de salida para las imágenes WEBP
FIXED_SIZE = (600, 600)  # Tamaño fijo (ancho, alto)

# Crear la carpeta de salida si no existe
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# Procesar todas las imágenes en la carpeta
for filename in os.listdir(INPUT_FOLDER):
    if filename.lower().endswith(".png") or filename.lower().endswith(".jpg"):
        input_path = os.path.join(INPUT_FOLDER, filename)
        output_path = os.path.join(OUTPUT_FOLDER, f"{os.path.splitext(filename)[0]}.webp")

        # Abrir, redimensionar y guardar en formato WEBP
        with Image.open(input_path) as img:
            img = img.resize(FIXED_SIZE, Image.Resampling.LANCZOS)
            img.save(output_path, "WEBP", quality=100)  # Ajusta la calidad según necesidad

        print(f"Convertido: {filename} → {output_path}")

print("Conversión completada.")
