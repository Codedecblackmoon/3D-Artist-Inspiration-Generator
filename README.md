# Flask Project: 3D Art Inspirational Generator

This project is a Flask-based web application designed to help 3D artists who are struggling to come up with ideas for their next creation. By selecting a difficulty level (Easy, Medium, or Hard), the application generates an inspirational prompt that includes a randomly chosen object, a setting, and a set of colors (with their HEX codes) to guide the creation process.

---

## **Features**
- **Difficulty Levels**:
  - **Easy**: Generates a simple object with 2 colors.
  - **Medium**: Generates a moderately challenging object with 3 colors.
  - **Hard**: Generates a complex object with 4 colors.
- **Randomized Inspiration**:
  - Themes and objects are randomly selected to spark creativity.
  - Colors are provided with HEX codes for precise use in 3D software.
- **User-Friendly Interface**:
  - Interactive HTML interface for prompt generation.

---

## **Requirements**
- Python 3.7+
- Flask (Python web framework)

---

## **Setup Instructions**

### 1. Clone the Repository
```bash
$ git clone <repository-url>
$ cd <repository-folder>
```

### 2. Set Up a Virtual Environment
To avoid dependency conflicts, it’s recommended to use a virtual environment:
```bash
$ python3 -m venv venv
$ source venv/bin/activate    # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
Install the required Python packages using `pip`:
```bash
$ pip install flask
```

### 4. Run the Application
Run the Flask server:
```bash
$ python app.py
```
The app will run on `http://127.0.0.1:5000/` by default.

---

## **Usage**
1. Open your web browser and navigate to `http://127.0.0.1:5000/`.
2. Select a difficulty level (Easy, Medium, or Hard).
3. Submit the form to generate an inspirational prompt.
4. Use the generated object, theme, and color scheme (with HEX codes) as a guide for your 3D art project.

---

## **Troubleshooting**
- **Dependencies Error**: Run `pip install -r requirements.txt` if a `requirements.txt` file is provided.
- **Port Issues**: If the default port is busy, run the app on a different port:
  ```bash
  $ python app.py --port=8080
  ```

---

## **Future Enhancements**
- Add more themes, objects, and color combinations for greater variety.
- Include advanced difficulty options with additional constraints (e.g., specific dimensions or materials).
- Implement user accounts for saving and revisiting prompts.
- Provide integration with popular 3D software for direct imports.

---

Unleash your creativity with this 3D art inspiration generator and bring your ideas to life!

