# Conditional Rendering

Conditional rendering allows you to show or hide content based on conditions. PyTemplate supports `if`, `elif`, and `else` statements for dynamic content display.

## Basic If Statement

Use `if` to conditionally render content:

```pytempl
if condition {
  <p>This content shows when condition is true</p>
}
```

## If-Else Statement

Add an `else` clause for alternative content:

```pytempl
if props.get("done", False) {
  <input type="checkbox" checked="true" />
} else {
  <input type="checkbox" />
}
```

## If-Elif-Else Statement

Use `elif` for multiple conditions:

```pytempl
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
```

## Complex Conditional Example

Here's a comprehensive example from the demo:

```pytempl
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
```

## Conditional Attributes

Use conditionals to set dynamic attributes:

```pytempl
<!-- Dynamic class names -->
<div class="{{ "warning" if count == 0 else "info" }}">

<!-- Conditional attributes -->
if props.get("done", False) {
  <input type="checkbox" checked="true" />
} else {
  <input type="checkbox" />
}
```

## Conditional Components

Render different components based on conditions:

```pytempl
if user_type == "admin" {
  @AdminPanel()
} elif user_type == "user" {
  @UserPanel()
} else {
  @GuestPanel()
}
```

## Nested Conditionals

You can nest conditionals for complex logic:

```pytempl
if user_logged_in {
  if user_role == "admin" {
    <div class="admin-content">
      <h2>Admin Dashboard</h2>
      @AdminControls()
    </div>
  } else {
    <div class="user-content">
      <h2>User Dashboard</h2>
      @UserControls()
    </div>
  }
} else {
  <div class="login-prompt">
    <p>Please log in to continue</p>
    @LoginForm()
  </div>
}
```

## Conditional Lists

Show different content based on list states:

```pytempl
if len(todos) == 0 {
  <div class="empty-state">
    <p>No todos yet. Add one to get started!</p>
    @AddTodoButton()
  </div>
} else {
  <ul class="todo-list">
    for todo in todos {
      @TodoItem({
        "text": {{ todo["text"] }},
        "done": {{ todo["done"] }}, 
        "priority": {{ todo["priority"] }}
      })
    }
  </ul>
}
```

## Boolean Conditions

Use boolean values and expressions in conditions:

```pytempl
<!-- Direct boolean check -->
if is_active {
  <span class="status-active">Active</span>
}

<!-- Function return value -->
if get_status() == "active" {
  <p>System is running</p>
}

<!-- Comparison operators -->
if count > 0 {
  <p>Items available: {{ str(count) }}</p>
}

if count == 0 {
  <p>No items available</p>
}
```

## Conditional Styling

Apply different styles based on conditions:

```pytempl
<!-- Dynamic class names -->
<div class="{{ "completed" if props.get("done", False) else "pending" }}">
  {{ props.get("text", "Todo item") }}
</div>

<!-- Conditional CSS classes -->
if props.get("done", False) {
  <span class="completed">
    {{ props.get("text", "Todo item") }}
  </span>  
} else {
  <span>
    {{ props.get("text", "Todo item") }}
  </span>
}
```

## Common Conditional Patterns

### Loading States
```pytempl
if loading {
  <div class="spinner">Loading...</div>
} else {
  <div class="content">
    <!-- Your content here -->
  </div>
}
```

### Error Handling
```pytempl
if error {
  <div class="error">
    <p>Error: {{ error }}</p>
    <button onclick="retry()">Retry</button>
  </div>
} else {
  <!-- Normal content -->
}
```

### User Authentication
```pytempl
if user_authenticated {
  <div class="authenticated-content">
    <p>Welcome, {{ user_name }}!</p>
    @UserMenu()
  </div>
} else {
  <div class="login-form">
    @LoginForm()
  </div>
}
```

### Feature Flags
```pytempl
if feature_enabled("new_ui") {
  @NewUIComponent()
} else {
  @LegacyUIComponent()
}
```

## Best Practices

1. **Keep conditions simple** - complex logic should be in script blocks
2. **Use meaningful variable names** for better readability
3. **Provide fallback content** with else clauses when appropriate
4. **Test edge cases** to ensure conditions work as expected
5. **Use consistent formatting** for better code maintainability

## Performance Considerations

- Conditions are evaluated at render time
- Keep conditional logic lightweight
- Avoid complex calculations within conditions
- Consider moving heavy logic to script blocks

## Common Gotchas

### String vs Boolean
```pytempl
<!-- Wrong - string "false" is truthy -->
if props.get("enabled", "false") {
  <!-- This will always render -->
}

<!-- Correct - use actual boolean -->
if props.get("enabled", False) {
  <!-- This works as expected -->
}
```

### None Checks
```pytempl
<!-- Safe way to check for None -->
if user is not None {
  <p>Welcome, {{ user.name }}!</p>
} else {
  <p>Please log in</p>
}
```
