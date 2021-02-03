import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


setuptools.setup(
    name="ShazamAPI", # Replace with your own username
    version="10.2",
    author="Numenorean",
    author_email="author@example.com",
    description="Fully reverse engeenired shazam api",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/StarkGang/ShazamAPI",
    install_requires=['requests', 'pydub', 'numpy'],
    packages=setuptools.find_packages(),
    python_requires='>=3.6',
    
)
