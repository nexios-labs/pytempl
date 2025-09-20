# Loops and Iteration

Loops allow you to iterate over collections and generate dynamic content. PyTemplate supports `for` loops for rendering lists, arrays, and other iterable data.

## Basic For Loop

Use `for` to iterate over collections:

```pytempl
for item in items {
  <div>{{ item }}</div>
}
```

## Iterating Over Lists

Loop through Python lists:

```pytempl
<script type="text/python">
  colors = ["red", "green", "blue", "purple", "orange"]
</script>

<template>
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
</template>
```

## Iterating Over Dictionaries

Loop through lists of dictionaries:

```pytempl
<script type="text/python">
  todos = [
    {"text": "Learn template engine", "done": True, "priority": 9},
    {"text": "Build awesome app", "done": False, "priority": 16}, 
    {"text": "Deploy to production", "done": False, "priority": 25}
  ]
</script>

<template>
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
</template>
```

## Using Range for Numbers

Generate loops with numeric ranges:

```pytempl
<div class="button-group">
  for i in {{ range(3) }} {
    @Button({ "onclick": "showAlert('hello')", "count": {{ (i + 1) * (i + 1) }} }) {
      Dynamic Button {{ str(i + 1) }}
    }
  }
</div>
```

## Loop with Index

Access both the item and its index:

```pytempl
for i, item in enumerate(items) {
  <div class="item-{{ str(i) }}">
    <span class="index">{{ str(i + 1) }}</span>
    <span class="content">{{ item }}</span>
  </div>
}
```

## Nested Loops

You can nest loops for complex data structures:

```pytempl
<script type="text/python">
  categories = [
    {
      "name": "Frontend",
      "items": ["React", "Vue", "Angular"]
    },
    {
      "name": "Backend", 
      "items": ["Python", "Node.js", "Java"]
    }
  ]
</script>

<template>
  for category in categories {
    <div class="category">
      <h3>{{ category["name"] }}</h3>
      <ul>
        for item in category["items"] {
          <li>{{ item }}</li>
        }
      </ul>
    </div>
  }
</template>
```

## Conditional Loops

Combine loops with conditionals:

```pytempl
for todo in todos {
  if todo["done"] {
    <div class="completed-todo">
      <span class="completed">{{ todo["text"] }}</span>
    </div>
  } else {
    <div class="pending-todo">
      <span>{{ todo["text"] }}</span>
      <button onclick="markDone({{ todo["id"] }})">Mark Done</button>
    </div>
  }
}
```

## Loop with Components

Use components within loops:

```pytempl
<div class="product-grid">
  for product in products {
    @ProductCard({
      "name": {{ product["name"] }},
      "price": {{ product["price"] }},
      "image": {{ product["image"] }},
      "id": {{ product["id"] }}
    })
  }
</div>
```

## Dynamic Loop Content

Generate different content based on loop data:

```pytempl
for user in users {
  <div class="user-card">
    <h4>{{ user["name"] }}</h4>
    
    if user["role"] == "admin" {
      <span class="admin-badge">Admin</span>
      @AdminControls({ "user_id": {{ user["id"] }} })
    } else {
      <span class="user-badge">User</span>
      @UserControls({ "user_id": {{ user["id"] }} })
    }
    
    <div class="user-stats">
      for stat in user["stats"] {
        <div class="stat">
          <span class="stat-label">{{ stat["label"] }}</span>
          <span class="stat-value">{{ str(stat["value"]) }}</span>
        </div>
      }
    </div>
  </div>
}
```

## Loop with Mathematical Operations

Perform calculations within loops:

```pytempl
for i in {{ range(5) }} {
  <div class="math-item">
    <p>Number: {{ str(i) }}</p>
    <p>Square: {{ str(i * i) }}</p>
    <p>Cube: {{ str(i * i * i) }}</p>
    <p>Factorial: {{ str(math.factorial(i) if i <= 10 else "Too large") }}</p>
  </div>
}
```

## Filtering in Loops

Use conditional logic to filter items:

```pytempl
<!-- Show only completed todos -->
for todo in todos {
  if todo["done"] {
    @TodoItem({
      "text": {{ todo["text"] }},
      "done": {{ todo["done"] }}, 
      "priority": {{ todo["priority"] }}
    })
  }
}

<!-- Show only high priority items -->
for todo in todos {
  if todo["priority"] > 10 {
    @TodoItem({
      "text": {{ todo["text"] }},
      "done": {{ todo["done"] }}, 
      "priority": {{ todo["priority"] }}
    })
  }
}
```

## Loop with Dynamic Attributes

Set dynamic attributes based on loop data:

```pytempl
for item in items {
  <div 
    class="{{ "item-" + str(item["id"]) }}"
    data-priority="{{ str(item["priority"]) }}"
    data-status="{{ item["status"] }}"
  >
    <h3>{{ item["title"] }}</h3>
    <p>{{ item["description"] }}</p>
  </div>
}
```

## Common Loop Patterns

### Table Generation
```pytempl
<table class="data-table">
  <thead>
    <tr>
      <th>Name</th>
      <th>Email</th>
      <th>Role</th>
      <th>Actions</th>
    </tr>
  </thead>
  <tbody>
    for user in users {
      <tr>
        <td>{{ user["name"] }}</td>
        <td>{{ user["email"] }}</td>
        <td>{{ user["role"] }}</td>
        <td>
          <button onclick="editUser({{ user["id"] }})">Edit</button>
          <button onclick="deleteUser({{ user["id"] }})">Delete</button>
        </td>
      </tr>
    }
  </tbody>
</table>
```

### Card Grid
```pytempl
<div class="card-grid">
  for card in cards {
    <div class="card">
      <img src="{{ card["image"] }}" alt="{{ card["title"] }}">
      <h3>{{ card["title"] }}</h3>
      <p>{{ card["description"] }}</p>
      <button onclick="selectCard({{ card["id"] }})">Select</button>
    </div>
  }
</div>
```

### Navigation Menu
```pytempl
<nav class="main-nav">
  <ul>
    for item in menu_items {
      <li class="{{ "active" if item["current"] else "" }}">
        <a href="{{ item["url"] }}">{{ item["label"] }}</a>
      </li>
    }
  </ul>
</nav>
```

## Best Practices

1. **Keep loop logic simple** - complex operations should be in script blocks
2. **Use meaningful variable names** for loop variables
3. **Handle empty collections** gracefully
4. **Avoid deep nesting** - consider breaking complex loops into components
5. **Use components** for repeated complex structures

## Performance Considerations

- Loops are evaluated at render time
- Large collections may impact performance
- Consider pagination for large datasets
- Use efficient data structures in your Python code

## Common Gotchas

### Empty Collections
```pytempl
<!-- Handle empty lists gracefully -->
if len(items) > 0 {
  for item in items {
    <div>{{ item }}</div>
  }
} else {
  <p>No items available</p>
}
```

### String vs List Iteration
```pytempl
<!-- Iterating over a string gives characters -->
for char in "hello" {
  <span>{{ char }}</span>  <!-- h, e, l, l, o -->
}

<!-- Iterating over a list gives items -->
for word in ["hello", "world"] {
  <span>{{ word }}</span>  <!-- hello, world -->
}
```
