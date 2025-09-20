# Getting Started

PyTemplate is a powerful template engine that allows you to build component-based web applications using Python logic and familiar HTML-like syntax.

## What is PyTemplate?

PyTemplate transpiles `.pytempl` files into pure Python code, enabling you to:

- Create reusable components with props and slots
- Use Python expressions and logic in your templates
- Include both Python and JavaScript code
- Build dynamic, data-driven web applications

## Basic Syntax

A PyTemplate file consists of:

1. **Python imports** at the top
2. **Component definitions** with templates
3. **Script blocks** for Python and JavaScript code
4. **HTML-like template syntax** with interpolation

## Your First Component

Here's a simple example:

```pytempl
component HelloWorld(props) {
  <template>
    <h1>Hello, {{ props.get("name", "World") }}!</h1>
    <p>Count: {{ props.get("count", 0) }}</p>
  </template>
}

component App() {
  <template>
    <div>
      @HelloWorld({ "name": "PyTemplate", "count": 42 })
    </div>
  </template>
}
```

## Key Features

### 1. Component Definition

```pytempl
component ComponentName(props) {
  <template>
    <!-- Your HTML template here -->
  </template>
}
```

### 2. Interpolation

```pytempl
{{ python_expression }}
```

### 3. Component Usage

```pytempl
@ComponentName({ "prop1": "value1", "prop2": "value2" })
```

### 4. Conditional Rendering

```pytempl
if condition {
  <p>This shows when condition is true</p>
} else {
  <p>This shows when condition is false</p>
}
```

### 5. Loops

```pytempl
for item in items {
  <div>{{ item }}</div>
}
```

### 6. Scripts

```pytempl
<script type="text/python">
  # Python code here
  data = ["item1", "item2", "item3"]
</script>

<script type="text/javascript">
  // JavaScript code here
  function handleClick() {
    alert("Button clicked!");
  }
</script>
```

## Next Steps

- Learn about [Components](/components) in detail
- Explore [Interpolation and Expressions](/interpolation)
- Master [Conditional Rendering](/conditionals)
- Understand [Loops and Iteration](/loops)
- Discover [Script Integration](/scripts)

## Example Project

Check out the [Examples](https://github.com/nexios-labs/pytempl/tree/main/examples) section to see a complete demo application showcasing all PyTemplate features.
