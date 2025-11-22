import instaloader
from pathlib import Path
from os import makedirs
from datetime import datetime

DOWNLOAD_DIR = "downloads"
LOG_FILE = Path(DOWNLOAD_DIR) / "logs.log"


def log_message(message: str):
    """Log message to both terminal and file with timestamp"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] {message}"
    print(log_entry)
    
    # Ensure logs directory exists
    LOG_FILE.parent.mkdir(parents=True, exist_ok=True)
    
    # Append to log file
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(log_entry + "\n")


def download_public_videos(username: str, max_posts: int = 10, start_post: int = 1):
    """
    Download latest public videos from an Instagram profile.
    max_posts limits the number of posts downloaded.
    Each post gets its own folder named by the post's timestamp.
    """
    loader = instaloader.Instaloader(
        download_videos=True,
        download_video_thumbnails=True,
        download_comments=False,
        save_metadata=False,
        compress_json=False,
    )

    # Public profiles don't need login
    log_message(
        f"Downloading videos up to {max_posts} latest posts from @{username}, "
        f"starting from post {start_post}..."
    )

    try:
        profile = instaloader.Profile.from_username(loader.context, username)

        position = 1
        downloaded = 0
        skipped_latest = 0
        skipped_media = 0
        for post in profile.get_posts():
            if downloaded >= max_posts:
                log_message("Reached maximum number of posts to download.")
                break

            if position < start_post:
                log_message(f"Skipping post {position}: {post.shortcode}")
                skipped_latest += 1
                position += 1
                continue

            if not post.is_video:
                log_message(f"Skipping photo post: {post.shortcode}")
                skipped_media += 1
                position += 1
                continue

            # Create post folder (for organization/reference later)
            post_timestamp = post.date_utc.strftime("%Y-%m-%d_%H-%M-%S_UTC")
            post_folder = Path(DOWNLOAD_DIR) / username / post_timestamp
            makedirs(post_folder, exist_ok=True)

            loader.download_post(
                post, target=Path("downloads") / username / post_timestamp
            )
            downloaded += 1
            log_message(f"Downloaded posts {downloaded}: {post.shortcode}")
            position += 1

        total_skipped = skipped_latest + skipped_media
        log_message(f"Skipped latest posts: {skipped_latest}")
        log_message(f"Skipped photo posts: {skipped_media}")
        log_message(f"Total skipped posts: {total_skipped}")
        log_message(f"Total downloaded posts: {downloaded}")
        log_message("Done!")

    except instaloader.exceptions.ProfileNotExistsException:
        log_message("❌ Profile not found.")
        return
    except instaloader.exceptions.LoginRequiredException:
        log_message("❌ Login required for this profile.")
        return
    except Exception as e:
        log_message(f"❌ Error: {e}")
        return


def download_public_photos(username: str, max_posts: int = 10, start_post: int = 1):
    """
    Download latest public photos from an Instagram profile.
    max_posts limits the number of posts downloaded.
    Each post gets its own folder named by the post's timestamp.
    """
    loader = instaloader.Instaloader(
        download_videos=False,
        download_video_thumbnails=False,
        download_comments=False,
        save_metadata=False,
        compress_json=False,
    )

    # Public profiles don't need login
    log_message(
        f"Downloading photos up to {max_posts} latest posts from @{username}, "
        f"starting from post {start_post}..."
    )

    try:
        profile = instaloader.Profile.from_username(loader.context, username)

        position = 1
        downloaded = 0
        skipped_latest = 0
        skipped_media = 0
        for post in profile.get_posts():
            if downloaded >= max_posts:
                log_message("Reached maximum number of posts to download.")
                break

            if position < start_post:
                log_message(f"Skipping post {position}: {post.shortcode}")
                skipped_latest += 1
                position += 1
                continue

            if post.is_video:
                log_message(f"Skipping video post: {post.shortcode}")
                skipped_media += 1
                position += 1
                continue

            # Create post folder (for organization/reference later)
            post_timestamp = post.date_utc.strftime("%Y-%m-%d_%H-%M-%S_UTC")
            post_folder = Path(DOWNLOAD_DIR) / username / post_timestamp
            makedirs(post_folder, exist_ok=True)

            loader.download_post(
                post, target=Path("downloads") / username / post_timestamp
            )
            downloaded += 1
            log_message(f"Downloaded posts {downloaded}: {post.shortcode}")
            position += 1

        total_skipped = skipped_latest + skipped_media
        log_message(f"Skipped latest posts: {skipped_latest}")
        log_message(f"Skipped video posts: {skipped_media}")
        log_message(f"Total skipped posts: {total_skipped}")
        log_message(f"Total downloaded posts: {downloaded}")
        log_message("Done!")

    except instaloader.exceptions.ProfileNotExistsException:
        log_message("❌ Profile not found.")
        return
    except instaloader.exceptions.LoginRequiredException:
        log_message("❌ Login required for this profile.")
        return
    except Exception as e:
        log_message(f"❌ Error: {e}")
        return


# Execute
download_public_photos(username="ar.guto", max_posts=10, start_post=1)
download_public_videos(username="ar.guto", max_posts=5, start_post=1)
