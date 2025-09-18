
# Audio Converter API 

A **Flask-based API** that allows users to convert audio files from one format to another.  This project uses **PyDub** (powered by FFmpeg) to handle audio conversions efficiently. 


## Features  

✅ Convert between 20+ audio input formats (MP3, WAV, FLAC, AAC, OGG, etc.)  

✅ Supports 20+ output formats, covering popular and advanced codecs  

✅ Built with Flask – lightweight and easy-to-use API framework  

✅ Uses PyDub (powered by FFmpeg) for fast and accurate audio conversion  

✅ Clean and modular project structure for better maintainability  

✅ Returns the converted audio file as a downloadable response  

✅ Error handling for unsupported formats, missing files, or invalid requests  


## Tech Stack

- Python 3.x  
- Flask – Web framework for building the API  
- PyDub – For audio processing and conversion  
- FFmpeg – Backend engine for media handling  

## How It Works

- User sends a POST request to the `/convert` endpoint with:  

   `file`: Audio file (form-data)  

   `target_format`: Desired output format (e.g., mp3, wav)  

- The API:  

   Saves the uploaded file in the `uploads/` folder  

   Converts it using PyDub + FFmpeg  

   Saves the output in the `converted/` folder  

   Returns the converted file as a download  

Any error (like missing file/invalid format) returns a clear JSON error message.  

## Supported Formats  

✅ Input Formats (20 examples)  

mp3, wav, flac, aac, ogg, m4a, wma, amr, au, ac3, aiff, opus, ra, voc, mp2, gsm, dts, caf, atrac, spx  

✅ Output Formats (20 examples)  

mp3, wav, flac, aac, ogg, m4a, wma, amr, au, ac3, aiff, opus, ra, voc, mp2, gsm, dts, caf, atrac, spx  

## API Endpoints  

### Home Endpoint  
- **URL:** `/`  
- **Method:** `GET`  
- **Description:** Shows welcome message, supported formats, and usage instructions.  

---

### Convert Endpoint  
- **URL:** `/convert`  
- **Method:** `POST`  
- **Parameters (form-data):**  
  - `file` → audio file to convert  
  - `target_format` → desired output format  

- **Response:** Returns converted audio file as a download.  

---

## Example (Postman)  

### ✅ Postman Setup  
- **Method:** `POST`  
- **URL:** `http://127.0.0.1:5000/convert`  
- **Body → form-data:**  
  - Key: `file` → Select your audio file  
  - Key: `target_format` → Example: `wav`  

👉 Send request → You’ll get the converted file as a download.  

## Setup Instructions

 Clone the Repository:

```bash
git clone https://github.com/yourusername/audio-converter-api.git
cd audio-converter-api
```

Create & activate virtual environment:

```bash
python -m venv venv
source venv/bin/activate   # (Linux/Mac)
venv\Scripts\activate      # (Windows)
```
Install dependencies:

```bash
pip install -r requirements.txt
```
Run the app:
```bash 
python app.py
```
By default, backend runs at: http://localhost:5000

## Why This Project Stands Out

✔️ Demonstrates backend development skills with Flask

✔️ Real-world use case: audio file conversion

✔️ Uses FFmpeg (industry standard) for audio processing

✔️ Showcases API design, error handling, and clean documentation

✔️ Can be extended into a full-stack project (React frontend, cloud deployment, etc.)

##  Demo

[![Watch the demo](https://drive.google.com/file/d/1q87_H6Wty0oGA9NO-IkiXcVRX_uk66Gn/view?usp=sharing)]


## 🔗 Links
[![GitHub](https://img.shields.io/badge/my_github-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://github.com/shambhavisingh011)
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/shambhavi-singh-619100239/)
[![twitter](https://img.shields.io/badge/leetcode-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://leetcode.com/u/Shambhavi011/)

