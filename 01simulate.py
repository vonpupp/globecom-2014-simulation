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
2014 SBRC Simulations
"""
__version__ = "0.1"
__author__ = "Albert De La Fuente"


import argparse
import os
from scenariosvars import *

def get_default_arg(default_value, arg):
    if arg is None:
        return default_value
    else:
        return arg

if __name__ == "__main__":
    seu = 0
    sksp = 0
    sec = 0
    seccpu = 1

    eu_params = ''
    ksp_params = ''
    ec_params = ''
    if seu == 1:
        eu_params = '-seu 1'
    if sksp == 1:
        ksp_params = '-sksp 1'
    if sec == 1:
        ec_params = '-sec 1'
    if seccpu == 1:
        ec_params = '-seccpu 1'

    #trace_scenarios = [
    #    'planetlab-workload-traces/20110409/146-179_surfsnel_dsl_internl_net_root',
    #    'planetlab-workload-traces/20110409/host4-plb_loria_fr_uw_oneswarm',
    #    'planetlab-workload-traces/20110420/plgmu4_ite_gmu_edu_rnp_dcc_ufjf',
    #
    #    'planetlab-workload-traces/20110309/planetlab1_fct_ualg_pt_root',
    #    'planetlab-workload-traces/20110325/host3-plb_loria_fr_inria_omftest',
    #    'planetlab-workload-traces/20110412/planetlab1_georgetown_edu_nus_proxaudio',
    #
    #    'planetlab-workload-traces/20110306/planetlab1_dojima_wide_ad_jp_princeton_contdist',
    #    'planetlab-workload-traces/planetlab-selected/planetlab-20110409-filtered_planetlab1_s3_kth_se_sics_peerialism',
    #    'planetlab-workload-traces/20110322/planetlab-wifi-01_ipv6_lip6_fr_inria_omftest'
    #]
    #
    ## Setup the scenarios
    #host_scenarios = range(10, 110, 10)
    #simulation_scenarios = range(1, 31)

    # Change current directory
    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    os.chdir(dname + '/' + 'pyCloudSim')

    # Start the simulation
    for trace in trace_scenarios:
        for host in host_scenarios:
            for simulation in simulation_scenarios:
                command = 'python distsim.py -t {} -o {} -pm {} -vma 16 -vmo 304 -vme 16 {} {} {}'\
                        .format(trace, dname + 'results', host, eu_params, ksp_params, ec_params)
                os.system(command)

    print('done')
