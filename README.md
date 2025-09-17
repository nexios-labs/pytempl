# PyTempl: A Pythonic Component-Based Template Engine

PyTempl is a powerful template engine that transpiles component-based `.pytempl` files into highly optimized, pure Python code. It allows you to leverage the full power of Python within your templates for logic, expressions, and component composition, eliminating runtime parsing overhead and boosting performance.

## ✨ Features

-   **Component-Based Architecture**: Build complex UIs from small, reusable, and encapsulated components.
-   **Python-in-Template**: Write Python logic, expressions, and imports directly within your template files.
-   **Compile-Time Transpilation**: Converts `.pytempl` files into standard Python functions ahead of time for maximum performance.
-   **Zero Runtime Dependencies**: The compiled output is pure Python, requiring no special template engine at runtime.
-   **Framework Agnostic**: Use the generated Python components with any web framework, such as Nexios, Flask, or FastAPI.

## 🚀 Getting Started

Follow these instructions to get the project up and running on your local machine.

### Prerequisites

-   Python 3.11 or higher
-   Git

### ⚙️ Installation

1.  **Clone the repository**:
    ```bash
    git clone https://github.com/nexios-labs/pytempl.git
    cd pytempl
    ```

2.  **Create and activate a virtual environment**:
    *   On macOS and Linux:
        ```bash
        python3 -m venv venv
        source venv/bin/activate
        ```
    *   On Windows:
        ```bash
        python -m venv venv
        .\venv\Scripts\activate
        ```

3.  **Install the required dependencies**:
    ```bash
    pip install -e .[dev]
    ```
    This command installs the package in editable mode along with the development dependencies.

## 🛠️ Usage

PyTempl works by transpiling `.pytempl` files into `.py` files. You can then import and use the generated functions in your application.

### 1. Writing a Component

Create a file with a `.pytempl` extension. This syntax combines HTML-like structure with Python capabilities.

**`sample.pytempl`**:
```pytempl
component Button(props) {
  <template>
    <button onclick="{{ props.get('onclick') }}">
      @slot()
    </button>
  </template>
}

component Counter() {
  <script type="text/python">
    count = 0
  </script>

  <template>
    <div>
      <span>Count is: {{ count }}</span>
      @Button({"onclick": "increase()"}) { Increase }
      @Button({"onclick": "decrease()"}) { Decrease }
    </div>
  </template>
}
```

### 2. Transpiling to Python

Run the engine to process your template file. The `main.py` script provides a simple way to do this.

```bash
python main.py
```

This will read `./sample.pytempl` and generate a corresponding `./sample.py` file containing standard Python functions.

**Generated `sample.py`**:
```python
# This is a representation of the generated output
def Button(props, slot):
    return ( '<button onclick="'+str(props.get('onclick'))+'"'>+slot()+'</button>' )

def Counter():
    count = 0
    return ( '<div'>+'<span>'+'Count is: '+str(count)+'</span>'+Button({"onclick": "increase()"}, lambda: 'Increase')+Button({"onclick": "decrease()"}, lambda: 'Decrease')+'</div>' )
```

### 3. Using Components in a Web App

You can now use the generated functions in any web application. The example below uses the `Nexios` framework.

**`nexios_sample.py`**:
```python
import uvicorn
from nexios import NexiosApp
# Import your generated components
from sample import Button

app = NexiosApp()

@app.get("/")
async def hello_world(request, response):
    # Render the component by calling it as a function
    html_content = Button({"onclick": "alert('Hello!')"}, lambda: "Click Me")
    return response.html(html_content)

if __name__ == "__main__":
    uvicorn.run("nexios_sample:app", reload=True)
```

Run the web server:
```bash
uvicorn nexios_sample:app --reload
```
Navigate to `http://127.0.0.1:8000` in your browser to see the rendered component.

## 💻 Technologies Used

| Technology                                    | Description                              |
| --------------------------------------------- | ---------------------------------------- |
| [Python 3.11+](https://www.python.org/)       | The core language for the engine.        |
| [Lark](https://github.com/lark-parser/lark)   | A modern parsing library for Python.     |
| [Nexios](https://pypi.org/project/nexios/)    | A web framework used for the example.    |
| [Uvicorn](https://www.uvicorn.org/)           | An ASGI server for running the web app.  |

## 🤝 Contributing

Contributions are welcome! If you have suggestions for improvement or want to contribute to the codebase, please follow these steps:

1.  **Fork the Project**: Click the 'Fork' button at the top right of this page.
2.  **Create your Feature Branch**:
    ```bash
    git checkout -b feature/AmazingFeature
    ```
3.  **Commit your Changes**:
    ```bash
    git commit -m 'Add some AmazingFeature'
    ```
4.  **Push to the Branch**:
    ```bash
    git push origin feature/AmazingFeature
    ```
5.  **Open a Pull Request**: Create a new Pull Request from your forked repository.

## 📄 License

This project is not licensed. All rights are reserved.

## 👤 Author

**[Your Name]**

-   **LinkedIn**: [linkedin.com/in/your-username](https://linkedin.com/in/your-username)
-   **Twitter**: [@your-handle](https://twitter.com/your-handle)

---

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.11%2B-blue?style=for-the-badge&logo=python" alt="Python Version">
  <img src="https://img.shields.io/badge/License-UNLICENSED-red?style=for-the-badge" alt="License">
  <img src="https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge" alt="Project Status">
</p>

[![Readme was generated by Dokugen](https://img.shields.io/badge/Readme%20was%20generated%20by-Dokugen-brightgreen)](https://www.npmjs.com/package/dokugen)