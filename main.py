import os
from colorama import Fore, Style
from amateur_bands import AmateurBands
from qso_recorder import QSORecorder

def main():
    amateur_bands = AmateurBands.from_config_file("config.ini")
    recorder = QSORecorder.from_bands(amateur_bands)

    recorder.MY_CALL = input(Fore.GREEN + "Enter your callsign: " + Style.RESET_ALL).upper()
    adif_filename = input(Fore.GREEN + "Enter the path to save the ADIF file: " + Style.RESET_ALL)

    if not adif_filename.endswith(".adif"):
        adif_filename += ".adif"

    if not os.path.exists(adif_filename):
        with open(adif_filename, "w") as f:
            f.write("ADIF Export\n")

    while True:
        print("\n" + Fore.MAGENTA + "Record a new contact (type 'exit' to quit):" + Style.RESET_ALL)
        qso_data = recorder.record_contact()

        if qso_data == "exit":
            break

        with open(adif_filename, "a") as f:
            f.write("<EOH>\n")
            f.write(qso_data + "\n")
            f.write("<EOR>\n")
        print(Fore.YELLOW + "Contact recorded successfully." + Style.RESET_ALL)

    print(Fore.BLUE + "Goodbye!" + Style.RESET_ALL)

if __name__ == "__main__":
    main()
