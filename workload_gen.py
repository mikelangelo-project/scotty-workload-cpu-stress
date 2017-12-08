import logging
import time

from scotty import utils

logger = logging.getLogger(__name__)


def run(context):
    #workload = context.v1.workload
    #exp_helper = utils.ExperimentHelper(context)
    #logger.info(workload.resources)
    #cpu_stress_resource = exp_helper.get_resource(workload.resources['cpu_stressor'])
    #logger.info(cpu_stress_resource)
    #logger.info('I\'m workload generator {}'.format(workload.name))
    logger.info('Hi')
    time.sleep(1)
    logger.info('Yes I am')
    seconds_delay = 60*60*24
    for period in range(seconds_delay):
        time.sleep(1)
        logger.info(period)
    #logger.info('The resource endpoint is {}'.format(cpu_stress_resource.endpoint))
    return 42


def clean(context):
    pass
