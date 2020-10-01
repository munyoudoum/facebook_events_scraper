import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="facebook_events_scraper",  # Replace with your own username
    version="0.0.1",
    author="munyoudoum",
    author_email="munyoudoum@gmail.com",
    description="Scrape Facebook page events(recurring and upcoming), and individual event",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/munyoudoum/facebook_events_scraper",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
