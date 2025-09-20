# Examples

This section provides comprehensive examples of PyTemplate usage, based on the demo application.

## Complete Demo Application

Here's the full demo application that showcases all PyTemplate features:

```pytempl
import math
from math import sqrt

component Label(props) {
  <template>
    <span class="text-red bg-black" id="20">{{ str(sqrt(int(props.get("count", "1")))) }}</span>
    <span>{{ props.get("text", "Click Me") }}</span>
    <label>@slot()</label>
  </template>
}

component Button(props) {
  <template>
    <button onclick="{{ props.get("onclick", "") }}" class="demo-button">
      @Label({ "count": {{ props.get("count", 4) }}, "text": {{ props.get("label", "Button") }} }) {
        @slot()
      }
    </button>
  </template>
}

component TodoItem(props) {
  <template>
    <li class="todo-item">
      if props.get("done", False) {
        <input type="checkbox" checked="true" />
      } else {
        <input type="checkbox" />
      }

      if props.get("done", False) {
        <span class="completed">
          {{ props.get("text", "Todo item") }}
        </span>  
      } else {
        <span>
          {{ props.get("text", "Todo item") }}
        </span>
      }
      @Label({ "count": {{ props.get("priority", 1) }} }) { Priority }
    </li>
  </template>
}

component Demo() {
  <script type="text/javascript">
    function showAlert(message) {
      alert("Demo Alert: " + message);
    }
    
    function toggleCount() {
      count = count === 0 ? 5 : 0;
      console.log("Count toggled to:", count);
    }
  </script>
  
  <script type="text/python">
    colors = ["red", "green", "blue", "purple", "orange"]
    count = 3
    todos = [
      {"text": "Learn template engine", "done": True, "priority": 9},
      {"text": "Build awesome app", "done": False, "priority": 16}, 
      {"text": "Deploy to production", "done": False, "priority": 25}
    ]
    
    def get_status():
      return "active" if count > 0 else "inactive"
      
    def get_message():
      return f"System has {count} items"
  </script>
  
  <template>
    <div class="demo-container">
      <h1>Template Engine Demo</h1>
      
      <div class="section">
        <h2>Basic Components & Math</h2>
        <p>
          Current count: <strong>{{ str(count) }}</strong>
          sqrt: {{ str(math.sqrt(count) if count > 0 else 0) }}
        </p>
        
        @Button({
          "onclick": "toggleCount()", 
          "label": "Toggle",
          "count": {{ str(count * count) }}
        }) {
          Toggle Count
        }

        @Button({
          "onclick": "showAlert('Hello World!')",
          "label": "Alert", 
          "count": 64
        }) {
          Show Alert
        }
      </div>
      
      <div class="section">
        <h2>Conditional Rendering</h2>
        <div class="{{ "status-" + get_status() }}">
          if count == 0 {
            <p class="warning">⚠️ No items available</p>
            @Label({"count": 1, "text": "Empty State"}) { System Idle }
          } elif count <= 3 {
            <p class="info">✅ Low activity mode</p>
            @Label({"count": {{ count * count }}, "text": "Low Mode"}) { {{ get_message() }} }
          } else {
            <p class="success">🚀 High activity mode</p>
            @Label({"count": {{ count * 4 }}, "text": "High Mode"}) { System is busy! }
          }
        </div>
      </div>
      
      <div class="section">
        <h2>Loops & Collections</h2>
        <div class="color-palette">
          <h3>Available Colors:</h3>
          for color in colors {
            <div class="{{ "color-item color-" + color }}">
              @Label({"count": {{ len(color) }}, "text": {{ color.title() }}}) { 
                {{ "Color: " + color }} 
              }
              <span class="color-code">#{{ color }}</span>
            </div>
          }
        </div>
        
        <div class="todo-list">
          <h3>Todo List:</h3>
          <ul>
            for todo in todos {
              @TodoItem({
                "text": {{ todo["text"] }},
                "done": {{ todo["done"] }}, 
                "priority": {{ todo["priority"] }}
              })
            }
          </ul>
        </div>
      </div>
      
      <div class="section">
        <h2>Nested Components</h2>
        <div class="nested-demo">
          @Button({"onclick": "showAlert('Outer button')", "count": 100}) {
            Outer Button with 
            @Label({"count": 49, "text": "Inner"}) { Nested Label }
            and more content
          }
          
          <div class="button-group">
            for i in {{ range(3) }} {
              @Button({ "onclick": "showAlert('hello')", "count": {{ (i + 1) * (i + 1) }} }) {
                Dynamic Button {{ str(i + 1) }}
              }
            }
          </div>
        </div>
      </div>
      
      <div class="section">
        <h2>Mixed Content</h2>
        <div class="mixed-content">
          <p>This section combines:</p>
          <ul>
            <li>Static HTML content</li>
            <li>Dynamic Python expressions: Count squared = {{ str(count * count) }}</li>
            <li>Component composition with {{ "@Label and @Button" }}</li>
            <li>JavaScript interactions</li>
          </ul>
          
          @Label({"count": {{ str(sum(range(count + 1))) }}, "text": "Sum"}) {
            Mathematical computation: Sum of 0 to {{ str(count) }} = {{ str(sum(range(count + 1))) }}
          }
          
          <br/>
          
          @Button({ "onclick": "showAlert('Demo completed!')", "count": 144 }) {
            Finish Demo
          }
        </div>
      </div>
    </div>
  </template>
}

component App() {
  <template>
    <!DOCTYPE html>
    <html>
    <head>
      <title>Template Engine Demo</title>

      <style>
        body { font-family: Arial, sans-serif; margin: 20px; background: #f5f5f5; }
        .demo-container { max-width: 800px; margin: 0 auto; background: white; padding: 20px; border-radius: 8px; }
        .section { margin: 30px 0; padding: 20px; border-left: 4px solid #007acc; }
        .demo-button { background: #007acc; color: white; border: none; padding: 10px 20px; margin: 5px; cursor: pointer; border-radius: 4px; }
        .demo-button:hover { background: #005a9e; }
        .text-red { color: red; }
        .bg-black { background: black; color: white; padding: 2px 6px; border-radius: 3px; }
        .color-item { margin: 10px; padding: 10px; border: 1px solid #ddd; border-radius: 4px; }
        .todo-item { margin: 5px 0; padding: 8px; }
        .completed { text-decoration: line-through; color: #888; }
        .warning { color: orange; }
        .info { color: blue; }
        .success { color: green; }
        .button-group { margin: 10px 0; }
        .color-red { background: #ffebee; }
        .color-green { background: #e8f5e8; }
        .color-blue { background: #e3f2fd; }
        .color-purple { background: #f3e5f5; }
        .color-orange { background: #fff3e0; }
      </style>
    </head>
    <body>
      @Demo()
    </body>
    </html>
  </template>
}
```

