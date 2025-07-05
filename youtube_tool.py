from agno.tools import tool

from youtube_transcript_api import YouTubeTranscriptApi

import re



@tool

def youtube_tool(url: str) -> str:

    """

    Summarize a YouTube video by fetching and trimming the transcript.



    Args:

        url (str): The full YouTube video URL.



    Returns:

        str: A brief summary or error message.

    """

    try:

        video_id = extract_video_id(url)

        transcript = YouTubeTranscriptApi.get_transcript(video_id)

        first_10_segments = [segment["text"] for segment in transcript[:10]]

        summary = " ".join(first_10_segments)

        return f"📄 Transcript Summary Preview:\n{summary}"

    except Exception as e:

        return f"❌ Error: {str(e)}"



def extract_video_id(url: str) -> str:

    """

    Extracts the video ID from a YouTube URL.

    Supports both full and short YouTube links.



    Args:

        url (str): YouTube URL



    Returns:

        str: Video ID

    """

    patterns = [

        r"(?:v=|\/)([0-9A-Za-z_-]{11})(?:[&?]|\s|$)",  # full URLs

        r"youtu\.be\/([0-9A-Za-z_-]{11})"              # shortened URLs

    ]

    for pattern in patterns:

        match = re.search(pattern, url)

        if match:

            return match.group(1)

    raise ValueError("Could not extract video ID from URL.")
