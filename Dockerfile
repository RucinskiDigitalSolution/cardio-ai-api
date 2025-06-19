# 🐍 Obraz z Pythona
FROM python:3.10-slim

# 📂 Katalog roboczy
WORKDIR /app

# 🧾 Skopiuj pliki
COPY . .

# 🔧 Zainstaluj zależności
RUN pip install --no-cache-dir -r requirements.txt

# 🚪 Otwórz port
EXPOSE 10000

# ▶️ Komenda startowa
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "10000"]
