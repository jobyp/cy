from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

ext_modules = [(Extension("hello", ["hw.pyx"]))]

setup(name = 'Hello App',
      cmdclass = {'build_ext' : build_ext },
      ext_modules = ext_modules)



