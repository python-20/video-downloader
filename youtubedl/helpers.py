import logging
import os


DEFAULT_DIRECTORY = "./downloads"
APP_NAME = "Video Downloader"


def logging_setup(logging_directory, appName=APP_NAME):
    """
    Function to redirect logs to files
    Current enabled logger(s): info (logging.info)
    """
    if not os.path.exists(logging_directory):
        os.makedirs(logging_directory)

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    infoLog = logging.FileHandler(
        f"{logging_directory}{appName}_info.log", 'w+', 'utf-8')
    infoLog.setLevel(logging.INFO)

    formatter = logging.Formatter('%(levelname)s - %(message)s')
    infoLog.setFormatter(formatter)

    logger.addHandler(infoLog)

    infoLogscreen = logging.StreamHandler()

    infoLogscreen.setLevel(logging.INFO)
    infoLogscreen.setFormatter(formatter)

    logger.addHandler(infoLogscreen)

    return logger


logger = logging_setup("logs/")
