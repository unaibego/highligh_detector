# Highlight Detector (Telegram Bot para detección de música en audio)

Este proyecto ahora funciona como un bot de Telegram que detecta segmentos musicales en un archivo de audio enviado por el usuario.

## Qué hace

- Recibe audio (o video convertido a audio) por Telegram.
- Procesa el audio para detectar segmentos de música.
- Responde con un texto que indica los tiempos de cada segmento (`Musika: HH:MM:SS - HH:MM:SS`).

## Flujo principal

1. Desplegar el bot (por ejemplo, en un servidor con Docker).
2. En Telegram, iniciar chat con el bot.
3. Enviar un mensaje con el archivo de audio (o video). El bot descarga el archivo, lo analiza y responde con los tiempos detectados.

## Estructura clave

- `src/telegram_main.py`: arranca el bot de Telegram y registra handlers.
- `api/telegram_handlers.py`: maneja mensajes y archivos enviados con el bot.
- `src/noise_detector.py`: lógica de detección de segmentos de música.
- `dockerfile`: define la imagen con Python, ffmpeg y dependencias.
- `docker-compose.yml`: configura el servicio para desplegar.

## Cómo desplegar

1. Clona el repositorio:

```bash
git clone <URL_DEL_REPOSITORIO>
cd higlight_detector
```

2. Crea un archivo `.env` con el token de Telegram:

```bash
echo "TELEGRAM_TOKEN=<TU_TOKEN>" > .env
```

3. (Opcional) crea un entorno virtual e instala dependencias:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

4. Levanta con Docker Compose:

```bash
docker compose up --build
```

5. Confirma que el bot esté activo en Telegram y responde a mensajes.

## Uso en Telegram

- Envía un archivo de audio directamente (formato mp3, wav, etc.).
- Si envías un video, el bot puede extraer audio internamente (según implementación) y analizarlo.
- El bot responde con texto:

```
Musika: 00:02:40 - 00:05:47
Musika: 00:06:30 - 00:07:51
...
```

## Ejemplo rápido con Telegram

1. Abre Telegram y busca tu bot.
2. Envía un mensaje con audio  como archivo.
3. Espera la respuesta con los segmentos detectados.

> Si recibes error, revisa logs en el contenedor y verifica que `TELEGRAM_TOKEN` esté bien configurado.

## Notas

- Este repo está enfocado a deploy rápido y uso por Telegram.
- Asegúrate de tener `ffmpeg` disponible (el contenedor lo incluye).
- Los resultados se devuelven en texto en el chat de Telegram, en el mismo formato de segmentos por línea.

