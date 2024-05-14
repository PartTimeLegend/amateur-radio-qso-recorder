import configparser

class AmateurBands:
    def __init__(self, bands):
        self.bands = bands

    @classmethod
    def from_config_file(cls, config_file):
        config = configparser.ConfigParser()
        config.read(config_file)
        bands = {band: tuple(map(float, freq_range.split(','))) for band, freq_range in config['AmateurBands'].items()}
        return cls(bands)

    def validate_frequency(self, frequency):
        try:
            freq = float(frequency)
            for _, (lower, upper) in self.bands.items():
                if lower <= freq <= upper:
                    return True
            return False
        except ValueError:
            return False
