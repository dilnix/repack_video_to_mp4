# Python script to repack video files to MP4

Born as a simple solution for batch repacking videos from any specified container (extension) to MP4.
The default source container (extension) is MKV.

## How to use it

- Copy the single Python file `main.py` to the folder which contains the target video files, required to be repacked.
- Run `python main.py` or `chmod +x main.py && ./main.py` in terminal from that folder.

## How it works

The only one source container (extension) can be used with a single execution. For example, if your set of videos have different containers (extensions), like MKV and AVI, you need 2 executions of the script to target repacking process for both containers (executions).

Once you execute the script, it will ask you for the source extension. If it is MKV, you can simply type nothing and push Return button, as the MKV is the default value.

While processing file-by-file with repacking to MP4, script will ask you about the requirement to keep or delete the source video file. The default value is to keep, if you will simply push Return button.

The number of video/audio/subtitle streams are calculated automatically. Subtitles are automatically converted to `mov_text` format, as it's usual for MP4. Video/audio streams are copied as they are.

## Requirements

- `ffmpeg` with `ffprobe`
- Python 3.8 or greater

**It is very important to remember that it's users responsibility to check if the video/audio streams provided in the source files are compatible with MP4 container**

For example, video streams must be encoded with AVC (H264) or HEVC (H265), audio streams must be encoded with AAC or E-AC3. Other codecs may be incompatible.

## TODO

- [ ] checking of the video/audio codec for each file before processing repacking with a warning to user
- [ ] option to convert audio from AC3 to E-AC3 or AAC
