from setuptools import setup, find_packages

setup(
    name='ft_package',
    version='0.0.1',
    description='Un package pour compter les occurrences dans une liste',
    author='abourdon',
    author_email="abourdon@42.fr",
    url="https://github.com/kolitoo/Python-Data-Piscine42/tree/main/Module_00/ex09",
    packages=find_packages(),
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    entry_points={
        'console_scripts': [],
    },
)