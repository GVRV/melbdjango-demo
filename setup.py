from setuptools import setup
import multiprocessing

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='melbdjango-joke',
      version='0.2',
      description='Lulz',
      long_description=readme(),
      classifiers = [
          'Development Status :: 1 - Planning',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License'
      ],
      keywords = 'melbdjango joke',
      url='http://github.com/GVRV/melbdjango-demo/',
      author='Gaurav Dadhania',
      author_email='gaurav@dadhania.in',
      license='MIT',
      packages=['thejoke'],
      install_requires=[
          'sh'
      ],
      zip_safe=False,
      test_suite='nose.collector',
      tests_require=['nose'],
      scripts=['bin/stupid-script'],
      entry_points={
          'console_scripts': [
              'say-the-joke = thejoke.teller:tell'
          ]
      })
