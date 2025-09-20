# Interpolation and Expressions

Interpolation allows you to embed Python expressions directly into your templates. Use double curly braces `{{ }}` to evaluate and display Python expressions.

## Basic Interpolation

The simplest form of interpolation displays the result of a Python expression:

```pytempl
<p>Current count: <strong>{{ str(count) }}</strong></p>
<p>Square root: {{ str(math.sqrt(count) if count > 0 else 0) }}</p>
```

## String Conversion

Always use `str()` to convert values to strings for display:

```pytempl
<!-- Correct -->
<span>{{ str(count) }}</span>
<span>{{ str(math.sqrt(count)) }}</span>

<!-- Incorrect - may cause errors -->
<span>{{ count }}</span>
```

## Complex Expressions

You can use any valid Python expression inside interpolation:

```pytempl
<!-- Mathematical operations -->
<p>Count squared: {{ str(count * count) }}</p>
<p>Sum of range: {{ str(sum(range(count + 1))) }}</p>

<!-- String operations -->
<p>Status: {{ "status-" + get_status() }}</p>
<p>Message: {{ get_message() }}</p>

<!-- Conditional expressions -->
<p>Mode: {{ "High" if count > 3 else "Low" }}</p>
```

## Props Interpolation

Access component props within interpolation:

```pytempl
component Label(props) {
  <template>
    <span>{{ props.get("text", "Default Text") }}</span>
    <span>{{ str(sqrt(int(props.get("count", "1")))) }}</span>
  </template>
}
```

## Dynamic Attributes

Use interpolation to set dynamic HTML attributes:

```pytempl
<!-- Dynamic class names -->
<div class="{{ "status-" + get_status() }}">
  <p>Content here</p>
</div>

<!-- Dynamic IDs -->
<span id="{{ str(count) }}">Item {{ str(count) }}</span>

<!-- Dynamic event handlers -->
<button onclick="{{ props.get("onclick", "") }}">
  Click me
</button>
```

## Component Props with Interpolation

Pass interpolated values as component props:

```pytempl
@Button({
  "onclick": "toggleCount()", 
  "label": "Toggle",
  "count": {{ str(count * count) }}  <!-- Interpolated value -->
}) {
  Toggle Count
}

@Label({
  "count": {{ count * count }}, 
  "text": "Low Mode"
}) { 
  {{ get_message() }}  <!-- Interpolated slot content -->
}
```

## String Concatenation

Combine strings and interpolated values:

```pytempl
<!-- In attributes -->
<div class="{{ "color-item color-" + color }}">

<!-- In content -->
<p>{{ "Color: " + color }}</p>
<p>{{ "System has " + str(count) + " items" }}</p>
```

## Mathematical Operations

Perform calculations within interpolation:

```pytempl
<!-- Basic arithmetic -->
<p>Count * 4: {{ str(count * 4) }}</p>
<p>Count squared: {{ str(count * count) }}</p>

<!-- Using imported functions -->
<p>Square root: {{ str(math.sqrt(count) if count > 0 else 0) }}</p>
<p>Length: {{ str(len(color)) }}</p>

<!-- Complex calculations -->
<p>Sum: {{ str(sum(range(count + 1))) }}</p>
```

## Conditional Interpolation

Use conditional expressions for dynamic values:

```pytempl
<!-- Ternary operator -->
<p>{{ "High activity" if count > 3 else "Low activity" }}</p>

<!-- With function calls -->
<p>{{ get_status() if count > 0 else "inactive" }}</p>

<!-- In attributes -->
<div class="{{ "warning" if count == 0 else "info" }}">
```

## Function Calls

Call Python functions within interpolation:

```pytempl
<!-- Simple function calls -->
<p>{{ get_status() }}</p>
<p>{{ get_message() }}</p>

<!-- Function calls with parameters -->
<p>{{ str(len(colors)) }}</p>
<p>{{ color.title() }}</p>
```

## Collection Access

Access dictionary and list elements:

```pytempl
<!-- Dictionary access -->
<p>{{ todo["text"] }}</p>
<p>{{ todo["done"] }}</p>
<p>{{ todo["priority"] }}</p>

<!-- List access -->
<p>{{ colors[0] }}</p>
<p>{{ str(len(colors)) }}</p>
```

## Best Practices

1. **Always use `str()`** for converting values to strings
2. **Keep expressions simple** - complex logic should be in script blocks
3. **Use meaningful variable names** for better readability
4. **Handle edge cases** with conditional expressions
5. **Test your expressions** to ensure they work as expected

## Common Patterns

### Dynamic Styling
```pytempl
<div class="{{ "active" if is_active else "inactive" }}">
```

### Conditional Content
```pytempl
<p>{{ "Welcome back!" if user_logged_in else "Please log in" }}</p>
```

### Formatted Numbers
```pytempl
<p>Price: ${{ str(price) }}</p>
<p>Percentage: {{ str(percentage) }}%</p>
```

### Dynamic URLs
```pytempl
<a href="/user/{{ str(user_id) }}">View Profile</a>
```

## Error Handling

Be careful with interpolation to avoid runtime errors:

```pytempl
<!-- Safe - provides default value -->
<p>{{ props.get("name", "Anonymous") }}</p>

<!-- Safe - checks for existence -->
<p>{{ str(len(items)) if items else "0" }}</p>

<!-- Potentially unsafe - could cause KeyError -->
<p>{{ user["name"] }}</p>

<!-- Better approach -->
<p>{{ user.get("name", "Unknown") }}</p>
```
