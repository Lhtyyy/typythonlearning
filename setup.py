import os
from setuptools import setup
from pip._internal.req import parse_requirements

CURRENT_PATH = os.path.dirname(__file__)
REQUIREMENTS_TEXT_PATH = os.path.join(CURRENT_PATH, 'requirements.txt')


def load_requirements():
    return [str(r.requirement) for r in parse_requirements(REQUIREMENTS_TEXT_PATH, 'test')]


def load_long_description():
    return open('README.md').read()


setup(
    python_requires='>=3.9',
    name='ty-python-learning',  # 包名
    version='0.0.2',  # 版本号
    author='youth_ty',
    author_email='youth_ty@163.com',
    description='python learning',
    long_description=load_long_description(),
    long_description_content_type='text/markdown',
    url='',  # 项目主页地址
    package_dir={"": "src"},  #
    include_package_data=False,  # 是否需要打包 .py 以外的其他文件
    package_data={
        'datas': ['data_path', 'template/*']
    },
    install_requires=load_requirements(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
