
from pypengine.job import Job
import sys
import logging
logging.basicConfig(level=logging.DEBUG)
_logger = logging.getLogger(__name__)

def job_template(pipeline,samples,args):
    for key in pipeline["resources"].keys():
        if key in samples["resources"]:
            _logger.error("Resource '{0}' found in both Pipeline and Samples definition".format(key))
            sys.exit(1)
    resources = dict(list(pipeline["resources"].items()) + list(samples["resources"].items()))
    job = Job(args.steps)
    multi_sample_job = []
    for step in args.steps:
        if not step in pipeline["steps"]:
            _logger.error("Step '{0}' not found in pipeline definition".format(step))
            sys.exit(1)
        else:
            job.steps[step] = pipeline["steps"][step]
            if "multi" in job.steps[step]:
                multi_sample_job.append(True)
            else:
                multi_sample_job.append(False)

    if len(set(multi_sample_job)) > 1:
        _logger.error("Mixing together in the same job single and multi samples steps")
        sys.exit(1)
    job.multi = multi_sample_job[0]


    samples_to_process = {}
    if args.samples:
        for s in args.samples:
            if not s in samples["samples"]:
                _logger.error("Sample '{0}' not found in samples file".format(s))
                sys.exit(1)
            else:
                samples_to_process[s] = samples["samples"][s]

    return job


