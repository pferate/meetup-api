from setuptools import setup, find_packages

setup(
    name='meetup-api',
    version='0.0.1',
    packages=find_packages(),
    url='https://github.com/pferate/meetup-api',
    license='MIT',
    author='Pat Ferate',
    author_email='',
    description='Python API for Meetup',
    long_description=open('README.md').read(),
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Internet :: WWW/HTTP',
    ],
    keywords="meetup api",
)
