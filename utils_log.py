from loguru import logger

logger.debug("Isso é um log de DEBUG.")
logger.info("Isso é um log de INFO.")
logger.warning("Isso é um log de WARNING.")
logger.error("Isso é um log de ERROR.")
logger.critical("Isso é um log de CRITICAL.")


logger.add("logs/app.log", format="{time} - {level} - {message}")
logger.info("Mensagem com formatação personalizada.")
