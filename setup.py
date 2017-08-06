#!/usr/bin/env python

from setuptools import setup

setup(name="marginAlign",
      version="1.2.0",
      description="Toil-based functions for performing MinION sequence analysis",
      author="Benedict Paten and Art Rand",
      author_email="arand@soe.ucsc.edu",
      url="https://github.com/UCSC-nanopore-cgl/marginAlign",
      packages=['src'],
      # install_requires=["numpy>=1.9.2",
      #                   "h5py>=2.2.1",
      #                   "pysam>=0.8.2.1",
      #                   "pandas>=0.18.1",
      #                   "sonLib>=1.1.0",
      #                   "PyYAML>=3.12"]
      )
