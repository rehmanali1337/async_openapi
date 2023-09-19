import setuptools
from .chatgpt._metadata import __version__

required_packages = [
    "aiohttp",
]


setuptools.setup(
    name="async-chatgpt-api",
    version=__version__,
    author="Rehman Ali",
    author_email="rehmanali.9442289@gmail.com",
    description="An async API wrapper chatgpt API",
    url="",
    packages=setuptools.find_packages(),
    install_requires=required_packages,
)
