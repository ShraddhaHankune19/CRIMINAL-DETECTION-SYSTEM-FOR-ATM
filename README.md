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
