#!/usr/bin/python
# vim:ts=4:sts=4:sw=4:et:wrap:ai:fileencoding=utf-8:
#
# Copyright 2013-2014 Albert De La Fuente Vigliotti
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
2014 Globecom Simulations
"""

__version__ = "0.2"
__author__ = "Albert De La Fuente Vigliotti"


# Add relative path for other imports
import sys
sys.path.append("pyCloudSim")

#from distsim.model.tracefilter import TraceFilter
import pycloudsim.analysis.summarizedata as sd
import pycloudsim.analysis.csvloader as csvl
import pycloudsim.analysis.plotdata as plot
from scenariosvars import *
import argparse
import os
from operator import methodcaller
from collections import defaultdict


def get_default_arg(default_value, arg):
    if arg is None:
        return default_value
    else:
        return arg
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='A VM distribution/placement simulator.')
    parser.add_argument('-i', '--indir', help='Input directory', required=False)
    parser.add_argument('-o', '--outdir', help='Output directory', required=False)
    args = parser.parse_args()

    # Change current directory
    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    os.chdir(dname + '/' + 'pyCloudSim')

    indir = get_default_arg('results', args.indir)
    outdir = get_default_arg('results', args.outdir)

    # Get only the filenames (remove prepending paths)
    trace_scenarios = map(lambda trace: trace.split('/')[-1], trace_scenarios)

    p = plot.GraphGenerator(indir)
    pgg = plot.PlacementGraphGenerator(indir)

    per_algorithm_placement = defaultdict(
        lambda: defaultdict(
            lambda: defaultdict(
                lambda: defaultdict(dict)
            )
        ))
    for trace in trace_scenarios:
        for host in host_scenarios:
            per_algorithm_summary = {}
            for algorithm in algorithm_scenarios:
                fname = 'simulation-' + trace + '-' + algorithm + '-' + str(host).zfill(3)
                print('processing {}...'.format(fname))
                d = sd.SummarizeData(indir)

                d.load_pm_scenario(fname)
                per_algorithm_summary[algorithm] = d
                d.csv_write()

            p.set_data(per_algorithm_summary)
            p.plot_all_algorithm_comparison(host, trace)

            for vms in range(vms_start, vms_stop, vms_step):
                for algorithm in algorithm_scenarios:
                    fname = 'summarized-placement-' + trace + '-' + algorithm + '-' + str(host).zfill(3) + '-' + str(vms).zfill(3)
                    print('processing {}...'.format(fname))
                    d = sd.SummarizePlacementData(indir)
                    d.load_placement(fname)
                    per_algorithm_placement[host][vms][algorithm][trace] = d
#                    per_algorithm_placement[vms][algorithm][trace][host] = d
    pgg.set_data(per_algorithm_placement)
    pgg.plot_all_algorithm_comparison(algorithm_scenarios, trace_scenarios, host, vms_stop - vms_step)
