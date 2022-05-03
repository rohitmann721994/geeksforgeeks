import logging


class Logger:
    def __init__(self)->logging.Logger:
        self.logging = logging.getLogger(__name__)
        fieldstyle = {'asctime': {'color': 'green'},
                      'levelname': {'bold': True, 'color': 'black'},
                      'filename':{'color':'cyan'},
                      'funcName':{'color':'blue'}}
        levelstyles = {'critical': {'bold': True, 'color': 'red'},
                       'debug': {'color': 'green'},
                       'error': {'color': 'red'},
                       'info': {'color':'magenta'},
                       'warning': {'color': 'yellow'}}
        coloredlogs.install(
            logger=self.logging,
            fmt='%(asctime)s [%(levelname)s] - [%(filename)s > %(funcName)s() > %(lineno)s] - %(message)s',
            datefmt='%H:%M:%S',
            field_styles=fieldstyle,
            level_styles=levelstyles)
        return self.logging
