import assemblyai as aai
import os
from dotenv import load_dotenv
import time

# Replace with your API key
load_dotenv()

aai.settings.api_key = os.getenv("ASSEMBLYAI_API_KEY")

# You can also transcribe a local file by passing in a file path
FILE_URL = './09-11-23_Council_Mtg_60.ogg'

config = aai.TranscriptionConfig(
    speaker_labels=True,
)

# Transcribe the audio file. WHen done, print the time it took to transcribe
t0 = time.time()
transcriber = aai.Transcriber()
transcript = transcriber.transcribe(FILE_URL, config)
t1 = time.time()

print(f"Transcription complete. Time taken: {t1 - t0}")
print("Now generating minutes of meeting...")

prompt = """You are an assistant tasked with generating Minutes of Meeting (MoM) from a well-annotated meeting transcript. 

Please analyze the provided transcript and create a structured summary with the following sections:

1. **Meeting Overview** ("N/A" if not available for each):
   - Date and Time of Meeting
   - Participants and Roles (e.g., John Doe - Project Manager)
   - Main Objectives

2. **Key Points Discussed**:
   - Summarize each topic of discussion, focusing on the main points raised by participants. Group related points under clear subheadings or bullet points.

3. **Decisions Made**:
   - List all key decisions reached during the meeting, along with any consensus or dissent noted among participants.

4. **Action Items**:
   - Clearly outline each action item, specifying the task, the responsible person(s), and any deadlines or follow-up dates.

5. **Additional Notes**:
   - Any other relevant information, questions raised, or future discussion points.

Using the transcript annotations, please identify and attribute key points to specific entities where possible (e.g., "John Doe emphasized the need for...").

Return the Minutes of Meeting in a structured, readable format suitable for distribution to meeting attendees.
"""

result = transcript.lemur.task(
    prompt, final_model=aai.LemurModel.claude3_5_sonnet
)

t2 = time.time()
print(f"Minutes of Meeting generated. Time taken: {t2 - t1}")

print(result.response)