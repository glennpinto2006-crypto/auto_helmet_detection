
# 🚦 AI-Based Real-Time Helmet Violation Detection and Automatic Number Plate Recognition System

An AI-powered traffic surveillance system that detects two-wheeler riders without helmets, recognizes vehicle registration numbers, and captures violation evidence from video streams. The system combines deep learning, computer vision, Optical Character Recognition (OCR), and multithreaded processing to automate traffic monitoring.

## 📌 Problem Statement

Road safety remains a major concern due to helmet violations among two-wheeler riders. Traditional traffic monitoring methods depend heavily on manual inspection and traffic personnel, making continuous monitoring time-consuming and labor-intensive.

Identifying violating vehicles and recording their registration numbers from CCTV footage can also be challenging, especially under poor lighting, motion blur, and low-resolution conditions.

This project aims to develop an automated traffic surveillance system that detects helmet violations in real time, extracts vehicle number plates using OCR, captures relevant evidence, and maintains structured violation records for monitoring and further review.

## 🎯 Objectives

- Detect riders, helmets, and vehicle number plates from video streams.
- Identify potential helmet violations using object detection and spatial association.
- Extract vehicle registration numbers using OCR.
- Improve number plate readability through image preprocessing.
- Capture and store rider and number plate images as evidence.
- Validate and normalize extracted registration text.
- Maintain organized violation records with timestamps.
- Improve processing efficiency using multithreading.

## ✨ Key Features

- 🧠 **YOLOv8 Object Detection:** Detects relevant objects using a trained detection model.
- 🪖 **Helmet Violation Detection:** Identifies potential cases where a rider is not wearing a helmet.
- 🔢 **Automatic Number Plate Recognition (ANPR):** Detects and extracts vehicle registration text.
- 🔍 **OCR Processing:** Uses EasyOCR to recognize characters from cropped number plate images.
- ⚡ **Multithreaded Processing:** Separates video detection and OCR workloads for more efficient processing.
- 🖼️ **Evidence Capture:** Saves rider images and number plate images associated with detected violations.
- 🧹 **Text Cleaning and Validation:** Removes unwanted characters and checks extracted text against supported registration formats.
- 📂 **Automatic File Organization:** Organizes captured images into folders based on recognized registration numbers.
- 🗃️ **Violation Logging:** Supports structured storage of violation details and timestamps.

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core application development |
| YOLOv8 | Object detection |
| OpenCV | Video capture, image processing, and cropping |
| EasyOCR | Number plate text recognition |
| PyTorch | Deep learning model execution |
| Threading and Queues | Parallel task processing and communication |
| NumPy | Numerical and image-array operations |
| Tkinter / Python GUI | Desktop interface, if using `gui.py` |
| SQLite / Other Database | Structured violation records, if integrated |

## 🏗️ System Architecture

The system is organized into the following functional modules:

1. **Video Input Module:** Receives frames from a webcam, CCTV stream, or prerecorded video.
2. **Frame Processing Module:** Resizes frames and prepares them for detection.
3. **Object Detection Module:** Uses YOLOv8 to identify riders, helmets, and number plates.
4. **Violation Analysis Module:** Associates helmet detections with riders and identifies potential violations.
5. **Image Extraction Module:** Crops the relevant rider and number plate regions.
6. **OCR Processing Module:** Extracts registration text from number plate images using EasyOCR.
7. **Validation Module:** Cleans and checks the recognized text.
8. **Storage Module:** Saves evidence images and records associated information.
9. **Display Module:** Presents detection results through the application interface.

## 🔄 Workflow

```text
Video Input
     |
     v
Frame Capture using OpenCV
     |
     v
Frame Preprocessing
     |
     v
YOLOv8 Object Detection
     |
     +---------------------------+
     |                           |
     v                           v
Rider and Helmet Detection   Number Plate Detection
     |                           |
     v                           v
Helmet Association          Crop Number Plate
     |                           |
     v                           v
Potential Violation?        Image Preprocessing
     |                           |
     +------------+              v
                  |           EasyOCR
                  |              |
                  |              v
                  |        Text Cleaning
                  |              |
                  |              v
                  |        Format Validation
                  |              |
                  +--------------+
                         |
                         v
              Save Evidence and Results
                         |
                         v
               Display / Violation Log
```

