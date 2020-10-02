import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="facebook_events_scraper",
    version="0.0.1b3",
    author="munyoudoum",
    author_email="munyoudoum@gmail.com",
    description="Scrape Facebook page events(recurring and upcoming), and individual event on new Facebook Design using Selenium webdriver",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/munyoudoum/facebook_events_scraper",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'selenium>=3.141.0'
    ],
    python_requires='>=3.6',
)
