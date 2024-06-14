import re
from setuptools import setup, find_packages

# Load version from module (without loading the whole module)
with open('pyproject.toml', 'r') as fo:
    version = re.search(r'^version\s*=\s*[\'"]([^\'"]*)[\'"]',
                        fo.read(), re.MULTILINE).group(1)

# Read in the README.md for the long description.
with open('README.md') as fo:
    content = fo.read()
    long_description = content
    description = "Kafka and RabbitMQ message brokers"

setup(
    name='messagebrokerstumeke',
    version=version,
    url='https://github.com/tumeke-tech/messagebrokers-tumeke',
    author='Sergei Kazakov',
    author_email='kazakov.s.fl@gmail.com',
    description=description,
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='GPLv3+',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    test_suite='',
    install_requires=[],
    keywords='',
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)