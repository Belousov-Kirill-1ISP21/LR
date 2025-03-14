import logging

class loggingConfig:
    @staticmethod
    def setupLogging(log_file='app.log'):
        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)

        with open(log_file, 'w'):
            pass

        file_handler = logging.FileHandler(log_file, encoding='utf-8')
        file_handler.setLevel(logging.DEBUG)

        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)

        logger.addHandler(file_handler)

