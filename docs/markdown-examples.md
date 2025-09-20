# PyTemplate Syntax Examples

This page demonstrates PyTemplate syntax highlighting and provides examples of common patterns.

## Syntax Highlighting

PyTemplate files use the `.pytempl` extension and support syntax highlighting for:

- **Python code** in script blocks and interpolations
- **HTML-like template syntax** with component definitions
- **JavaScript code** in script blocks
- **CSS styles** in style blocks

### Example with Line Highlighting

```python{4,8,12}
# PyTemplate Component Example
component UserCard(props) {
  <template>
    <div class="user-card">
      <h3>{{ props.get("name", "Anonymous") }}</h3>
      <p>Email: {{ props.get("email", "No email") }}</p>
      if props.get("is_admin", False) {
        <span class="admin-badge">Admin</span>
      }
    </div>
  </template>
}
```

## Code Examples

### Basic Component
```html
<!-- PyTemplate Component -->
component Greeting(props) {
  <template>
    <h1>Hello, {{ props.get("name", "World") }}!</h1>
  </template>
}
```

### Component with Scripts

**Python Script Block:**
```python
<script type="text/python">
  def get_greeting(name):
    return f"Welcome, {name}!"
</script>
```

**JavaScript Script Block:**
```javascript
<script type="text/javascript">
  function showAlert(message) {
    alert(message);
  }
</script>
```

**Template Component:**
```html
<!-- PyTemplate Component -->
component Welcome(props) {
  <template>
    <div>
      <h2>{{ get_greeting(props.get("name", "Guest")) }}</h2>
      <button onclick="showAlert('Hello!')">Click me</button>
    </div>
  </template>
}
```

### Conditional Rendering
```html
<!-- PyTemplate Conditional Component -->
component StatusIndicator(props) {
  <template>
    if props.get("status") == "online" {
      <span class="status online">🟢 Online</span>
    } elif props.get("status") == "away" {
      <span class="status away">🟡 Away</span>
    } else {
      <span class="status offline">🔴 Offline</span>
    }
  </template>
}
```

### Loop Example

**Python Data:**
```python
<script type="text/python">
  items = [
    {"name": "Item 1", "price": 10.99},
    {"name": "Item 2", "price": 15.50},
    {"name": "Item 3", "price": 8.75}
  ]
</script>
```

**Template with Loop:**
```html
<!-- PyTemplate with Loop -->
<template>
  <div class="item-list">
    for item in items {
      <div class="item">
        <h4>{{ item["name"] }}</h4>
        <p>Price: ${{ str(item["price"]) }}</p>
      </div>
    }
  </div>
</template>
```

## Custom Containers

Use these containers to highlight important information:

::: info
**Info**: This is general information about PyTemplate features.
:::

::: tip
**Tip**: Always use `str()` when interpolating values to ensure proper string conversion.
:::

::: warning
**Warning**: Be careful with complex expressions in interpolation - keep them simple and readable.
:::

::: danger
**Danger**: Avoid using mutable objects as default values in props.get() - use immutable values instead.
:::

::: details
**Details**: Click to expand and see more information about PyTemplate internals.

PyTemplate transpiles your `.pytempl` files into pure Python code, which means all your template logic becomes executable Python that can be run in any Python environment.
:::

## Code Blocks

### Python Script Block
```python
<script type="text/python">
  # This is Python code
  users = [
    {"name": "Alice", "role": "admin"},
    {"name": "Bob", "role": "user"}
  ]
  
  def get_admin_users():
    return [user for user in users if user["role"] == "admin"]
</script>
```

### JavaScript Script Block
```javascript
<script type="text/javascript">
  // This is JavaScript code
  function handleUserClick(userId) {
    console.log('User clicked:', userId);
    // Handle user interaction
  }
  
  function updateUI(data) {
    document.getElementById('content').innerHTML = data;
  }
</script>
```

### HTML Template
```html
<template>
  <div class="container">
    <h1>{{ title }}</h1>
    <div class="content">
      <!-- Template content here -->
    </div>
  </div>
</template>
```

### CSS Styles
```css
<style>
  .container {
    max-width: 800px;
    margin: 0 auto;
    padding: 20px;
  }
  
  .user-card {
    border: 1px solid #ddd;
    border-radius: 8px;
    padding: 16px;
    margin: 8px 0;
  }
  
  .status.online { color: green; }
  .status.away { color: orange; }
  .status.offline { color: red; }
</style>
```

## Interactive Examples

### Toggle Component
```pytempl
<script type="text/javascript">
  function toggleVisibility(elementId) {
    const element = document.getElementById(elementId);
    element.style.display = element.style.display === 'none' ? 'block' : 'none';
  }
</script>

<template>
  <div>
    <button onclick="toggleVisibility('content')">Toggle Content</button>
    <div id="content" style="display: none;">
      <p>This content can be toggled!</p>
    </div>
  </div>
</template>
```

### Form Handling
```pytempl
<script type="text/javascript">
  function handleSubmit(event) {
    event.preventDefault();
    const formData = new FormData(event.target);
    const data = Object.fromEntries(formData);
    console.log('Form data:', data);
    // Process form data
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

## Best Practices

::: tip
**Use meaningful component names** that clearly describe their purpose and functionality.
:::

::: tip
**Keep interpolation expressions simple** - complex logic should be moved to script blocks or functions.
:::

::: tip
**Always provide default values** for props to make components more robust and reusable.
:::

::: tip
**Use slots for flexible content** - they make components more versatile and composable.
:::
