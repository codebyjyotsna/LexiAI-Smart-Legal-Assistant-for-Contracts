# LexiAI-Smart-Legal-Assistant-for-Contracts\
LexiAI is an AI-powered platform that helps individuals, businesses, and startups analyze, understand, and improve legal contracts. The platform leverages Natural Language Processing (NLP) and Machine Learning (ML) to simplify the complexities of legal documents.

## Table of Contents
- [Features](#features)
- [Getting Started](#getting-started)
- [Architecture](#architecture)
- [Technologies Used](#technologies-used)
- [Datasets](#datasets)
- [Future Roadmap](#future-roadmap)
- [Contributing](#contributing)
- [License](#license)

## Features
1. **Contract Summarization**
   - Automatically generates summaries of lengthy contracts.
   - Highlights critical sections, such as termination clauses, payment terms, and liabilities.
2. **Risk Detection & Simplification**
   - Identifies risky or vague clauses using rule-based algorithms and ML classifiers.
   - Simplifies legal jargon into easy-to-understand language for non-lawyers.
3. **Clause Suggestions**
   - Suggests missing or ideal clauses based on contract type (e.g., NDA, Service Agreement).
   - Uses fine-tuned GPT-4 for custom clause generation.
4. **PDF & OCR Upload**
   - Allows users to upload contracts in PDF or image format.
   - Extracts text using Tesseract OCR or AWS Textract.
5. **Search & Explanation Tool**
   - Enables users to highlight any clause and get a contextual explanation, references, or similar past clauses.

## Getting Started
### Prerequisites
- **Frontend Requirements**: Node.js, npm or yarn
- **Backend Requirements**: Python 3.9+, pip, Docker (optional for deployment)
- **API Keys**: OpenAI API key (for GPT integration), AWS credentials (for Textract, optional)

### Installation
#### Clone the Repository
```bash
git clone https://github.com/codebyjyotsna/LexiAI.git
cd LexiAI
```
#### Frontend Setup
1. Navigate to the `frontend` directory:
   ```bash
   cd frontend
   ```
2. Install dependencies:
   ```bash
   npm install
   ```
3. Start the development server:
   ```bash
   npm start
   ```
#### Backend Setup
1. Navigate to the `backend` directory:
   ```bash
   cd backend
   ```
2. Create a virtual environment and activate it:
   ```bash
   python3 -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the backend server:
   ```bash
   uvicorn main:app --reload
   ```
#### Environment Configuration
- Add your OpenAI API key, Firebase credentials, and other configuration details in `.env` files in both `frontend` and `backend` directories.
### Usage
1. Open the frontend at `http://localhost:3000`.
2. Upload a PDF or image of your contract.
3. Explore features like summarization, risk detection, clause suggestions, and explanations.

## Architecture
### Frontend
- **Framework**: React.js
- **Styling**: Tailwind CSS / Material UI
- **Hosting**: Vercel

### Backend
- **Framework**: FastAPI
- **AI/NLP Models**: Hugging Face Transformers, GPT-4
- **OCR**: Tesseract OCR / AWS Textract
- **Authentication**: Firebase Authentication
- **Database**: Firebase Firestore

### Diagram
```
User → Frontend (React.js) → Backend (FastAPI) → AI Models & Services (Hugging Face, GPT-4, OCR)
```

## Technologies Used

| Component          | Technology/Tool                          |
|---------------------|------------------------------------------|
| Frontend Framework  | React.js                                |
| Backend Framework   | FastAPI                                 |
| AI Models           | T5, BART, GPT-4                         |
| OCR Tools           | Tesseract OCR, AWS Textract             |
| Database            | Firebase Firestore                      |
| Hosting             | Vercel (Frontend), AWS/Render/Spaces    |
| Containerization    | Docker                                  |

## Datasets
1. **CUAD (Contract Understanding Atticus Dataset)**: For clause classification and summarization.
2. **SEC Legal Contract Dataset**: For training clause detection models.
3. **Custom Datasets**: Scraped or synthetic contracts for domain-specific tasks.

## Future Roadmap
1. **Collaboration Tools**
   - Enable sharing documents with team members for feedback.
2. **AI-Powered Negotiation Assistant**
   - Assist users during contract negotiations with real-time suggestions.
3. **Voice-to-Contract Dictation**
   - Convert verbal agreements or ideas into written contracts.
4. **Indian Law-Specific Modules**
   - Add tailored features for the Indian legal system.
