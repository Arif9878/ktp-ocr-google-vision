## Installation (UBUNTU)

KTP OCR needs Python 3+ and tesseract OCR. Currently i'm using Ubuntu 20.0 and its running normaly.

To install tesseract OCR Click [here](https://tesseract-ocr.github.io/tessdoc/Installation.html)

1. Clone GIT Repository
    ```sh
    git clone git@github.com:Arif9878/ktp-ocr-tesseract.git
    ```
2. Go root directory of this project 
    ```sh
    cd ktp-ocr
    ```
3. Optionally to use Virtual ENV (You can skip this step if you want install dependencies globaly)
    ```sh
    virtualenv venv
    source venv/bin/activate
    ```
4. Set Google Credentials
    ```sh
    export GOOGLE_APPLICATION_CREDENTIALS="/home/user/Downloads/service-account-file.json"
    ```
5. Install dependencies
     ```sh
    pip install -r requirement.txt
    ```
6. running the server, this is for development server
    ```sh
    python wsgi.py
    ```