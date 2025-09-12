from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/update_location', methods=['POST'])
def update_location():
    try:
        data = request.get_json()
        latitude = data.get('latitude')
        longitude = data.get('longitude')
        
        # Here you can save the location to a database
        print(f"Received location: {latitude}, {longitude}")
        
        return jsonify({'status': 'success'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

if __name__ == '__main__':
    # Use adhoc SSL context for HTTPS (required for geolocation in modern browsers)
    app.run(debug=True, ssl_context='adhoc')