FROM python:3.9-slim
WORKDIR /app

# El contexto de build es la RAÍZ del repo
# Copiar requirements desde app/
COPY app/requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el contenido de la carpeta app/ al /app del contenedor
COPY app/ .

# Verificar que app.py está
RUN ls -la /app/ && test -f /app/app.py

EXPOSE 5000
CMD ["python", "app.py"]