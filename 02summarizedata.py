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

#def summarize_file(fname):
#
#    #/home/afu/2013-sbrc-experiments.results
#    s = sd.SummarizeData('/home/afu/2013-sbrc-experiments/results')
#    best, worst, average = s.load_pm_scenario(fname)
#    s.csv_write()

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

    for trace in trace_scenarios:
        for host in host_scenarios:
            per_algoritm_summary = {}
            for algorithm in algorithm_scenarios:
                fname = 'simulation-' + trace + '-' + algorithm + '-' + str(host).zfill(3)
                print('processing {}...'.format(fname))
                d = sd.SummarizeData(indir)

                d.load_pm_scenario(fname)
                per_algoritm_summary[algorithm] = d
                d.csv_write()
            p.set_data(per_algoritm_summary)
            p.plot_all_algorithm_comparison(host, trace)
