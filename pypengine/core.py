
from pypengine.job import Job
from pypengine.step import Step
import logging
logging.basicConfig(level=logging.DEBUG)
_logger = logging.getLogger(__name__)

def run_job(pipeline,samples,args):
    resources = dict(list(pipeline["resources"].items()) + list(samples["resources"].items()))
    _logger.info(resources)

