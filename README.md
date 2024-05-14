# Amateur Radio QSO Recorder

This Python script allows amateur radio operators to record their contacts and save them to an ADIF (Amateur Data Interchange Format) file. The script prompts the user for the contacted callsign, frequency, mode, and saves the contact details to the specified ADIF file.

## Features

- Record amateur radio contacts and save them to an ADIF file.
- Validate frequency to ensure it is within the amateur radio allocations.
- Supports different bands defined in a configuration file.
- User-friendly command-line interface.
- Colourised output for improved readability.

## Installation

1. Clone this repository to your local machine.
2. Install the required dependencies by running `pip install -r requirements.txt`.
3. Run the script by executing `python main.py`.

## Usage

1. When prompted, enter your callsign and the path to save the ADIF file.
2. Follow the prompts to record each contact.
3. Type `exit` to quit the program.

## Configuration

You can customise the amateur radio bands and their frequency ranges by editing the `config.ini` file.

## Dependencies

- [colorama](https://pypi.org/project/colorama/): For colourising the command-line output.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
