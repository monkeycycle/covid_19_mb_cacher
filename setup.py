from setuptools import setup
setup(
    name="covid_19_mb_cacher",
    version="0.1.0",
    packages=["covid_19_mb_cacher"],
    entry_points={
        "console_scripts": [
            "covid_19_mb_cacher = covid_19_mb_cacher.__main__:main"
        ]
    },
    author="Michael Pereira",
    author_email="michael@monkeycycle.org",
    description="Simple cacher for Manitoba's COVID-19 data",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    python_requires='>=3.6',    
)

