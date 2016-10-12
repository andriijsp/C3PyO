try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


setup(
    name='c3pyo',
    version='0.0.1',
    description="Python C3 - Chart Library for d3.js",
    keywords='plot, graph, c3, d3',
    author='Ben Keen',
    author_email='bak@benalexkeen.com',
    url='http://github.com/benalexkeen/C3PyO',
    license="MIT",
    # test_suite='tests',
    packages=[
        'c3pyo',
    ],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'python-slugify==1.1.4',
        'Jinja2>=2.8'
    ],
    # entry_points={
    #     'console_scripts': [
    #         'nvd3 = nvd3.NVD3Chart:_main',
    #     ],
    # },
)