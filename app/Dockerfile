FROM python:3.9-slim
WORKDIR /app

# Copiar todo el contenido del contexto (que es app/)
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copiar TODO el contexto actual (app.py, templates/, static/)
COPY . /app/

# Verificar que app.py existe (esto fallará el build si no está)
RUN ls -la /app/ && test -f /app/app.py || (echo "ERROR: app.py no encontrado" && exit 1)

EXPOSE 5000
CMD ["python", "/app/app.py"]