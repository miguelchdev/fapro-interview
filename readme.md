# API para consultar la Unidad de Fomento
Esta API está desarrollada con FastAPI, se encarga de devolver el valor de la UF para una fecha dada, primero intenta buscar el valor en la base de datos, si no lo encuentra hace una request a https://www.sii.cl/ para encontrar el valor.

## Instalación usando Docker Compose

```bash
docker-compose build
```

### Iniciar el servidor

```bash
docker-compose up
api_1  | INFO:     Started server process [1]
api_1  | INFO:     Waiting for application startup.
api_1  | INFO:     Application startup complete.
api_1  | INFO:     Uvicorn running on http://0.0.0.0:80 (Press CTRL+C to quit)

```

### Correr test unitarios

```bash
docker-compose up
docker-compose exec api  pytest -o log_cli=true

```
## Instalación usando Pip
Crear entorno virtual
```bash
python3.9 -m venv sii_api
```

Activar entorno virtual
```bash
 source sii_api/bin/activate
```
Instalación de dependecias.
```bash
 pip install -r requeriments.txt
```
Iniciar el servidor
```bash
uvicorn main:app
INFO:     Started server process [15964]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
``` 
### Correr test unitarios
```bash
pytest -o log_cli=true

```
# Uso
La API  tiene dos endpoints:

1. **/uf/{date}:** Obtiene el valor de la UF para la fecha dada.
2. **/docs** Documentación de la API.


### Ejemplo de llamada a /uf
Obtener el valor de la UF para el 16 de Septiembre de 2022
```bash
http://0.0.0.0:80/uf/2022-09-16 #  http://127.0.0.1:8000/uf/2022-09-16 (Usando pip)
```
Respuesta
```json
{
  "date": "2022-09-16",
  "value": 34068.05
}
```
