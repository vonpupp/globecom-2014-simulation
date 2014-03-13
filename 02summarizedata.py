#!/usr/bin/python
# vim:ts=4:sts=4:sw=4:et:wrap:ai:fileencoding=utf-8:
#
# Copyright 2013 Albert De La Fuente
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
SummarizeData :: Data summarizer
"""
__version__ = "0.1"
__author__  = "Albert De La Fuente"


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

    #trace_scenarios = [
    #    '146-179_surfsnel_dsl_internl_net_root',
    #    'host4-plb_loria_fr_uw_oneswarm',
    #    'plgmu4_ite_gmu_edu_rnp_dcc_ufjf',
    #
    #    'planetlab1_fct_ualg_pt_root',
    #    'host3-plb_loria_fr_inria_omftest',
    #    'planetlab1_georgetown_edu_nus_proxaudio',
    #
    #    'planetlab1_dojima_wide_ad_jp_princeton_contdist',
    #    'planetlab-20110409-filtered_planetlab1_s3_kth_se_sics_peerialism',
    #    'planetlab-wifi-01_ipv6_lip6_fr_inria_omftest'
    #]
    #algorithm_scenarios = [
    #    'EnergyUnawareStrategyPlacement',
    #    'OpenOptStrategyPlacement',
    #    'EvolutionaryComputationStrategyPlacement'
    #]
    ## Setup the scenarios
    #host_scenarios = range(10, 110, 10)
    #simulation_scenarios = range(1, 31)

    #host_scenarios = range(200, 210, 10)
    #simulation_scenarios = range(1, 31)

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
