import re
import sys

def main():
    print(parse(input("HTML: ")))

def parse(s):
    # Regular expression to match the src attribute of an iframe element with a YouTube URL
    pattern = re.compile(r'src="(https?://(?:www\.)?youtube\.com/embed/[\w-]+)"')
    match = pattern.search(s)
    if match:
        # Extract the video ID from the matched URL and convert to youtu.be format
        url = match.group(1)
        video_id = url.split('/')[-1]
        return f"https://youtu.be/{video_id}"
    return None

if __name__ == "__main__":
    main()
