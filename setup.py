setup(
    name="python20-video downloader",
    version="0.1.0",
    description="Downloads YouTube Videos",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/python-20/video-downloader",
    author="Python 20 Team",
    author_email="",
    license="GPL-3.0",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Operating System :: Microsoft :: Windows",
        "Topic :: Multimedia :: Video",
        "Topic :: Multimedia :: Sound/Audio",
        "Natural Language :: English",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python :: 3",
    ],
    packages=["youtubedl"],
    include_package_data=True,
    install_requires=[
        "PyQt5", "PyQt5-sip", "pytube3", "typing-extensions"
    ],
    entry_points={"console_scripts": ["realpython=reader.__main__:main"]},
)
