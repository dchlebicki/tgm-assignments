from setuptools import setup

setup(
    name='todo list',
    packages=['application'],
    include_package_data=True,
    install_requires=[
        'flask',
    ],
)