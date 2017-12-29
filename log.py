

import sys,coloredlogs
import logging

#logging.basicConfig(level=logging.INFO)


#coloredlogs.DEFAULT_FIELD_STYLES = {'hostname': {'color': 'magenta'}, 'programname': {'color': 'cyan'}, 'name': {'color': 'blue'}, 'levelname': {'color': 'black', 'bold': True}, 'asctime': {'color': 'green'}}

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
# create a file handler
handler = logging.FileHandler('hello.log')
handler.setLevel(logging.DEBUG)
# create a logging format
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
# add the handlers to the l
logger.addHandler(handler)
#l.addHandler(console_handler)

#test code

class myconsolelog():
    def __init__(self):
        coloredlogs.DEFAULT_LEVEL_STYLES= {
                                            'debug': {'color': 'magenta','bold': True},
                                            'info': {'color': 'yellow','bold': True},
                                            'warning': {'color': 'green','bold': True},
                                            'error': {'color': 'red','bold': True}
                                            }
        coloredlogs.DEFAULT_LOG_FORMAT = '%(message)s'
        coloredlogs.install(level='info',logger=logger)
        # create a console handler
        # and set its log level to the command-line option
        #
        #console_handler = logging.StreamHandler(sys.stdout)
        #console_handler.setLevel(logging.INFO)


    def info(self,m):
        logger.warning(m)
    def debug(self,m):
        logger.debug(m)
    def verbose(self,m):
        logger.info(m)
    def err(self,m):
        logger.error(m)

l = myconsolelog()

#logger.warning("WARNING")
l.info('my info = WARNING')
#logger.info("info")
l.verbose('my verbose = INFO ...')
#logger.error("error")
l.err('my error = EEEEEE')
#logger.debug("DEBUG")
l.debug('my debug = DEBUG ')
