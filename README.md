
## **Overview** 📄

This is my first hackathon project that leverages hand gesture recognition to detect and classify shapes drawn in the air using a webcam.

## **Features** ✨

- **Real-time Hand Gesture Detection**: Using the `cvzone.HandTrackingModule`, the system can detect and track hand movements.
- **Shape Classification**: The system can classify basic shapes such as triangles, squares, rectangles, pentagons, and circles based on hand gestures.
- **Interactive Drawing**: Users can draw shapes in the air, which are then classified and displayed on the screen.
- **Web Interface**: The project includes a simple web interface using Flask to display the video feed and the recognized shapes.

## **Technologies Used** 🛠️

- **Flask**: A lightweight web framework to create the web interface.
- **OpenCV**: A powerful library for real-time computer vision tasks.
- **cvzone.HandTrackingModule**: A module for detecting and tracking hands.
- **NumPy**: A library for numerical operations.

## **How It Works** ⚙️

1. **Hand Detection**: The system uses a webcam to capture video frames and detect hands in real-time.
2. **Gesture Recognition**: Specific hand gestures are recognized, such as pointing with the index finger or drawing shapes.
3. **Shape Classification**: Based on the contour of the drawn shape, the system classifies it as a triangle, square, rectangle, pentagon, or circle.
4. **Drawing**: The shapes are drawn on the screen and the name of the recognized shape is displayed.

## **Setup and Installation** 💻

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/your-username/hand-gesture-recognition.git
    cd hand-gesture-recognition
    ```

2. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the Application**:
    ```bash
    python app.py
    ```

4. **Access the Web Interface**:
    Open your web browser and go to `http://127.0.0.1:5000`.

## **Project Structure** 📁

- `app.py`: The main Flask application file.
- `templates/index.html`: The HTML template for the web interface.
- `requirements.txt`: A list of required Python libraries.

## **Usage** 🎮

- Navigate to the web interface.
- Allow access to your webcam.
- Use specific hand gestures to draw shapes in the air.
- The system will detect and classify the shapes in real-time.

## **Future Improvements** 🌟

- **Enhanced Shape Recognition**: Extend the shape classification to include more complex shapes.
- **Gesture-based Controls**: Implement gestures to control smart home devices.
- **User Interface**: Improve the web interface for better user experience.

## **Conclusion** 🏁

This project demonstrates the potential of combining computer vision and machine learning to create interactive applications. It serves as a foundation for more advanced gesture-based control systems in smart homes.

## **Acknowledgments** 🙏

Special thanks to the organizers and my teammates for their support and collaboration during this hackathon.
