from setuptools import setup

setup(name='melbdjango-joke',
      version='0.1',
      description='Lulz',
      url='http://github.com/GVRV/melbdjango-demo/',
      author='Gaurav Dadhania',
      author_email='gaurav@dadhania.in',
      license='MIT',
      packages=['thejoke'],
      install_requires=[
          'sh'
      ],
      zip_safe=False)
