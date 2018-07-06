import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="yourpackage",
    version="0.0.1",
    author="Christopher Simpson",
    author_email="enquiries@karmacomputing.co.uk",
    description="A simple cli app",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://karmacomputing.co.uk",
    packages=setuptools.find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
    ],
    classifiers=(
        "Programming Language :: Python :: 2",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
    ),
    entry_points={
        'console_scripts': [
            'cliapp = cliapp.scripts.cli:cli',
        ]
    },
)
