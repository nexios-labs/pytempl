# Scripts

PyTemplate supports both Python and JavaScript scripts within your templates. This allows you to define data, functions, and logic that can be used throughout your template.

## Python Scripts

Use `<script type="text/python">` to define Python code that will be available in your template:

```pytempl
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
```

## JavaScript Scripts

Use `<script type="text/javascript">` to define JavaScript code for client-side functionality:

```pytempl
<script type="text/javascript">
  function showAlert(message) {
    alert("Demo Alert: " + message);
  }
  
  function toggleCount() {
    count = count === 0 ? 5 : 0;
    console.log("Count toggled to:", count);
  }
</script>
```

## Data Definition

Define variables and data structures in Python scripts:

```pytempl
<script type="text/python">
  # Simple variables
  user_name = "John Doe"
  is_logged_in = True
  user_count = 42
  
  # Lists and arrays
  menu_items = [
    {"label": "Home", "url": "/", "active": True},
    {"label": "About", "url": "/about", "active": False},
    {"label": "Contact", "url": "/contact", "active": False}
  ]
  
  # Dictionaries
  user_profile = {
    "name": "John Doe",
    "email": "john@example.com",
    "role": "admin",
    "permissions": ["read", "write", "delete"]
  }
  
  # Complex data structures
  products = [
    {
      "id": 1,
      "name": "Widget A",
      "price": 29.99,
      "category": "electronics",
      "in_stock": True
    },
    {
      "id": 2,
      "name": "Widget B", 
      "price": 39.99,
      "category": "electronics",
      "in_stock": False
    }
  ]
</script>
```

## Function Definitions

Define Python functions for reusable logic:

```pytempl
<script type="text/python">
  def get_user_greeting():
    if is_logged_in:
      return f"Welcome back, {user_name}!"
    else:
      return "Please log in to continue"
  
  def calculate_total_price(items):
    return sum(item["price"] for item in items if item["in_stock"])
  
  def get_available_products():
    return [product for product in products if product["in_stock"]]
  
  def format_price(price):
    return f"${price:.2f}"
  
  def get_user_permissions():
    if user_profile["role"] == "admin":
      return user_profile["permissions"]
    else:
      return ["read"]
</script>
```

## Using Script Data in Templates

Access variables and call functions defined in scripts:

```pytempl
<template>
  <div class="user-info">
    <h1>{{ get_user_greeting() }}</h1>
    <p>Total users: {{ str(user_count) }}</p>
    <p>Available products: {{ str(len(get_available_products())) }}</p>
    <p>Total value: {{ format_price(calculate_total_price(products)) }}</p>
  </div>
  
  <nav>
    for item in menu_items {
      <a href="{{ item["url"] }}" class="{{ "active" if item["active"] else "" }}">
        {{ item["label"] }}
      </a>
    }
  </nav>
</template>
```

## JavaScript Integration

Use JavaScript functions for client-side interactions:

```pytempl
<script type="text/javascript">
  let currentUser = null;
  let cartItems = [];
  
  function addToCart(productId) {
    const product = products.find(p => p.id === productId);
    if (product && product.in_stock) {
      cartItems.push(product);
      updateCartDisplay();
    }
  }
  
  function updateCartDisplay() {
    const cartElement = document.getElementById('cart');
    cartElement.textContent = `Cart (${cartItems.length})`;
  }
  
  function showProductDetails(productId) {
    const product = products.find(p => p.id === productId);
    if (product) {
      alert(`Product: ${product.name}\nPrice: $${product.price}`);
    }
  }
</script>

<template>
  <div class="product-list">
    for product in products {
      <div class="product-card">
        <h3>{{ product["name"] }}</h3>
        <p>Price: {{ format_price(product["price"]) }}</p>
        if product["in_stock"] {
          <button onclick="addToCart({{ product["id"] }})">Add to Cart</button>
        } else {
          <button disabled>Out of Stock</button>
        }
        <button onclick="showProductDetails({{ product["id"] }})">View Details</button>
      </div>
    }
  </div>
  
  <div id="cart">Cart (0)</div>
</template>
```

## Complex Example from Demo

Here's how scripts are used in the demo:

```pytempl
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
    </div>
  </div>
</template>
```

## Script Organization

### Multiple Script Blocks

You can have multiple script blocks in a single component:

```pytempl
<script type="text/python">
  # Data definitions
  users = []
  current_user = None
</script>

<script type="text/javascript">
  // Client-side utilities
  function formatDate(date) {
    return new Date(date).toLocaleDateString();
  }
</script>

<script type="text/python">
  # Functions that use the data
  def get_current_user():
    return current_user
  
  def is_admin():
    return current_user and current_user.get("role") == "admin"
</script>
```

### Import Statements

Include Python imports at the top of your file or in script blocks:

```pytempl
import math
from datetime import datetime
from typing import List, Dict

<script type="text/python">
  def calculate_compound_interest(principal, rate, time):
    return principal * (1 + rate) ** time
  
  def get_current_timestamp():
    return datetime.now().isoformat()
</script>
```

## Best Practices

1. **Separate concerns** - use Python for data and logic, JavaScript for interactions
2. **Keep scripts focused** - each script block should have a clear purpose
3. **Use meaningful names** - make variables and functions self-documenting
4. **Handle errors gracefully** - include error handling in your functions
5. **Document complex logic** - add comments for complex operations

## Common Patterns

### Data Fetching Simulation
```pytempl
<script type="text/python">
  def fetch_user_data():
    # Simulate API call
    return {
        "name": "John Doe",
        "email": "john@example.com",
        "last_login": "2024-01-15"
    }
  
  user_data = fetch_user_data()
</script>
```

### State Management
```pytempl
<script type="text/python">
  # Application state
  app_state = {
      "current_page": "home",
      "user_preferences": {},
      "notifications": []
  }
  
  def set_current_page(page):
      app_state["current_page"] = page
  
  def add_notification(message, type="info"):
      app_state["notifications"].append({
          "message": message,
          "type": type,
          "timestamp": datetime.now()
      })
</script>
```

### Utility Functions
```pytempl
<script type="text/python">
  def truncate_text(text, max_length=100):
      if len(text) <= max_length:
          return text
      return text[:max_length] + "..."
  
  def format_currency(amount):
      return f"${amount:,.2f}"
  
  def get_initial_letters(name):
      return "".join(word[0].upper() for word in name.split())
</script>
```

## Performance Considerations

- Python scripts are executed at template compilation time
- JavaScript scripts are included in the final output
- Keep Python logic lightweight for better performance
- Use JavaScript for heavy client-side operations
- Consider caching expensive calculations
