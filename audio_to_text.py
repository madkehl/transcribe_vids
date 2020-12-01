import speech_recognition as sr
import time


def aud_to_text(path=None):
    """
    Takes audio and converts it to text.  Audio must be around 1 minute in length
    :param path: Gives path to temporarily store the audio segments
    :return: transcript for the segment in question
    """
    if path is None:
        path = './trial/trial.wav'
    r = sr.Recognizer()
    audio = sr.AudioFile(path)
    with audio as source:
        audio_file = r.record(source)
    result = r.recognize_google(audio_file, language='en-US', show_all=True)
    if len(result) > 0:
        print(result['alternative'][0])
        return result['alternative'][0]['transcript']


def aud_to_text_ls(count):
    """
    In instances where the file is too large to be handled by the free api, iterates through list of split files
    :param count: Number of files to expect
    :return: the full transcript concatenated. Can sometimes duplicate a few words at the beginning and end
    """
    sub_files = range(count + 1)
    full_transcript = ""
    for i in sub_files:
        path = './trial/' + str(i) + '_trial.wav'
        result = aud_to_text(path)
        try:
            full_transcript = full_transcript + result + ' '
        except TypeError:
            pass
        # trying to throw the api off
        time.sleep(5)

    return full_transcript
