# CRIMINAL-DETECTION-SYSTEM-FOR-BANKING-SECTOR
🔐 Project Overview: Facial Recognition-Based Criminal Detection in Banking
This system integrates facial recognition with criminal record databases to ensure secure banking transactions and detect potential criminal activity at the point of transaction for ATMs.

📊 System Workflow Breakdown
🧍 User Initiates Transaction

A user accesses an ATM or banking terminal to initiate a transaction.

The bank server receives the transaction request.

📸 Capture Facial Data

The system captures the facial image of the user in real-time using a camera at the terminal.

🧼 Preprocessing

The captured image undergoes:

Noise removal

Feature detection

Image enhancement

🛠️ Tech Stack & Technical Skills

💻 Programming Languages & Core Logic
Python: Used as the primary programming language for computer vision pipelines, image processing, and backend logic.

JavaScript: Utilized to build responsive, interactive user interfaces for the administrative and law enforcement dashboards.

⚙️ Backend Architecture

Flask: Employed as the core web framework to build robust RESTful APIs, manage system routes, and handle real-time HTTP requests.

REST APIs: Designed and integrated secure data flows to transmit transaction logs, facial matching statuses, and system alerts seamlessly.

Real-time Alert System: Developed automated trigger mechanisms to handle critical actions like account blocking and law enforcement notifications instantly.  
PDF

🗄️ Database Management

MongoDB (NoSQL): Utilized as a robust, scalable database to securely store user profiles, real-time transaction logs, and pre-verified criminal records across structured collections.

👁️ Computer Vision & Deep Learning

OpenCV: Leveraged for real-time video feed analysis, frame capturing, and image preprocessing.

Haar Cascade: Integrated for accurate real-time facial detection within live video streams.

LBPH (Local Binary Patterns Histograms): Deployed for facial feature extraction and match verification against the centralized database.

🔍 Feature Extraction

Extracts unique facial features using:

Landmarks

Eigenfaces

CNN-based (Convolutional Neural Network) deep learning features

🗃️ Data Matching with Criminal Records

Extracted features are compared against a criminal database.

If the face matches a record, the system follows a secure process to prevent misuse.

🔒 If Criminal Match Found

Hold the bank account

Notify the bank and the account holder

Check for status:

If legal action is taken, the bank account can be reopened

If not, the account remains on hold until action is taken

✅ If No Match Found

The system allows bank operations to proceed normally

The process ends securely
