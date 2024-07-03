# CLAUDE IMAGE INPUT

This repository allows you to input images and text to CLAUDE using an API key.

## Overview
This project provides a simple interface to interact with CLAUDE, enabling users to input both images and text.

## Requirement
- API key for CLAUDE `os.environ["CLAUDE_API_KEY"]`
- Python 3.7+
- Required Python packages (listed in `requirements.txt`)

## Usage
1. Clone the repository:
    ```bash
    git clone git@github.com:elsy0111/CLAUDE_IMAGE_INPUT.git
    ```
2. Navigate to the project directory:
    ```bash
    cd CLAUDE_IMAGE_INPUT
    ```
3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```
4. Run the application:
    ```bash
    streamlit run main.py
    ```

> [!CAUTION]
> Image input may consume a large number of tokens.


## Features
- Input images to CLAUDE
- Input text to CLAUDE
- Simple and easy-to-use interface

## Reference
- [CLAUDE API Documentation](https://docs.anthropic.com/en/api)

## Author
- [Twitter](https://twitter.com/arcsec_std)

## Licence
This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).
