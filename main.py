import os
import sys


def repack_video_to_mp4(video_path: str, source_ext: str = ".mkv") -> None:
    """
    Repack video to mp4 format
    """
    if not os.path.exists(video_path):
        print("Video path does not exist")
        sys.exit(1)

    # Get video name
    video_name: str = os.path.basename(video_path)

    # Get video name without extension
    video_name_without_extension: str = os.path.splitext(video_name)[0]

    # Get video extension
    video_extension: str = os.path.splitext(video_name)[1]

    # Get video directory
    video_directory: str = os.path.dirname(video_path)

    # Get video name with mp4 extension
    video_name_with_mp4_extension: str = video_name_without_extension + ".mp4"

    # Get video path with mp4 extension
    video_path_with_mp4_extension: str = os.path.join(
        video_directory, video_name_with_mp4_extension)

    # Detect the number of video streams
    video_streams: int = 0
    try:
        video_streams = int(os.popen(
            "ffprobe -v error -select_streams v -show_entries stream=codec_name \
                -of default=noprint_wrappers=1:nokey=1 " + video_path).read().count("\n"))
    except Exception as e:
        print(e)
        sys.exit(1)

    # Detect the number of audio streams
    audio_streams: int = 0
    try:
        audio_streams = int(os.popen(
            "ffprobe -v error -select_streams a -show_entries stream=codec_name \
                -of default=noprint_wrappers=1:nokey=1 " + video_path).read().count("\n"))
    except Exception as e:
        print(e)
        sys.exit(1)

    # Detect the number of subtitle streams
    subtitle_streams: int = 0
    try:
        subtitle_streams = int(os.popen(
            "ffprobe -v error -select_streams s -show_entries stream=codec_name \
                -of default=noprint_wrappers=1:nokey=1 " + video_path).read().count("\n"))
    except Exception as e:
        print(e)
        sys.exit(1)

    # Set map string for video/audio/subtitle number of streams
    map_number: int = video_streams + audio_streams + subtitle_streams
    map_string: str = " ".join(
        f"-map 0:{i}" for i in range(map_number))

    # Repack video to mp4 format
    if video_extension.lower() == source_ext:
        try:
            os.system(
                f"ffmpeg -y -i {video_path} {map_string} -c:v copy -c:a copy \
                    -disposition:a:0 default -c:s mov_text {video_path_with_mp4_extension}")
        except Exception as e:
            print(e)
            sys.exit(1)

    # Remove original video
    remove_trigger: str = input(
        f"Do you want to remove original video ({video_name})? (y/N): ") or "n"
    if remove_trigger.lower() == "y":
        os.remove(video_path)


if __name__ == "__main__":
    source_ext: str = input(
        "Enter source extension to repack (default: mkv): ").lower() or "mkv"
    for _dir, _, files in os.walk(os.getcwd()):
        for file in files:
            if file.endswith(source_ext):
                repack_video_to_mp4(os.path.join(_dir, file), "." + source_ext)
