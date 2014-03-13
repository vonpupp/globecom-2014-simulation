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
TraceAnalizer :: A VM trace analyzer
"""
__version__ = "0.1"
__author__  = "Albert De La Fuente"


# Add relative path for other imports
import sys
sys.path.append("../../")

from distsim.managers.simmanager import Simulator
from distsim.model.traceanalize import TraceAnalize
import argparse
import os


if __name__ == "__main__":
    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    
    t = TraceAnalize()
    t.csv_write_header(dname + '/traces.csv')

    # Change current directory
    os.chdir(dname + '/../../')
    traces_root = dname + '/../../' + 'planetlab-workload-traces'

    try:
        for root, dirs, files in os.walk(traces_root):
            if '.git' in dirs:
                dirs.remove('.git')
            #if '.git' in subFolders:
            #    subFolders.remove('.git')
            for basename in files:
                if basename[0] is not '.':
                    filename = os.path.join(root, basename)
                    data = t.analyze(filename)
                    t.csv_append_row()
    except:
        print('exception with file: {}'.format(filename))
    finally:
        t.csv_close()

#    if not os.path.exists(output_path):
#        os.makedirs(output_path)
    print('done')
