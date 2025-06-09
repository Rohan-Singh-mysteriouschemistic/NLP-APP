# NLP-APP

This Python script creates a GUI-based NLP application using Tkinter and the NLP Cloud API.

Features:
---------
1. **User Authentication System**:
   - Users can register with their name, email, and password.
   - Existing users can log in using their credentials.
   - Login credentials are verified using a custom 'Database' class (from 'mydatabase').

2. **Main Functionalities Available After Login**:
   - **Grammar and Spelling Check**: Uses NLP Cloud's fine-tuned LLaMA model to detect and correct grammatical errors.
   - **NER (Named Entity Recognition)**: Extracts specific types of named entities (e.g., persons, languages) from a paragraph.
   - **Sentiment Analysis**: Analyzes sentiment (positive, negative, etc.) in user-provided text with scoring.
   - **Language Detection**: Detects the language of the input text using a dedicated language detection model.
   - **Code Generation**: Uses a fine-tuned LLaMA model to generate code from text prompts.

3. **GUI Design with Tkinter**:
   - The interface is styled with light blue backgrounds and white text buttons.
   - Screens switch dynamically using a `Clear()` method that removes widgets except for the main heading.
   - Each functional screen takes text input and displays results in a neat format (label or text box).

4. **Integration**:
   - The app integrates `nlpcloud` for NLP functionalities using a token.
   - Proper error handling and feedback is provided via message boxes (`messagebox.showinfo()` and `showerror()`).

Note:
-----
- The design is simple and user-friendly, with consistent theming (colors and padding).
- Icons and assets are assumed to be available locally (e.g., `favicon.ico`).
- The app is launched when the `Nlp_Project()` object is created at the end of the script.
