from setuptools import setup, find_packages

setup(name='JargonProfiler',
      version='0.1',
      description='Assessing the jargon content of texts and speech',
      url='https://github.com/ejh243/MunroeJargonProfiler',
      author='Eilis Hannon, Jonathan Cooper, Mateusz Kuzak, Raniere Silva, Andrew Hufton, Emma Tattershall',
      author_email='',
      license='MIT',
      classifiers=['Development Status :: 3 - Alpha',
                   'Programming Language :: Python',
                   'Programming Language :: Python :: 3',
                   'Operating System :: OS Independent',
                   'Intended Audience :: Science/Research',
                   'License :: OSI Approved :: MIT License'],
      install_requires=['nltk'],
      python_requires='>=3.3',
      packages=find_packages('jargonprofiler', exclude=['*test']),
      package_data={
          # If any (sub-)package contains *.txt files, include them:
          '': ['*.txt']
      },
      zip_safe=False
      )
