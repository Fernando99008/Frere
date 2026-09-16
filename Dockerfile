FROM python:3.12

# Carpeta de trabajo
WORKDIR /app

# Dependencias del sistema necesarias para PySide6/Qt
RUN apt-get update && apt-get install -y \
    libdbus-1-3 \
    libgl1 \
    libegl1 \
    libgles2 \
    libxkbcommon0 \
    libxkbcommon-x11-0 \
    libx11-6 \
    libx11-xcb1 \
    libxcb1 \
    libxcb-cursor0 \
    libxcb-glx0 \
    libxcb-icccm4 \
    libxcb-image0 \
    libxcb-keysyms1 \
    libxcb-randr0 \
    libxcb-render-util0 \
    libxcb-shape0 \
    libxcb-shm0 \
    libxcb-xfixes0 \
    libxcb-xinerama0 \
    libxcb-xkb1 \
    libxext6 \
    libxfixes3 \
    libxi6 \
    libxrender1 \
    libfontconfig1 \
    libfreetype6 \
    libsm6 \
    libice6 \
    libnss3 \
    && rm -rf /var/lib/apt/lists/*

# Copiar requirements
COPY requirements.txt .

# Instalar dependencias Python
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el proyecto
COPY . .

# Ejecutar la aplicación
CMD ["python", "main.py"]