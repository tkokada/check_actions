from pathlib import Path
from setuptools import setup
import codecs

here = Path(__file__).resolve().parent

with codecs.open(here / 'requirements.txt', 'r') as fh:
    requirements = [line.replace('\n', '') for line in fh.readlines()]
    requirements = [line.split('==')[0] for line in requirements]

setup(
    name='check_actions',
    version='0.1',
    description='cocado',
    url='https://github.com/tkokada/check_actions',
    license='MIT',
    packages=[
        'check_actions'
    ],
    install_requires=requirements,
    zip_safe=False,
    setup_requires=["pytest-runner"],
    tests_require=["pytest"],
)


