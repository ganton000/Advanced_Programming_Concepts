from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

ext_modules = [
    Extension("first_module",  ["working_with_cython.pyx"]),
]

for e in ext_modules:
    e.cython_directives = {'language_level': "3"}

setup(
    name = 'My Cythonized Python Program',
    cmdclass = {'build_ext': build_ext},
    ext_modules = ext_modules
)
