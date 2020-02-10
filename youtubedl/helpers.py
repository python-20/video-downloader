import logging
import os


DEFAULT_DIRECTORY = "./downloads"
APP_NAME = "Video Downloader"


class Helpers:
    """
    Class used for auxiliary functions non related to core functionality of the application
    """

    def logging_setup(logging_directory, appName):
        """
        Function to redirect logs to files
        Current enabled logger(s): info (logging.info)
        """
        if not os.path.exists(logging_directory):
            os.makedirs(logging_directory)

        logger = logging.getLogger(appName)
        logger.setLevel(logging.INFO)

        infoLog = logging.FileHandler('{}{}_info.log'.format(
            logging_directory, appName), 'w+', 'utf-8')
        infoLog.setLevel(logging.INFO)

        formatter = logging.Formatter('%(levelname)s - %(message)s')
        infoLog.setFormatter(formatter)

        logger.addHandler(infoLog)

        infoLogscreen = logging.StreamHandler()

        infoLogscreen.setLevel(logging.INFO)
        infoLogscreen.setFormatter(formatter)

        logger.addHandler(infoLogscreen)

        return logger
