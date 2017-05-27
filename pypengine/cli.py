#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import sys
import logging
logging.basicConfig(level=logging.DEBUG)

from pypengine import __version__
from pypengine import utils
from pypengine import core

__author__ = "Francesco Strozzi"
__copyright__ = "Francesco Strozzi"
__license__ = "MIT"

_logger = logging.getLogger(__name__)


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--version',action='version',version='Pypengine {ver}'.format(ver=__version__))
    parser.add_argument("-c","--create",help="Create a samples.yml file from the project folder listed")
    parser.add_argument("-p","--pipeline",help="Pipeline YAML file",default="pipeline.yml")
    parser.add_argument("-l","--samples-list",help="List of samples to process",nargs='+')
    parser.add_argument("-f","--samples-file",help="Samples YAML file",default="samples.yml")
    parser.add_argument("-s","--steps",help="One or more pipeline steps to execute",nargs='+')
    parser.add_argument("-d","--dry",help="Dry run. Only to create scripts without running them")
    parser.add_argument("-t","--tmp",help="Temporary output folder")
    parser.add_argument("-g","--group",help="Specify the groups of samples to apply the pipeline on")
    parser.add_argument("-n","--name",help="Set a custom name for the pipeline step")
    parser.add_argument("-o","--output",help="Override standard output directory names")
    parser.add_argument("-b","--scheduler-options",help="Specify custom scheduler options")
    parser.add_argument("-q","--scheduler-queue",help="Specify scheduler queue")
    return parser.parse_args()

def main():
    args = parse_args()
    pipeline = utils.parse_yaml(args.pipeline)
    samples = utils.parse_yaml(args.samples_file)
    if not all(x in pipeline.keys() for x in ["pipeline","resources","steps"]):
        _logger.error("Pipeline YAML file is missing required keys. Please check that 'pipeline','resources' and 'steps' keys are present")
        sys.exit(1)
    elif not all(x in samples.keys() for x in ["resources","samples"]):
        _logger.error("Samples YAML file is missing required keys. Please check that 'resources',and 'samples' keys are present")
        sys.exit(1)
    else:
        core.run_job(pipeline,samples,args)

if __name__ == "__main__":
    main()
