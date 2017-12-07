import logging

from scotty import utils

logger = logging.getLogger(__name__)


def run(context):
    workload = context.v1.workload
    exp_helper = utils.ExperimentHelper(context)
    logger.info(workload.resources)
    cpu_stress_resource = exp_helper.get_resource(workload.resources['cpu_stressor'])
    logger.info(cpu_stress_resource)
    logger.info('I\'m workload generator {}'.format(workload.name))
    logger.info('The resource endpoint is {}'.format(cpu_stress_resource.endpoint))
    return 42


def clean(context):
    pass
