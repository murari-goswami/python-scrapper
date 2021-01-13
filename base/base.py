import logging
import sys


def baselog():
    formatter_string = '%(asctime)s %(name)s %(levelname)s %(message)s'
    logging.basicConfig(filename="running-log-yyyyMMDD.log"
                        , filemode='a'
                        , level=logging.INFO
                        , format=formatter_string
                        , datefmt='%H:%M:%S'
                        )
    handler = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter(formatter_string)
    handler.setFormatter(formatter)
    logger = logging.getLogger(__name__)
    logger.addHandler(handler)
    logger.info("Master execution")


if __name__ == '__main__':
    baselog()
