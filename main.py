from audio_to_text import aud_to_text, aud_to_text_ls
from SplitWav import SplitWavAudio
import moviepy.editor as mp
import os
import shutil


def full_path_to_txt(movie_path, file_name, split=True):
    """
    :param movie_path: str representing link to mp4
    :param file_name: str representing the desired name of final file
    :param split: whether or not the file has to be split to get around API limitations
    :return: None, writes text to file
    """
    clip = mp.VideoFileClip(movie_path)
    current_vid = file_name
    os.mkdir('./trial')
    clip.audio.write_audiofile(r'./trial/trial.wav')

    folder = './trial'
    file = 'trial.wav'

    if split:
        split_wav = SplitWavAudio(folder, file)
        count = split_wav.multiple_split(min_per_split=1)
        full_transcript = aud_to_text_ls(count)
    else:
        full_transcript = aud_to_text()

    shutil.rmtree(folder)
    text_file = open(current_vid, "w")
    text_file.write(full_transcript)
    text_file.close()


def main():
    """
    Iterates through data dir, running conversion pipeline as appropriate
    :return: nothing, fills up folder using full_path_to_text
    """
    data_dir = r'./data'
    for subdir, dirs, files in os.walk(data_dir):
        for filename in files:
            if filename == '4047124581474259204.mp4':
                filepath = subdir + os.sep + filename
                if filepath.endswith(".mp4"):
                    current_vid = filename.replace("mp4", "txt")
                    size = os.stat(filepath).st_size
                    if size > 3000000:
                        split_bool = True
                    else:
                        split_bool = False
                    full_path_to_txt(filepath, current_vid, split=split_bool)


if __name__ == '__main__':
    main()
