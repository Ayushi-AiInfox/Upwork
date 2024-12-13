from flask import Flask, jsonify, logging, request

app = Flask(__name__)

@app.route('/callback', methods=['POST','GET'])

def upwork_callback():
    """
    Endpoint to handle callbacks from Upwork API.
    """
    try:
        # Log the incoming request for debugging
        logging.info("Received callback: %s", request.json)
 
        # Parse the data from Upwork API
        callback_data = request.json
 
        # Verify and validate callback data
        # You may need to use a secret key or other verification methods provided by Upwork
        if not callback_data:
            return jsonify({"error": "Invalid callback data"}), 400
 
        # Process the callback data (example processing)
        event_type = callback_data.get("event", "unknown_event")
        details = callback_data.get("details", {})
 
        # Log or process the event as needed
        logging.info(f"Event Type: {event_type}, Details: {details}")
 
        # Respond to Upwork to acknowledge receipt
        return jsonify({"status": "success", "message": "Callback processed successfully"}), 200
 
    except Exception as e:
        # Handle errors
        logging.error("Error processing callback: %s", str(e))
        return jsonify({"status": "error", "message": str(e)}), 500
 
if __name__ == '__main__':
    # Run the Flask app
    app.run(host='0.0.0.0', port=5000, debug=True)