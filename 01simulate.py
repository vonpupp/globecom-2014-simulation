#!/usr/bin/python
# vim:ts=4:sts=4:sw=4:et:wrap:ai:fileencoding=utf-8:
#
# Copyright 2014 Albert P. M. De La Fuente Vigliotti
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


import argparse
import os
from scenariosvars import *

def get_default_arg(default_value, arg):
    if arg is None:
        return default_value
    else:
        return arg

if __name__ == "__main__":
    seu = 1
    sksp = 1
    sec = 1
    seccpu = 1
    skspmem = 1

    params = ''
    if seu == 1:
        params += '-seu 1 '
    if sksp == 1:
        params += '-sksp 1 '
    if sec == 1:
        params += '-sec 1 '
    if seccpu == 1:
        params += '-seccpu 1 '
    if skspmem == 1:
        params += '-skspmem 1 '

    # Change current directory
    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    os.chdir(dname + '/' + 'pyCloudSim')

    # Start the simulation
    for trace in trace_scenarios:
        for host in host_scenarios:
            for simulation in simulation_scenarios:
                command = 'python distsim.py -t {} -o {} -pm {} -vma 16 -vmo 304 -vme 16 {}'\
                        .format(trace, dname + 'results', host, params)
                os.system(command)

    print('done')
