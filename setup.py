import os

import pkg_resources
from setuptools import setup, find_packages

setup(
    version="1.0",
    name="yt_whisper",
    packages=find_packages(),
    py_modules=["yt_whisper"],
    author="Kewing Jarquin",
    install_requires=[
        'yt-dlp',
        'openai-whisper @ git+https://github.com/openai/whisper.git@main#egg=whisper'
    ],
    description="Genere subtítulos para videos de YouTube usando Whisper",
    entry_points={
        'console_scripts': ['yt_whisper=yt_whisper.cli:main'],
    },
    include_package_data=True,
)
