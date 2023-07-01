from setuptools import setup

setup(
    name='Tool',
    version='1.0',
    py_modules=['main'],
    install_requires=['Click'],
    entry_points={
        'console_scripts':[
            'tool = main:main'
        ]
    }
)