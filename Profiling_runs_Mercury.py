#A.S. This clean's the directory, recompiles the directory, and then runs mercury, keeping time in the process.
import multiprocessing as mp
from subprocess import call
import os
import sys

def execute(dir):
    call('cp mercury6_2.for '+dir+'/.',shell=True)
    call('cp element6.for '+dir+'/.',shell=True)
    call('rm mercury_*.in '+dir+'/.',shell=True)
    call('cp *.in '+dir+'/.',shell=True)
    call('cp *.inc '+dir+'/.',shell=True)
    call('cp clean.sh '+dir+'/.',shell=True)
    os.chdir(dir)
    call('sh clean.sh',shell=True)
    call('gfortran -o mercury6 mercury6_2.for',shell=True)
    call('gfortran -o element6 element6.for',shell=True)
    call('rm eo.txt ET.txt',shell=True)
    call('touch eo.txt',shell=True)
    call('./mercury6 > eo.txt',shell=True)

if __name__== '__main__':
    files = [x[0] for x in os.walk('input_files/')]
    files=files[1:]
    length = len(files)
    pool = mp.Pool(processes=length)
    args=[files[i] for i in xrange(0,length)]
    print args
    pool.map(execute, args)
    pool.close()
    pool.join()
