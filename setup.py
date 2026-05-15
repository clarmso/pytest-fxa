# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from setuptools import setup

setup(
    version="1.7.0",
    name="pytest-fxa-mte",
    description="pytest plugin for Firefox Accounts",
    long_description=open("README.rst").read(),
    author="Dave Hunt",
    author_email="dhunt@mozilla.com",
    url="https://github.com/clarmso/pytest-fxa",
    maintainer="Clare So",
    maintainer_email="cso@mozilla.com",
    packages=["pytest_fxa"],
    install_requires=["PyFxA"],
    setup_requires=["setuptools_scm"],
    entry_points={"pytest11": ["fxa = pytest_fxa.plugin"]},
    license="MPL-2.0",
    keywords="py.test pytest mozilla automation firefox account fxa",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Framework :: Pytest",
        "Intended Audience :: Developers",
        "Operating System :: POSIX",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: MacOS :: MacOS X",
        "Topic :: Software Development :: Quality Assurance",
        "Topic :: Software Development :: Testing",
        "Topic :: Utilities",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Programming Language :: Python :: 3.14",
        "Programming Language :: Python :: Implementation :: CPython",
    ],
)
