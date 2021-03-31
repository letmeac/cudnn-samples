import os
import sys

base_dir = sys.argv[1]

try:
    os.system('MSBUILD_UTIL.bat rnnCUDNN_vs2010.sln x64 Release ' ' %s' % (base_dir))
except Exception as e:
    raise e
    #print 'Even if MSBUILD is special here, binary is generated successfully, so ignore this exception'