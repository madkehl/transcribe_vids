from pydub import AudioSegment
import math
# lost the link somewhere, but this is borrowed from a stack overflow answer with very minor modifications


class SplitWavAudio:
    def __init__(self, folder, filename):
        self.folder = folder
        self.filename = filename
        self.filepath = folder + '/' + filename
        self.audio = AudioSegment.from_wav(self.filepath)

    def get_duration(self):
        return self.audio.duration_seconds

    def single_split(self, from_min, to_min, split_filename):
        """
        Splits the file once
        :param from_min:
        :param to_min:
        :param split_filename:
        :return:
        """
        t1 = from_min * 60 * 1000
        t2 = to_min * 60 * 1000
        split_audio = self.audio[t1:t2]
        split_audio.export(self.folder + '/' + split_filename, format="wav")

    def multiple_split(self, min_per_split):
        """
        Splits the file by the amount of time
        :param min_per_split:
        :return:
        """
        total_min = math.ceil(self.get_duration() / 60)
        for i in range(0, total_min, min_per_split):
            split_fn = str(i) + '_' + self.filename
            self.single_split(i, i + min_per_split, split_fn)
            print(str(i) + ' Done')
            if i == total_min - min_per_split:
                print('All split successfully')
                return i
