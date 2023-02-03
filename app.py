import streamlit as st
import pytube

def download_video(url, quality='360p'):
    yt = pytube.YouTube(url)
    video = yt.streams.filter(file_extension='mp4', resolution=quality).first()
    video.download(filename=yt.title)
    st.write(f"{yt.title} video successfully downloaded in {quality} quality")

def download_audio(url, quality='128kbps'):
    yt = pytube.YouTube(url)
    audio = yt.streams.filter(only_audio=True, abr=quality).first()
    audio.download(filename=yt.title)
    st.write(f"{yt.title} audio successfully downloaded in {quality} quality")

if __name__ == '__main__':
    st.title("YouTube Video and Audio Downloader")
    url = st.text_input("Enter the YouTube video URL: ")
    video_quality = st.selectbox("Select the desired video quality:", ('240p', '360p', '480p', '720p', '1080p'), index=1)
    audio_quality = st.selectbox("Select the desired audio quality:", ('64kbps', '128kbps', '192kbps'), index=1)
    if st.button("Download"):
        download_video(url, video_quality)
        download_audio(url, audio_quality)
