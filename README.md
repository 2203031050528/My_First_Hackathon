```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Smart Home Control System Using Hand Gesture Recognition</title>
</head>
<body>
    <h1>Smart Home Control System Using Hand Gesture Recognition</h1>

    <h2>Overview</h2>
    <p>This is my first hackathon project, a Smart Home Control System that leverages hand gesture recognition to detect and classify shapes drawn in the air using a webcam.</p>

    <h2>Features</h2>
    <ul>
        <li><strong>Real-time Hand Gesture Detection</strong>: Using the <code>cvzone.HandTrackingModule</code>, the system can detect and track hand movements.</li>
        <li><strong>Shape Classification</strong>: The system can classify basic shapes such as triangles, squares, rectangles, pentagons, and circles based on hand gestures.</li>
        <li><strong>Interactive Drawing</strong>: Users can draw shapes in the air, which are then classified and displayed on the screen.</li>
        <li><strong>Web Interface</strong>: The project includes a simple web interface using Flask to display the video feed and the recognized shapes.</li>
    </ul>

    <h2>Technologies Used</h2>
    <ul>
        <li><strong>Flask</strong>: A lightweight web framework to create the web interface.</li>
        <li><strong>OpenCV</strong>: A powerful library for real-time computer vision tasks.</li>
        <li><strong>cvzone.HandTrackingModule</strong>: A module for detecting and tracking hands.</li>
        <li><strong>NumPy</strong>: A library for numerical operations.</li>
    </ul>

    <h2>How It Works</h2>
    <ol>
        <li><strong>Hand Detection</strong>: The system uses a webcam to capture video frames and detect hands in real-time.</li>
        <li><strong>Gesture Recognition</strong>: Specific hand gestures are recognized, such as pointing with the index finger or drawing shapes.</li>
        <li><strong>Shape Classification</strong>: Based on the contour of the drawn shape, the system classifies it as a triangle, square, rectangle, pentagon, or circle.</li>
        <li><strong>Drawing</strong>: The shapes are drawn on the screen and the name of the recognized shape is displayed.</li>
    </ol>

    <h2>Setup and Installation</h2>
    <ol>
        <li><strong>Clone the Repository</strong>:
            <pre><code>git clone https://github.com/your-username/hand-gesture-recognition.git
cd hand-gesture-recognition</code></pre>
        </li>
        <li><strong>Install Dependencies</strong>:
            <pre><code>pip install -r requirements.txt</code></pre>
        </li>
        <li><strong>Run the Application</strong>:
            <pre><code>python app.py</code></pre>
        </li>
        <li><strong>Access the Web Interface</strong>:
            <p>Open your web browser and go to <code>http://127.0.0.1:5000</code>.</p>
        </li>
    </ol>

    <h2>Project Structure</h2>
    <ul>
        <li><code>app.py</code>: The main Flask application file.</li>
        <li><code>templates/index.html</code>: The HTML template for the web interface.</li>
        <li><code>requirements.txt</code>: A list of required Python libraries.</li>
    </ul>

    <h2>Usage</h2>
    <ul>
        <li>Navigate to the web interface.</li>
        <li>Allow access to your webcam.</li>
        <li>Use specific hand gestures to draw shapes in the air.</li>
        <li>The system will detect and classify the shapes in real-time.</li>
    </ul>

    <h2>Future Improvements</h2>
    <ul>
        <li><strong>Enhanced Shape Recognition</strong>: Extend the shape classification to include more complex shapes.</li>
        <li><strong>Gesture-based Controls</strong>: Implement gestures to control smart home devices.</li>
        <li><strong>User Interface</strong>: Improve the web interface for better user experience.</li>
    </ul>

    <h2>Conclusion</h2>
    <p>This project demonstrates the potential of combining computer vision and machine learning to create interactive applications. It serves as a foundation for more advanced gesture-based control systems in smart homes.</p>

    <h2>Acknowledgments</h2>
    <p>Special thanks to the organizers and my teammates for their support and collaboration during this hackathon.</p>
</body>
</html>
```
