import logging
import logging.config
from teams_logger import TeamsHandler, Office365CardFormatter

url = 'https://ncu365.webhook.office.com/webhookb2/c16429e8-84e2-40ff-a502-d6de25498993@ab3ca549-6720-4beb-87e2-ee68221a6605/TeamFoundationServer/a2beeb32e187473683c9b89698c3e3b5/760e9a70-b103-49b7-872b-805c59dc2600'
logging_dict = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'teamscard': {
            '()': Office365CardFormatter,
            'facts': ["name", "levelname", "lineno"],
        },
    },
    'handlers': {
        'msteams': {
            'level': logging.INFO,
            'class': 'teams_logger.TeamsHandler',
            'url': url,
            'formatter': 'teamscard',
        },
    },
    'loggers': {
        __name__: {
            'handlers': ['msteams'],
            'level': logging.DEBUG,
        }
    },
}
logging.config.dictConfig(logging_dict)
logger = logging.getLogger(__name__)
logger.info('IoT && AI 測試通知')
