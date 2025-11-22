import instaloader
from pathlib import Path
from os import makedirs

DOWNLOAD_DIR = "downloads"


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
    print(
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
                print("Reached maximum number of posts to download.")
                break

            if position < start_post:
                print(f"Skipping post {position}: {post.shortcode}")
                skipped_latest += 1
                position += 1
                continue

            if not post.is_video:
                print(f"Skipping photo post: {post.shortcode}")
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
            print(f"Downloaded posts {downloaded}: {post.shortcode}")
            position += 1

        total_skipped = skipped_latest + skipped_media
        print(f"\nSkipped latest posts: {skipped_latest}")
        print(f"Skipped photo posts: {skipped_media}")
        print(f"Total skipped posts: {total_skipped}")
        print(f"Total downloaded posts: {downloaded}")
        print("Done!")

    except instaloader.exceptions.ProfileNotExistsException:
        print("❌ Profile not found.")
        return
    except instaloader.exceptions.LoginRequiredException:
        print("❌ Login required for this profile.")
        return
    except Exception as e:
        print("❌ Error:", e)
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
    print(
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
                print("Reached maximum number of posts to download.")
                break

            if position < start_post:
                print(f"Skipping post {position}: {post.shortcode}")
                skipped_latest += 1
                position += 1
                continue

            if post.is_video:
                print(f"Skipping video post: {post.shortcode}")
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
            print(f"Downloaded posts {downloaded}: {post.shortcode}")
            position += 1

        total_skipped = skipped_latest + skipped_media
        print(f"\nSkipped latest posts: {skipped_latest}")
        print(f"Skipped video posts: {skipped_media}")
        print(f"Total skipped posts: {total_skipped}")
        print(f"Total downloaded posts: {downloaded}")
        print("Done!")

    except instaloader.exceptions.ProfileNotExistsException:
        print("❌ Profile not found.")
        return
    except instaloader.exceptions.LoginRequiredException:
        print("❌ Login required for this profile.")
        return
    except Exception as e:
        print("❌ Error:", e)
        return


# Execute
download_public_photos(username="ar.guto", max_posts=10, start_post=1)
download_public_videos(username="ar.guto", max_posts=5, start_post=1)
