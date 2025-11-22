# Instagram Posts Downloader

A Python script to download Instagram posts (photos, videos, captions) from public profiles for personal archiving or AI/ML projects.

## Features

- ✅ Download photos, videos, and captions from public Instagram profiles
- ✅ Organize downloads by user profile and post timestamp
- ✅ Configurable post limits and starting position
- ✅ Minimal dependencies
- ✅ No authentication required—simply run the code (no login, no token)

## Prerequisites

- Python 3.8+

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/insta-loader.git
   cd insta-loader
   ```

2. **Create virtual environment**
   ```bash
   python -m venv .venv
   ```

3. **Activate virtual environment**
   - **Windows:**
     ```bash
     .venv\Scripts\activate
     ```
   - **macOS/Linux:**
     ```bash
     source .venv/bin/activate
     ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Change the parameters at the bottom of the script as needed.
```python
download_public_photos(username="ar.guto", max_posts=10, start_post=1)
download_public_videos(username="ar.guto", max_posts=5, start_post=1)
```

## Parameters

- **username** (str): Instagram profile username to download from
- **max_posts** (int): Maximum number of posts to download (default: 10)
- **start_post** (int): Starting position (default: 1)

## Output Structure

Downloads are organized as follows:
```
downloads/
└── [username]/
    ├── [2025-11-07_18-52-50_UTC]/
    │   ├── 2025-11-07_18-52-50_UTC_1.jpg
    │   ├── 2025-11-07_18-52-50_UTC_2.jpg
    │   ├── 2025-11-07_18-52-50_UTC_3.jpg
    │   └── 2025-11-07_18-52-50_UTC.txt  # caption
    └── [2025-11-04_15-18-48_UTC]/
        ├── 2025-11-04_15-18-48_UTC.jpg  # thumbnail
        ├── 2025-11-04_15-18-48_UTC.mp4
        └── 2025-11-04_15-18-48_UTC.txt  # caption
```

Each post is organized in its own folder named by post timestamp in UTC format. The folder contains:
- Image files (`.jpg`) - Photos from the post
- Video file (`.mp4`) - If the post contains video
- Caption file (`.txt`) - Post caption/description

## Configuration

Edit `DOWNLOAD_DIR` in `instagram_posts_downloader.py` to change the default download directory:

```python
DOWNLOAD_DIR = "downloads"  # Change this path
```

For more customization options, refer to the [Instaloader documentation](https://instaloader.github.io/).

## Disclaimer

⚠️ **Ethical Use**: This tool downloads public Instagram content. Respect creators' rights and use downloaded content responsibly.

## Support

Feel free to create an issue or open a pull request on GitHub.
