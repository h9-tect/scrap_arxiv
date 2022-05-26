import sys
try:
    from setuptools import setup, find_packages
except ImportError:
    sys.exit("""Error: Setuptools is required for installation.
 -> http://pypi.python.org/pypi/setuptools""")


with open("requirements.txt", "r") as f:
    reqs = [line.rstrip("\n") for line in f if line != "\n"]
    

setup(
    name = "arxiv_scaraping",
    version = "0.0.1",
    description = "Get arXiv.org metadate within a date range and category",
    author = "Hesham haroon",
    author_email = "heshamharoon19@gmail.com",
    py_modules = [""],
    packages=find_packages(),
    keywords = ["arxiv", "scraper", "api", "citation"],
    license = "MIT",
    classifiers = [
        "Programming Language :: Python :: 3",
        "Operating System :: windows",
        "Development Status :: test",
        "Intended Audience :: Science/Research",
        "Topic :: Text Processing :: Markup :: LaTeX",
        ]
    )

