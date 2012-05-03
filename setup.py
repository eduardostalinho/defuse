import sys
import setuptools

setuptools.setup(
    name="defuse",
    version="0.1",
    packages=["defuse",],
    install_requires=["fuse-python",],
    url="http://github.com/Roger/defuse",
    description="fuse wrapper for pythons",
)

