#!/usr/bin/env python3

from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

requirements = [
    # TODO: package requirements
]

test_requirements = [
    # TODO: test requirements
]

setup(
    name='Space Weather Service',
    version='0.1.0',
    description="Tracking >=10 MeV levels",
    author="Nicole Thompson",
    packages=[
        'space_weather_service',
    ],
    package_dir={'space_weather_service'},
    include_package_data=True,
    install_requires=requirements,
    test_suite='tests',
    tests_require=test_requirements
)
