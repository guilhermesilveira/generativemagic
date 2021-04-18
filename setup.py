import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="generativemagic",
    version="0.8.0",
    author="Guilherme Silveira",
    author_email="guilherme.silveira@gmail.com",
    description="Generative magic uses computer science, mathematics, design and statistics to generate new magic.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/guilhermesilveira/generativemagic",
    project_urls={},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(include=["generativemagic*"]),
    python_requires=">=3.6",
    install_requires=["numpy>=1.20.1", "pandas>=1.2.3", "z3-solver>=4.8.10", "tqdm>=4.59"],
    tests_require=["pytest>=6.2.2"],
    test_suite='tests',
)
