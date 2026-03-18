from pydantic_settings  import BaseSettings


class TelegramSettings(BaseSettings):
    token: str

    #indicamos el prefijo para las variables de entorno
    class Config:
        env_prefix = "TELEGRAM_"
   

telegram_settings = TelegramSettings()
def get_telegram_settings():
    return telegram_settings