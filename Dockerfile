# Gunakan Python 3.11 sebagai base image
FROM python:3.11-slim

# Set working directory di dalam container
WORKDIR /app

# Salin requirements.txt ke working directory
COPY requirements.txt .

# Instal dependensi Python
RUN pip install --no-cache-dir -r requirements.txt

# Salin seluruh kode proyek ke working directory
COPY . .

# Kumpulkan static files
RUN python manage.py collectstatic --noinput

# Expose port 8000 untuk aplikasi Django
EXPOSE 8000

# Jalankan aplikasi Django menggunakan Gunicorn
CMD ["gunicorn", "event_management.wsgi:application", "--bind", "0.0.0.0:8000"]