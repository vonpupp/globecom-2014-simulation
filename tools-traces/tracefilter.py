#!/usr/bin/python
# vim:ts=4:sts=4:sw=4:et:wrap:ai:fileencoding=utf-8:

# Add relative path for other imports
import sys
sys.path.append("../pyCloudSim/")

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
