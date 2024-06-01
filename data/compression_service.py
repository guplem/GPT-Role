from utils.singleton import Singleton


class CompressionService(metaclass=Singleton):

    @staticmethod
    def compress_summaries(summaries:[str]) -> [str]:
        print("Compressing summaries...")
        # TODO: Compress summaries
        return summaries