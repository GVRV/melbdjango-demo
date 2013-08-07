from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='melbdjango-joke',
      version='0.1',
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
      zip_safe=False)
