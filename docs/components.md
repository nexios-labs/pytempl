# Components

Components are the building blocks of PyTemplate applications. They allow you to create reusable, encapsulated pieces of UI with their own logic and styling.

## Component Definition

Components are defined using the `component` keyword followed by a name and optional props parameter:

```pytempl
component ComponentName(props) {
  <template>
    <!-- Your template content here -->
  </template>
}
```

## Props

Props allow you to pass data into components. Access props using the `props.get()` method:

```pytempl
component Label(props) {
  <template>
    <span class="text-red bg-black">
      {{ str(sqrt(int(props.get("count", "1")))) }}
    </span>
    <span>{{ props.get("text", "Click Me") }}</span>
  </template>
}
```

### Props.get() Method

- **Syntax**: `props.get(key, default_value)`
- **Parameters**:
  - `key`: The property name to retrieve
  - `default_value`: Value to return if the key doesn't exist
- **Returns**: The prop value or default value

## Component Usage

Use components with the `@` syntax and pass props as a dictionary:

```pytempl
@Label({ "count": 4, "text": "Button" })
```

### Example from Demo

```pytempl
component Button(props) {
  <template>
    <button onclick="{{ props.get("onclick", "") }}" class="demo-button">
      @Label({ 
        "count": {{ props.get("count", 4) }}, 
        "text": {{ props.get("label", "Button") }} 
      }) {
        @slot()
      }
    </button>
  </template>
}
```

## Slots

Slots allow you to pass content into components. Use `@slot()` to render the content passed between component tags:

```pytempl
component Button(props) {
  <template>
    <button>
      @Label({ "count": {{ props.get("count", 4) }}, "text": {{ props.get("label", "Button") }} }) {
        @slot()  <!-- This renders the content passed to the component -->
      }
    </button>
  </template>
}

<!-- Usage with slot content -->
@Button({ "onclick": "toggleCount()", "label": "Toggle", "count": {{ str(count * count) }} }) {
  Toggle Count  <!-- This content goes into @slot() -->
}
```

## Complex Component Example

Here's a more complex component from the demo:

```pytempl
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
```

## Component Composition

Components can be nested and composed together:

```pytempl
component App() {
  <template>
    <div class="demo-container">
      <h1>Template Engine Demo</h1>
      
      @Button({
        "onclick": "showAlert('Hello World!')",
        "label": "Alert", 
        "count": 64
      }) {
        Show Alert
      }
      
      <div class="todo-list">
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
  </template>
}
```

## Best Practices

1. **Use descriptive component names** that clearly indicate their purpose
2. **Provide default values** for all props using `props.get(key, default)`
3. **Keep components focused** on a single responsibility
4. **Use slots** for flexible content injection
5. **Compose components** to build complex UIs from simple building blocks

## Component Lifecycle

Components in PyTemplate are stateless by design. Each time a component is rendered, it receives fresh props and renders accordingly. This makes components predictable and easy to reason about.

## Styling Components

You can include CSS styles within your components or in separate style blocks:

```pytempl
component StyledComponent(props) {
  <template>
    <div class="my-component">
      <h2>{{ props.get("title", "Default Title") }}</h2>
      <p>{{ props.get("content", "Default content") }}</p>
    </div>
  </template>
  <style>
    .my-component {
        padding: 20px;
        border: 1px solid #ccc;
        border-radius: 8px;
    }
  </style>
}

```