Detection and OCR can run in separate threads, with queues used to transfer cropped images and associated metadata between processing stages.

## 🧠 Core Concepts

### 1. Object Detection

YOLOv8 processes video frames and predicts bounding boxes, object classes, and confidence scores for objects learned during model training.

The detection model must be trained or configured for the required classes, such as rider, helmet, and number plate.

### 2. Helmet Violation Analysis

The system evaluates helmet detections in relation to the corresponding rider. Spatial association, bounding-box positions, and optional tracking can help determine whether a helmet is associated with a rider.

The absence of a helmet detection alone does not conclusively prove a violation, so confidence thresholds and repeated-frame verification can help reduce false detections.

### 3. Automatic Number Plate Recognition

The number plate detector identifies the plate region and extracts a cropped image. The cropped image is then passed to EasyOCR to recognize the registration characters.

### 4. Image Preprocessing

Image resizing, contrast adjustment, denoising, and sharpening can be applied to improve OCR readability. Super-resolution can also be evaluated as an optional enhancement for low-resolution images.

### 5. Multithreading

The application can separate object detection from OCR processing. This allows the video-processing stage to continue while number plate text is being recognized.

Actual performance improvements depend on hardware, model inference time, and queue management.

### 6. Text Validation

OCR output may contain incorrectly recognized characters. Text cleaning and registration-format checks help identify invalid or uncertain results.

Validation rules must account for supported vehicle registration formats and should not automatically convert ambiguous characters without sufficient evidence.

## 📸 Expected Output

The system is designed to produce:

- Annotated video frames showing detected objects.
- Potential helmet violation records.
- Cropped rider images for relevant cases.
- Cropped number plate images.
- Recognized and validated registration text.
- Timestamps associated with captured events.
- Organized evidence folders and structured records.
- A display interface for reviewing detection results.

## 📁 Project Structure

```text
Project/
│
├── ocr+yolo.py           # Detection and OCR pipeline
├── gui.py                # Desktop interface, if applicable
├── read_plates/          # Saved number plate and rider images
│   └── APXX1234/
│       ├── plate_.jpg
│       └── rider_.jpg
├── images/               # README screenshots and diagrams
├── requirements.txt      # Python dependencies
├── .gitignore
└── README.md
```

The structure may vary depending on the final implementation. Trained model weights and datasets should be placed in their configured locations and should not be assumed to be included in the repository.

## 💻 Requirements

- Python 3.10 or another Python version supported by the selected dependencies.
- A laptop or desktop computer.
- Built-in laptop camera, USB webcam, CCTV stream, or prerecorded video.
- A trained YOLOv8 model compatible with the installed Ultralytics package.
- Sufficient RAM and processing power for video inference.
- An NVIDIA GPU is optional; CPU inference may be slower.

## ⚙️ Installation and Setup

