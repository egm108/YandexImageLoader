import setuptools

with open("README.md") as file:
    read_me_description = file.read()

setuptools.setup(
    name="yil",
    version="0.1",
    author="egm108",
    author_email="egm@yandex.ru",
    description="Yandex image loader",
    long_description=read_me_description,
    long_description_content_type="text/markdown",
    url="https://github.com/egm108/YandexImageLoader/tree/main",
    packages=['yil'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
)