from python:3.10-slim

WORKDIR /app

#install ffmpeg
RUN apt-get update && apt-get install -y ffmpeg

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

copy src/ ./src/

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]