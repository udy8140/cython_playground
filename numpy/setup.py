from setuptools import setup
from Cython.Build import cythonize

setup(
    ext_modules=cythonize(["convolve1.pyx","convolve2.pyx","convolve3.pyx","convolve4.pyx"], annotate=True),
)