### Step 1: Clone the Repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd <YOUR_PROJECT_FOLDER>
```

Replace the placeholders with your actual GitHub repository URL and folder name.

### Step 2: Create a Virtual Environment

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

### Step 3: Install Dependencies

If a `requirements.txt` file is available:

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Otherwise, install the required packages individually:

```bash
pip install ultralytics opencv-python easyocr numpy
```

Install a compatible PyTorch version according to the official PyTorch installation instructions.

### Step 4: Configure the YOLO Model

Place the trained YOLOv8 model weights in the configured model directory.

For example:

```text
Project/
├── models/
│   └── best.pt
```

Update the model path in the source code if required.

The model must have been trained or configured to recognize the object classes used by the application. A general-purpose pretrained model will not automatically detect every custom helmet or number plate class.

### Step 5: Run the Application

If `gui.py` launches the interface:

```bash
python gui.py
```

If `ocr+yolo.py` is the main pipeline entry point:

```bash
python "ocr+yolo.py"
```

Use the entry point and camera configuration defined in the actual source code.

## 🎥 Input Sources

The application can be configured to use different video sources.

**Laptop webcam or USB webcam:**

```python
cap = cv2.VideoCapture(0)
```

**Prerecorded video:**

```python
cap = cv2.VideoCapture("traffic.mp4")
```

**CCTV or IP camera:**

```python
cap = cv2.VideoCapture("YOUR_CAMERA_STREAM_URL")
```

Camera access, stream compatibility, and sufficient image resolution are required for reliable operation.

## 📊 Performance Evaluation

The system should be evaluated using measurable metrics rather than visual demonstrations alone.

| Metric | Purpose |
|---|---|
| Detection Precision | Measures how many predicted detections are correct |
| Detection Recall | Measures how many actual target objects are detected |
| mAP@50 | Evaluates object detection performance at an IoU threshold of 0.50 |
| OCR Character Accuracy | Measures the correctness of recognized characters |
| Exact Plate Match Rate | Measures how often the complete registration text is recognized correctly |
| Processing FPS | Measures the number of video frames processed per second |
| False Violation Rate | Measures how often non-violations are incorrectly flagged |
| Processing Latency | Measures the time taken to produce a result |

Performance should be measured on a representative test dataset containing different distances, lighting conditions, viewing angles, and image qualities.

## ⚠️ Limitations

- Detection accuracy depends on model training data and image quality.
- Motion blur, occlusion, poor lighting, and unusual viewing angles can reduce accuracy.
- Helmet-to-rider association may generate false positives or false negatives.
- OCR can misread unclear or partially visible registration characters.
- Multithreading does not guarantee higher FPS on every system.
- Super-resolution may introduce artificial details and does not guarantee improved recognition.
- A detected potential violation requires appropriate review before enforcement action.
- The prototype is not a substitute for an officially validated traffic enforcement system.

## 🔮 Future Enhancements

- Rider tracking using ByteTrack or another suitable tracking algorithm.
- Multi-frame verification to reduce duplicate or incorrect records.
- Improved helmet-to-rider association.
- Confidence-aware OCR and multiple-frame plate recognition.
- A web-based dashboard for live monitoring and historical analytics.
- Database integration for searching and filtering violation records.
- PDF report generation for authorized review.
- Performance optimization for CPU and GPU execution.
- Multi-camera support and camera-wise event monitoring.
- Secure access controls, evidence integrity checks, and configurable data-retention policies.

## 🌍 Sustainable Development Goals (SDGs)

- **SDG 3 – Good Health and Well-Being:** Supports road-safety monitoring and helmet compliance.
- **SDG 11 – Sustainable Cities and Communities:** Contributes to intelligent traffic surveillance and safer urban mobility.

## 🔐 Privacy and Responsible Use

This project processes images and vehicle registration information. It should be used only with appropriate authorization and in accordance with applicable privacy and traffic-enforcement requirements.

Access to captured evidence should be restricted, records should be retained only as necessary, and uncertain detections should be reviewed before any enforcement decision.

## 👨‍💻 Project Information

**Project Title:** AI-Based Real-Time Helmet Violation Detection and Automatic Number Plate Recognition System

**Project Type:** Academic Mini Project

**Domain:** Artificial Intelligence, Machine Learning, Computer Vision, and Intelligent Transportation Systems

**Developer:** Glenn Pinto

**Institution:** Fr. Conceicao Rodrigues Institute of Technology (FCRIT), Vashi

## 📚 References

- [Ultralytics YOLO Documentation](https://docs.ultralytics.com/)
- [OpenCV Documentation](https://docs.opencv.org/)
- [EasyOCR GitHub Repository](https://github.com/JaidedAI/EasyOCR)
- [PyTorch Documentation](https://pytorch.org/docs/stable/index.html)

---

⭐ If you find this project useful, consider starring the repository.

*Note: Features and evaluation metrics described above should be updated to reflect the functionality actually implemented and tested in the final project.*
