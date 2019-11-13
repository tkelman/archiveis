from setuptools import setup


setup(
    name='archiveis',
    version='0.0.8',
    description='A simple Python wrapper for the archive.is capturing service',
    author='Ben Welsh',
    author_email='ben.welsh@gmail.com',
    url='http://www.github.com/pastpages/archiveis/',
    packages=('archiveis',),
    include_package_data=True,
    license="MIT",
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'License :: OSI Approved :: MIT License',
    ],
    install_requires=[
        'six',
        'torrequest',
        'click'
    ],
entry_points='''
        [console_scripts]
        archiveis=archiveis.api:cli
    ''',
)
