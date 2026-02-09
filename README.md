# Anit-Futbol-Manager

## Instalar dependencias

Primero creamos el entorno virtual:

`python3 -m venv venvFutbol`

Accedemos a el entorno:

`source venvFutbol/bin/activate`

Instalamos las dependecias:

`python3 -m pip install -r requirements.txt`

## ¿Como configurar las claves?

1º Renombra el archivo tokens_plantilla.txt a tokens.txt

2º Añade las variables correspondientes siguiendo las instrucciones:

API_TOKEN= # Creamos un Token personalizado con permisos de edición del DNS para todos los dominios en la configuración de Cloudflare

ZONE_ID= # Información del usuario que se obtiene desde: https://dash.cloudflare.com/

![Imagen señalando la opcion Copy Zone ID.](/images/ZoneID.png "Imagen señalando la opcion Copy Zone ID.")

## ¿Como ejecutar?

Antes de nada entramos en el entorno virtual:

`source venvFutbol/bin/activate`

Para comprobar que funciona correctamente ejecuta en terminal:

`python3 futbolManager.py`

Si vemos que realiza la primera ejecución correctamente, esta terminal ya esta haciendo las funciones hasta que la cierres. Pero podemos ejecutar lo siguiente para que funcione de fondo sin molestar:

`nohup python3 futbolManager.py &`

Para comprobar que funciona bien podemos leer su salida con:

`cat nohup.out`

## ¿Como cerrar?

Tenemos que matar el proceso a mano, no hay forma user-friendly para hacerlo. Primero buscamos el proceso:

`ps aux | grep futbolManager.py`

Nos quedamos con su PID:

![Imagen señalando la opcion Copy Zone ID.](/images/ScrapperPID.png "Imagen señalando la opcion Copy Zone ID.")

Y lo matamos con:

`sudo kill PID_DEL_COMANDO_ANTERIOR`
