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


# These variables are used within both scripts with relative paths references!

trace_scenarios = [
    'hybrid1',
    'hybrid2',
    'hybrid3',
    'hybrid4',
    'hybrid5',
    'hybrid6',
    'hybrid7',
#    '../planetlab-workload-traces/20110409/146-179_surfsnel_dsl_internl_net_root',
#    '../planetlab-workload-traces/20110409/host4-plb_loria_fr_uw_oneswarm',
#    '../planetlab-workload-traces/20110420/plgmu4_ite_gmu_edu_rnp_dcc_ufjf',

#    '../planetlab-workload-traces/20110309/planetlab1_fct_ualg_pt_root',
#    '../planetlab-workload-traces/20110325/host3-plb_loria_fr_inria_omftest',
#    '../planetlab-workload-traces/20110412/planetlab1_georgetown_edu_nus_proxaudio',

#    '../planetlab-workload-traces/20110306/planetlab1_dojima_wide_ad_jp_princeton_contdist',
#    '../planetlab-workload-traces/planetlab-selected/planetlab-20110409-filtered_planetlab1_s3_kth_se_sics_peerialism',
#    '../planetlab-workload-traces/20110322/planetlab-wifi-01_ipv6_lip6_fr_inria_omftest'
]

algorithm_scenarios = [
    'EnergyUnawareStrategyPlacement',
    'OpenOptStrategyPlacement',
    'EvolutionaryComputationStrategyPlacement',
    'OpenOptStrategyPlacementMem',
    'EvolutionaryComputationStrategyPlacementNet',
]

# Setup the scenarios
host_scenarios = range(100, 110, 10)
simulation_scenarios = range(1, 31)
vms_start = 16
vms_stop = 304
vms_step = 16

#host_scenarios = range(10, 20, 10)
#simulation_scenarios = range(1, 2)
#vms_start = 16
#vms_stop = 32
#vms_step = 16
