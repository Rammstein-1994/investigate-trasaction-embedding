import logging


def get_logger(name: str = None, log_path: str = "./log.log") -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    # create file handler which logs even debug messages
    file_handler = logging.FileHandler(log_path, mode="a")
    file_handler.setLevel(logging.INFO)

    # create console handler and set level to debug
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.WARNING)

    # create formatter
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )

    # add formatter to handler
    file_handler.setFormatter(formatter)
    stream_handler.setFormatter(formatter)

    # add handler to logger
    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)

    return logger
