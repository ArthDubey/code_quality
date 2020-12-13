from setuptools import setup

with open("README-pypi.md", "r") as fh:
    long_description = fh.read()

setup(
    name="code_quality",
    packages=["code_quality"],
    version="0.0.4",
    license="MIT",
    install_requires=["termcolor"],
    description="A light-weight library for testing code quality.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Arth Dubey",
    author_email="arthdubey07@gmail.com",
    url="https://github.com/ArthDubey/code_quality",
    download_url="https://github.com/ArthDubey/code_quality/archive/v_01.gz",
    keywords=["test", "quality", "principles", "linter", "testing"],
    classifiers=['Intended Audience :: Developers',
                 'License :: OSI Approved :: MIT License', 'Programming Language :: Python :: 3']
)
