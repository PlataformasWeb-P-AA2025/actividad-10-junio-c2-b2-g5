    FROM python:3.10

    WORKDIR /app

    # Copiar todos los archivos de src/ al contenedor
    COPY src/ /app/

    # Instalar Flask
    RUN pip install flask

    EXPOSE 5000

    CMD ["python", "app.py"]
