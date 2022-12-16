import setuptools
with open('requirements.txt') as f:
    required = f.read().splitlines()
setuptools.setup(
    name="fx_rates",
    version="1.0.1",
    author="Rafal Dmitrowski",
    description="Generating fx_rates mix",
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(exclude=['tests']),
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "Operating System :: OS Independent",
    ],
    install_requires=required,
    python_requires='>=3.7'
)

