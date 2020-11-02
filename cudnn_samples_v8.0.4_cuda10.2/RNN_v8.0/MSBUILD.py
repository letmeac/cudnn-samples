import os
import sys

# WAR: Bug 200622838
# Description:
#     Removing the codegen version flag `compute_30` for nvcc specified in `CUDA 9.2.props` to prevent 
#     error from using `compute_30` with CUDA 11. As a proper fix, when testing with CUDA X, the test script should use 
#     correct configuration for CUDA X not `CUDA 9.2.props`     

base_dir = sys.argv[1]

# D:\tmp\dotNet\4.0\MSBuild\Microsoft.Cpp\v4.0\BuildCustomizations\CUDA 9.2.props
# D:\tmp\cuda\_tests\cudnn_tests\RNN\MSBUILD.py

path_cuda_9_2_prop = os.path.join(base_dir, "dotNet", "4.0", "MSBuild", "Microsoft.Cpp", "v4.0", "BuildCustomizations", "CUDA 9.2.props")

with open(path_cuda_9_2_prop, "r") as f:
    updated_prop = ''
    for line in f.readlines():
        if 'compute_30' in line:
            # ignoring line with compute_30
            pass
        else:
            updated_prop += line

with open(path_cuda_9_2_prop, "w") as f:
    f.write(updated_prop)

try:
    os.system('MSBUILD_UTIL.bat rnnCUDNN_vs2010.sln x64 Release ' ' %s' % (base_dir))
except Exception as e:
    raise e
    #print 'Even if MSBUILD is special here, binary is generated successfully, so ignore this exception'