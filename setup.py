from setuptools import setup, find_packages

setup(
    name='general_python_utilities',
    version='0.1',
    packages=find_packages(),
    install_requires=[],
    include_package_data=True,
    package_data={},
    description='A Python module with reusable functions for various projects',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Mythical-Github/general_python_utilities',
    author='Mythical',
    author_email='mythicaldata.com',
    license='GPL3',
)
