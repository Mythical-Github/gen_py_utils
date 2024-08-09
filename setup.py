from setuptools import setup, find_packages

setup(
    name='gen_py_utils',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'psutil',
    ],
    include_package_data=True,
    description='',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Mythical-Github/gen_py_utils',
    author='Mythical',
    author_email='mythicaldata.com',
    license='GPL-3.0',
)
