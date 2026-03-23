MVP Build Order:
Get ffmpeg installed and build a working M4B from hardcoded text — proves the output format works
Add gTTS → generates audio from text string — proves TTS pipeline
Add PyMuPDF → extract text + attempt TOC parsing — proves PDF input
Wire them together in a script (no web yet) — full pipeline working locally
Wrap in FastAPI with background task + polling
Add the drag-drop frontend last

Don't touch the frontend until step 5. The web layer is the least interesting problem here.

FastAPI (Python backend)
├── /upload        → receives PDF, queues job
├── /status/{id}   → polling endpoint (processing takes time)
└── /download/{id} → returns .m4b file

Libraries:
├── PyMuPDF         → PDF parsing + TOC + font data
├── gTTS or openai  → text to speech
├── ffmpeg (CLI)    → audio concat + M4B creation
└── python-ffmpeg or subprocess → call ffmpeg from Python

Frontend (same server or separate):
└── Simple HTML/JS drag-drop → polls status → download link