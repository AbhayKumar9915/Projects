import logging


class LogGen:
    @staticmethod
    def logGen():
        logging.basicConfig(filename='Abhay.log', level=logging.DEBUG)
        logging.debug('This message should go to the log file')
        logging.info('So should this {}')
        logging.warning('And this, too')


logger = LogGen()
logger.logGen()
