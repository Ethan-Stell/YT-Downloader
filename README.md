# YouTube to MP4 Downloader

## Introduction

I often found myself worrying about whether my YouTube video download links were safe. The internet is filled with tools and services that offer to download YouTube videos, but many come with the risk of malware or other unwanted software. That concern led me to develop my own YouTube to MP4 downloader. By creating this tool, I wanted to ensure a safer way to download videos without compromising on video quality or security. This project is the culmination of that effort, using reliable libraries like `pytube` and `moviepy` to handle video downloads and processing.

## Description

This tool allows users to download videos from YouTube and save them as MP4 files on their local machine. It's designed for ease of use, requiring only the video's URL. This project leverages `pytube` for the downloading process, which provides a straightforward and efficient way to access YouTube content. Additionally, `moviepy` is included for potential format conversion, making the tool versatile and capable of handling various video processing tasks.

## Features

- Download videos from YouTube by URL.
- Save videos in MP4 format.
- Downloads videos in the highest resolution available.

## Libraries Used

- **Pytube**: A lightweight, dependency-free Python library (and command-line utility) for downloading YouTube Videos.
- **MoviePy**: A Python module for video editing, which can be used for basic operations (like cuts, concatenations, title insertions), video compositing (a.k.a. non-linear editing), video processing, or to create advanced effects. It can read and write all the most common audio and video formats, including MP4, making it a valuable tool for video conversion and processing.

## Installation

### Prerequisites

- Python 3.8 or above.

### Dependencies

Install `pytube` and `moviepy` using pip:

```bash
pip install pytube moviepy
```

## Getting Started

1. **Clone the repository or download the script.**
    - You can clone the repository using Git with the following command:
    ```bash
    git clone <repository-url>
    ```
    - Or download the script directly from your GitHub repository's page.

2. **Navigate to the script's directory.**
    - Change into the directory where the script is located:
    ```bash
    cd path/to/youtube_to_mp4_downloader
    ```

3. **Install the required libraries.**
    - Run the following command to install `pytube` and `moviepy`:
    ```bash
    pip install pytube moviepy
    ```

## Usage

To use the YouTube to MP4 downloader, follow these steps:

1. **Run the script in your terminal:**
    ```bash
    python youtube_to_mp4_downloader.py
    ```

2. **Input the YouTube URL when prompted.**
    - The script will ask for the YouTube video URL. Paste the URL and press Enter.

The video will be downloaded to a `downloads/` directory at the location of the converter.py file. it will be in the highest resolution available.
