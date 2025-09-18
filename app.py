from flask import Flask, request, send_file, jsonify
from pydub import AudioSegment
import os
import uuid

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
CONVERTED_FOLDER = 'converted'

# Ensure folders exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(CONVERTED_FOLDER, exist_ok=True)

# Supported formats
SUPPORTED_INPUT_FORMATS = [
    'mp3', 'wav', 'flac', 'aac', 'ogg', 'm4a', 'wma', 'alac', 'aiff',
    'amr', 'au', 'caf', 'mka', 'opus', 'ra', 'ram', 'snd', 'pcm', 'aax', 'dsd'
]

SUPPORTED_OUTPUT_FORMATS = SUPPORTED_INPUT_FORMATS.copy()


@app.route('/')
def home():
    input_formats = ', '.join(SUPPORTED_INPUT_FORMATS)
    output_formats = ', '.join(SUPPORTED_OUTPUT_FORMATS)
    return f"""
    <h2>🎧 Welcome to the Audio Converter API 🎧</h2>
    <p><strong>Supported Input Formats:</strong></p>
    <p>{input_formats}</p>
    <p><strong>Supported Output Formats:</strong></p>
    <p>{output_formats}</p>
    <p>➡️ To convert an audio file, send a <code>POST</code> request to <code>/convert</code> with the following:</p>
    <ul>
        <li><strong>file</strong>: the audio file to convert</li>
        <li><strong>target_format</strong>: desired output format (e.g., mp3, wav, flac)</li>
    </ul>
    <p>💡 Test this API using <strong>Postman</strong> or <strong>cURL</strong>.</p>
    <p>Example Postman setup:</p>
    <ul>
        <li>Method: POST</li>
        <li>URL: http://127.0.0.1:5000/convert</li>
        <li>Body → form-data:</li>
        <ul>
            <li>key: file → select an audio file</li>
            <li>key: target_format → e.g., mp3</li>
        </ul>
    </ul>
    """


@app.route('/convert', methods=['POST'])
def convert_audio():
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 400

    file = request.files['file']
    target_format = request.form.get('target_format')

    if not target_format:
        return jsonify({'error': 'No target format specified'}), 400

    if target_format not in SUPPORTED_OUTPUT_FORMATS:
        return jsonify({'error': 'Unsupported target format'}), 400

    input_filename = f"{uuid.uuid4()}_{file.filename}"
    input_filepath = os.path.join(UPLOAD_FOLDER, input_filename)
    file.save(input_filepath)

    output_filename = f"{uuid.uuid4()}.{target_format}"
    output_filepath = os.path.join(CONVERTED_FOLDER, output_filename)

    try:
        # Detect input format from file extension
        input_format = file.filename.rsplit('.', 1)[-1].lower()

        if input_format not in SUPPORTED_INPUT_FORMATS:
            return jsonify({'error': 'Unsupported input format'}), 400

        # Load audio file
        audio = AudioSegment.from_file(input_filepath, format=input_format)

        # Export to target format
        audio.export(output_filepath, format=target_format)

        return send_file(output_filepath, as_attachment=True)

    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
