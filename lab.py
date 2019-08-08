# Students should not edit this file, since changes here will _only_
# affect how your code runs locally.  It will not change how your code
# executes in the cloud.
 
lab_name = "Characterizing Matrix Multiply"
output_files = ['submission/code.out', 'submission/code-stats.csv', 'submission/code.gprof']
input_files = ['submission/code.c', 'config']
run_cmd = ['make', '-C', 'submission']
clean_cmd = ['make', 'clean']
env = ['CC','CXX','CFLAGS','CXXFLAGS']
repo = "https://github.com/NVSL/CSE141pp-Lab-Characterizing-Matrix-Multiply.git"
reference_tag = "314bfbd09ab3a28b446742234851eeef2c29dcba"
time_limit = 90

valid_options={
    "compiler":
        {
        'gcc' : 
        {'CC': 'gcc',
         'CXX': 'g++'},
        'gcc-8' : 
        {'CC': 'gcc-8',
         'CXX': 'g++-8'},
        'gcc-9' : 
        {'CC': 'gcc-9',
         'CXX': 'g++-9'
         },
        'clang' : 
        {'CC': 'clang',
         'CXX': 'clang++'
         }
        },
    "optimize" :
        {
        '-O0' : 
        {'OPT_FLAGS': '-O0 -mno-mmx'},
        '-O1' : 
        {'OPT_FLAGS': '-O1 -mno-mmx'},
        '-O2' : 
        {'OPT_FLAGS': '-O2 -mno-mmx'},
        '-O3' : 
        {'OPT_FLAGS': '-O3 -mno-mmx'}
        },
    "MHz" : lambda x: {"MHZ": str(int(x))},
    "profiler" :
        {
        'gprof' : 
        {'PROFILE_FLAGS': '-pg',
         'LD_OPTS': '-pg',
         'EXTRA_TARGETS': 'code.gprof'
        },
        },
    }

default_options={
    'compiler' : 'gcc',
    'optimize' : '-O0'
}

figures_of_merit=[
    {
        "file": 'submission/code-stats.csv',
        "field": 'WallTime',
        "name": 'execution_time'
        },
    {
        "file": 'submission/code-stats.csv',
        "field": 'rapl:::PACKAGE_ENERGY:PACKAGE0',
        "name": 'energy'
    }
]
