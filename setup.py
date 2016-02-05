import io
from setuptools import setup, find_packages

from meetup import __version__

package_data = {
    'api_specification': ['api_specification/*.json']}


readme_file = io.open('README.rst', encoding='utf-8')

with readme_file:
    long_description = readme_file.read()

setup(
    name='meetup-api',
    version=__version__,
    packages=find_packages(),
    include_package_data=True,
    package_data=package_data,
    url='https://github.com/pferate/meetup-api',
    license='MIT',
    author='Pat Ferate',
    author_email='',
    description='Python API for Meetup',
    long_description=long_description,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Internet :: WWW/HTTP',
    ],
    keywords="meetup api",
    install_requires=['requests', 'six'],
    tests_require=['pytest'],
)
