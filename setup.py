from setuptools import setup, find_packages

setup(
    name='maillogsearch',
    version='0.1.0',
    packages=find_packages(exclude=['tests']),
    url='',
    license='',
    author='akozyrev',
    author_email='kozirev8@gmail.com',
    description='This is library created for interview exercise',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    python_requires='>=3.5, <4',
    install_requires=[],
)