## Key Features Demonstrated

### 1. Component Definition and Usage
- **Label Component**: Shows props usage and slot content
- **Button Component**: Demonstrates nested components and event handlers
- **TodoItem Component**: Complex component with conditional rendering

### 2. Interpolation and Expressions
- Mathematical operations: `{{ str(count * count) }}`
- Function calls: `{{ get_message() }}`
- String operations: `{{ "Color: " + color }}`
- Complex expressions: `{{ str(sum(range(count + 1))) }}`

### 3. Conditional Rendering
- Simple if/else: Checkbox states based on `done` property
- Complex if/elif/else: Different messages based on count value
- Conditional attributes: Dynamic class names

### 4. Loops and Iteration
- List iteration: Colors and todos
- Range iteration: Dynamic button generation
- Dictionary access: Todo properties

### 5. Script Integration
- Python scripts: Data definitions and functions
- JavaScript scripts: Event handlers and client-side logic
- Mixed usage: Python data with JavaScript interactions

### 6. Component Composition
- Nested components: Button containing Label
- Slot usage: Passing content between components
- Dynamic props: Calculated values passed as props

## Simple Examples

### Basic Component
```pytempl
component Greeting(props) {
  <template>
    <h1>Hello, {{ props.get("name", "World") }}!</h1>
  </template>
}

component App() {
  <template>
    @Greeting({ "name": "PyTemplate" })
  </template>
}
```

### Conditional Content
```pytempl
component UserStatus(props) {
  <template>
    if props.get("logged_in", False) {
      <p>Welcome back, {{ props.get("username", "User") }}!</p>
    } else {
      <p>Please log in to continue</p>
    }
  </template>
}
```

### Simple Loop
```pytempl
component ItemList(props) {
  <template>
    <ul>
      for item in props.get("items", []) {
        <li>{{ item }}</li>
      }
    </ul>
  </template>
}
```

## Advanced Patterns

### Data-Driven UI
```pytempl
<script type="text/python">
  dashboard_data = {
    "metrics": [
      {"name": "Users", "value": 1234, "trend": "up"},
      {"name": "Revenue", "value": 56789, "trend": "up"},
      {"name": "Orders", "value": 890, "trend": "down"}
    ]
  }
</script>

<template>
  <div class="dashboard">
    for metric in dashboard_data["metrics"] {
      <div class="metric-card">
        <h3>{{ metric["name"] }}</h3>
        <p class="value">{{ str(metric["value"]) }}</p>
        <span class="trend {{ metric["trend"] }}">{{ metric["trend"] }}</span>
      </div>
    }
  </div>
</template>
```

### Form Handling
```pytempl
<script type="text/javascript">
  function handleSubmit(event) {
    event.preventDefault();
    const formData = new FormData(event.target);
    console.log("Form submitted:", Object.fromEntries(formData));
  }
</script>

<template>
  <form onsubmit="handleSubmit(event)">
    <input type="text" name="username" placeholder="Username" required>
    <input type="email" name="email" placeholder="Email" required>
    <button type="submit">Submit</button>
  </form>
</template>
```

## Best Practices from Examples

1. **Component Reusability**: Create small, focused components that can be reused
2. **Props with Defaults**: Always provide default values for props
3. **Script Organization**: Separate data, functions, and client-side logic
4. **Conditional Logic**: Use clear, readable conditional statements
5. **Loop Efficiency**: Keep loop logic simple and efficient
6. **Error Handling**: Include fallbacks for missing data
7. **Styling**: Use CSS classes for consistent styling
8. **Accessibility**: Include proper HTML semantics and ARIA attributes
