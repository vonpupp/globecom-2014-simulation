#!/usr/bin/python
# vim:ts=4:sts=4:sw=4:et:wrap:ai:fileencoding=utf-8:

# Add relative path for other imports
import sys
sys.path.append("pyCloudSim")

#from distsim.model.tracefilter import TraceFilter
import distsim.analysis.summarizedata as sd
import distsim.analysis.csvloader as csvl
import distsim.analysis.plotdata as plot
from scenariosvars import *
import argparse
import os
from operator import methodcaller


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

    for trace in trace_scenarios:
        for host in host_scenarios:
            per_algorithm_summary = {}
            per_algorithm_placement = {}
#            for algorithm in algorithm_scenarios:
#                fname = 'simulation-' + trace + '-' + algorithm + '-' + str(host).zfill(3)
#                print('processing {}...'.format(fname))
#                d = sd.SummarizeData(indir)
#
#                d.load_pm_scenario(fname)
#                per_algorithm_summary[algorithm] = d
#                d.csv_write()
#
#            p.set_data(per_algorithm_summary)
#            p.plot_all_algorithm_comparison(host, trace)

            for vms in range(vms_start, vms_stop, vms_step):
                for algorithm in algorithm_scenarios:
                    fname = 'summarized-placement-' + trace + '-' + algorithm + '-' + str(host).zfill(3) + '-' + str(vms).zfill(3)
                    print('processing {}...'.format(fname))
                    d = sd.SummarizePlacementData(indir)
                    d.load_placement(fname)
                    per_algorithm_placement[algorithm] = d
                pgg.set_data(per_algorithm_placement)
                pgg.plot_all_algorithm_comparison(trace, host)
