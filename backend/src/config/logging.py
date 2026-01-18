# src/logging_config.py
import logging
from pathlib import Path
import sys

def setup_logging():
    """Configura o sistema de logging para salvar em arquivos"""
    
    # Cria diretório de logs se não existir
    logs_dir = Path(__file__).resolve().parent.parent / "logs"
    logs_dir.mkdir(exist_ok=True)
    
    # Configuração do logging
    logging_config = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "detailed": {
                "format": "%(asctime)s - %(name)s - %(levelname)s - %(module)s:%(lineno)d - %(message)s",
                "datefmt": "%Y-%m-%d %H:%M:%S"
            },
            "simple": {
                "format": "%(asctime)s - %(levelname)s - %(message)s",
                "datefmt": "%Y-%m-%d %H:%M:%S"
            }
        },
        "handlers": {
            "file_app": {
                "class": "logging.handlers.RotatingFileHandler",
                "level": "INFO",
                "formatter": "detailed",
                "filename": logs_dir / "app.log",
                "maxBytes": 10485760,  # 10MB
                "backupCount": 5,
                "encoding": "utf8"
            },
            "file_error": {
                "class": "logging.handlers.RotatingFileHandler",
                "level": "ERROR",
                "formatter": "detailed",
                "filename": logs_dir / "error.log",
                "maxBytes": 10485760,  # 10MB
                "backupCount": 5,
                "encoding": "utf8"
            },
            "file_debug": {
                "class": "logging.FileHandler",
                "level": "DEBUG",
                "formatter": "detailed",
                "filename": logs_dir / "debug.log",
                "encoding": "utf8"
            },
            # Handler para console (opcional - comente se não quiser no terminal)
            # "console": {
            #     "class": "logging.StreamHandler",
            #     "level": "INFO",
            #     "formatter": "simple",
            #     "stream": sys.stdout
            # }
        },
        "loggers": {
            "": {  # Root logger
                "level": "DEBUG",
                "handlers": ["file_app", "file_error", "file_debug"],
                "propagate": False
            },
            "src": {
                "level": "INFO",
                "handlers": ["file_app", "file_error"],
                "propagate": False
            },
            "uvicorn": {
                "level": "INFO",
                "handlers": ["file_app"],
                "propagate": False
            },
            "uvicorn.error": {
                "level": "ERROR",
                "handlers": ["file_error"],
                "propagate": False
            },
            "uvicorn.access": {
                "level": "INFO",
                "handlers": ["file_app"],
                "propagate": False
            }
        }
    }
    
    # Aplica a configuração
    logging.config.dictConfig(logging_config)
    
    # Suprime logs do terminal para alguns loggers chatos
    logging.getLogger("uvicorn.access").propagate = False
    logging.getLogger("uvicorn.error").propagate = False
    
    return logs_dir