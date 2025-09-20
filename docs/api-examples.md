# PyTemplate API Reference

This page provides a comprehensive reference for PyTemplate's API and syntax.

## Component API

### Component Definition
```pytempl
component ComponentName(props) {
  <template>
    <!-- Template content -->
  </template>
}
```

### Props API
```pytempl
<!-- Access props with default values -->
{{ props.get("key", "default_value") }}

<!-- Examples -->
{{ props.get("name", "Anonymous") }}
{{ props.get("count", 0) }}
{{ props.get("enabled", False) }}
```

### Slot API
```pytempl
<!-- Define slot in component -->
@slot()

<!-- Use slot content -->
@ComponentName({ "prop": "value" }) {
  <!-- This content goes into @slot() -->
}
```

## Interpolation API

### Basic Interpolation
```pytempl
{{ python_expression }}

<!-- Examples -->
{{ str(variable) }}
{{ str(math.sqrt(16)) }}
{{ "Hello " + name }}
{{ props.get("title", "Default") }}
```

### String Conversion
```pytempl
<!-- Always use str() for display -->
{{ str(number) }}
{{ str(boolean) }}
{{ str(list) }}
{{ str(dict) }}
```

## Control Structures API

### Conditional Rendering
```pytempl
if condition {
  <!-- Content when true -->
} else {
  <!-- Content when false -->
}

if condition1 {
  <!-- Content 1 -->
} elif condition2 {
  <!-- Content 2 -->
} else {
  <!-- Content 3 -->
}
```

### Loops
```pytempl
for item in collection {
  <!-- Repeat for each item -->
}

<!-- Examples -->
for user in users {
  <div>{{ user["name"] }}</div>
}

for i in {{ range(5) }} {
  <span>{{ str(i) }}</span>
}
```

## Script API

### Python Scripts
```pytempl
<script type="text/python">
  # Variables
  variable_name = "value"
  
  # Functions
  def function_name():
    return "result"
  
  # Data structures
  data = {"key": "value"}
</script>
```

### JavaScript Scripts
```pytempl
<script type="text/javascript">
  function functionName() {
    // JavaScript code
  }
  
  // Variables
  let variable = "value";
</script>
```

## Component Usage API

### Basic Usage
```pytempl
@ComponentName({ "prop1": "value1", "prop2": "value2" })
```

### With Slot Content
```pytempl
@ComponentName({ "prop": "value" }) {
  <!-- Slot content -->
}
```

### Nested Components
```pytempl
@OuterComponent({ "prop": "value" }) {
  @InnerComponent({ "inner_prop": "inner_value" }) {
    <!-- Nested slot content -->
  }
}
```

## Built-in Functions

### String Functions
```pytempl
{{ str(value) }}           <!-- Convert to string -->
{{ len(collection) }}      <!-- Get length -->
{{ "text".title() }}       <!-- Title case -->
{{ "text".upper() }}       <!-- Uppercase -->
{{ "text".lower() }}       <!-- Lowercase -->
```

### Mathematical Functions
```pytempl
{{ str(math.sqrt(16)) }}   <!-- Square root -->
{{ str(abs(-5)) }}         <!-- Absolute value -->
{{ str(sum([1,2,3])) }}    <!-- Sum of list -->
{{ str(max([1,2,3])) }}    <!-- Maximum value -->
{{ str(min([1,2,3])) }}    <!-- Minimum value -->
```

### Collection Functions
```pytempl
{{ str(len(list)) }}       <!-- List length -->
{{ str(range(5)) }}        <!-- Range generator -->
{{ str(enumerate(list)) }} <!-- Enumerate with index -->
```

## Common Patterns

### Dynamic Attributes
```pytempl
<div class="{{ "active" if is_active else "inactive" }}">
<input type="checkbox" {{ "checked" if is_checked else "" }}>
```

### Conditional Classes
```pytempl
<div class="{{ "warning" if has_error else "success" }}">
```

### Event Handlers
```pytempl
<button onclick="{{ props.get("onclick", "") }}">
```

### Data Access
```pytempl
{{ dict["key"] }}          <!-- Dictionary access -->
{{ list[0] }}              <!-- List access -->
{{ obj.attribute }}        <!-- Object attribute -->
```

## Error Handling

### Safe Property Access
```pytempl
{{ props.get("key", "default") }}  <!-- Safe with default -->
{{ dict.get("key", "default") }}   <!-- Safe dictionary access -->
```

### Conditional Checks
```pytempl
{{ str(value) if value is not None else "N/A" }}
{{ str(len(items)) if items else "0" }}
```

## Best Practices

1. **Always use `str()`** for converting values to strings
2. **Provide default values** for all props and dictionary access
3. **Keep expressions simple** - complex logic in script blocks
4. **Use meaningful names** for variables and functions
5. **Handle edge cases** with conditional expressions
6. **Test your templates** to ensure they work as expected
