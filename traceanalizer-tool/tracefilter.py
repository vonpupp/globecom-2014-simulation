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
sys.path.append("../")

#from distsim.model.tracefilter import TraceFilter
import distsim.model.tracefilter as tf


if __name__ == "__main__":
    t = tf.TraceFilter('traces.csv')
#    t.by_mean()
#    data = tf.filter_equals(t.data, 'var', 1000)
#    data = tf.filter_range(t.data, 'var', 1000, 1500)

#    data = tf.filter_range(t.data, 'std', 15, 16)
#    data = tf.filter_equals(data, 'mean', 25)
#    data = tf.filter_equals(data, 'mean', 35)
#    data = tf.filter_equals(data, 'mean', 45)

#    data = tf.filter_range(t.data, 'std', 30, 31)
#    data = tf.filter_equals(data, 'mean', 25)
#    data = tf.filter_equals(data, 'mean', 35)
#    data = tf.filter_equals(data, 'mean', 45)

    data = tf.filter_range(t.data, 'std', 35, 45)
#    data = tf.filter_equals(data, 'mean', 25)
#    data = tf.filter_equals(data, 'mean', 35)
    data = tf.filter_equals(data, 'mean', 45)
    print data
#    t.filter_rows_by_range('var', 1000, 1500)
#    t.csv_write()
#    print data
    print t.filtered_data
    print('done')
