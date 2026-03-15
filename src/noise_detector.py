from pathlib import Path
from inaSpeechSegmenter import Segmenter

video_path = Path("blob/Ensayo 7.mp4")

def detect_video_parts(video_path) -> list:

    print(f"Detectando partes del video: {video_path}")
    seg = Segmenter(vad_engine="smn", detect_gender=False)
    segments = seg(video_path)
    return segments


def transform_segments_time(segments) -> list:
    """Transforma los tiempos de los segmentos de segundos a formato horario HH:MM:SS.
    """
    transformed_segments = []
    for segment in segments:
        start_time = segment[1]
        end_time = segment[2]
        start_time_formatted = f"{int(start_time // 3600):02d}:{int((start_time % 3600) // 60):02d}:{int(start_time % 60):02d}"
        end_time_formatted = f"{int(end_time // 3600):02d}:{int((end_time % 3600) // 60):02d}:{int(end_time % 60):02d}"   
        transformed_segments.append((segment[0], start_time_formatted, end_time_formatted))
    return transformed_segments

def get_long_time_segments(segments, threshold=60) -> list:
    long_time_segments = []
    for segment in segments:
        start_time = segment[1]
        end_time = segment[2]
        duration = end_time - start_time
        if duration >= threshold:
            long_time_segments.append(segment)
    return long_time_segments

def get_music_segments(segments) -> list:
    music_segments = []
    for segment in segments:
        if segment[0] == "music":
            music_segments.append(segment)
    return music_segments


def get_string_from_segments(segments) -> str:
    """Genera un string con saltos de linea por cada segmento. En cada linea pone Musika y la hora de inicio del segmento.
    """
    segments_string = ""
    for segment in segments:
        segments_string += f"Musika: {segment[1]} - {segment[2]}\n"
    return segments_string


def procesar_video(video_path) -> str:
    print(f"Procesando video: {video_path}")
    segments = detect_video_parts(video_path)
    print(f"Filtrando por segmentos de musica")
    music_segments = get_music_segments(segments)
    print(f"Filtrando por segmentos de musica largos")
    music_long_segments = get_long_time_segments(music_segments, threshold=60)
    print(f"Transformando segmentos a formato horario")
    cleaned_segments = transform_segments_time(music_long_segments)
    print(f"Generando string con los segmentos")
    segment_string = get_string_from_segments(cleaned_segments)
    return segment_string

if __name__ == "__main__":
    segments = detect_video_parts(video_path)
    music_segments = get_music_segments(segments)
    music_long_segments = get_long_time_segments(music_segments, threshold=60)
    cleaned_segments = transform_segments_time(music_long_segments)
    segment_string = get_string_from_segments(cleaned_segments)
    print(segment_string)