import datetime
from colorama import Fore, Style
from datetime import timezone

class QSORecorder:
    def __init__(self, bands):
        self.MY_CALL = ""
        self.amateur_bands = bands

    @classmethod
    def from_bands(cls, bands):
        return cls(bands)

    def record_contact(self):
        while True:
            callsign = input(Fore.CYAN + "Enter contacted callsign: " + Style.RESET_ALL).upper()
            if callsign.strip().lower() == "exit":
                return "exit"
            
            while True:  # Loop until a valid frequency is provided
                frequency = input(Fore.CYAN + "Enter frequency (in MHz): " + Style.RESET_ALL)
                if frequency.strip().lower() == "exit":
                    return "exit"
                if not self.amateur_bands.validate_frequency(frequency):
                    print(Fore.RED + "Invalid frequency. Please enter a frequency within amateur radio allocations." + Style.RESET_ALL)
                else:
                    break  # Exit the loop if frequency is valid

            mode = input(Fore.CYAN + "Enter mode (e.g., SSB, CW, FT8): " + Style.RESET_ALL)
            if mode.strip().lower() == "exit":
                return "exit"
            
            time = datetime.datetime.now(timezone.utc).strftime("%Y%m%d%H%M%S")

            qso_data = f"<QSO_DATE:{len(time)}>{time}<TIME_ON:{len(time)}>{time}<MY_CALL:{len(self.MY_CALL)}>{self.MY_CALL}<CALL:{len(callsign)}>{callsign}<FREQ:{len(frequency)}>{frequency}<MODE:{len(mode)}>{mode}"
            return qso_data
