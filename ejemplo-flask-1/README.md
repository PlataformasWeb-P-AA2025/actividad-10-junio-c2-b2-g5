# Proyecto Ejemplo Flask

Este proyecto es un ejemplo básico de una aplicación web utilizando el framework Flask. La aplicación permite a los usuarios ingresar su nombre y recibir un saludo personalizado.

## Estructura del Proyecto

```
ejemplo-flask
├── src
│   ├── app.py                  # Punto de entrada de la aplicación Flask
│   ├── controllers
│   │   └── hello_controller.py  # Controlador que maneja la lógica de saludo
│   ├── models
│   │   └── __init__.py          # Archivo para definiciones de modelos (vacío por ahora)
│   ├── views
│   │   └── hello.html           # Plantilla HTML para mostrar el saludo
│   └── types
│       └── index.py             # Archivo para definiciones de tipos (vacío por ahora)
├── requirements.txt             # Dependencias del proyecto
└── README.md                    # Documentación del proyecto
```

## Requisitos

Para ejecutar esta aplicación, necesitas tener instalado Python y Flask. Puedes instalar las dependencias necesarias ejecutando:

```
pip install -r requirements.txt
```

## Ejecución

Para iniciar la aplicación, ejecuta el siguiente comando en la terminal:

```
python src/app.py
```

Luego, abre tu navegador y visita `http://127.0.0.1:5000` para ver la aplicación en acción.