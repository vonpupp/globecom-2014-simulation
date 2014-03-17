#!/usr/bin/python
# vim:ts=4:sts=4:sw=4:et:wrap:ai:fileencoding=utf-8:

# Add relative path for other imports
import sys
sys.path.append("../pyCloudSim/")

from distsim.model.traceanalize import TraceAnalize
import os


if __name__ == "__main__":
    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)

    t = TraceAnalize()
    t.csv_write_header(dname + '/traces.csv')

    # Change current directory
    os.chdir(dname + '/../')
    traces_root = dname + '/../' + 'planetlab-workload-traces'

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
