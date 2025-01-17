# Code Blocks Examples

## Basic Code Block

```python
def greet(name):
    return f"Hello, {name}!"

print(greet("World"))
```

## Code with Line Numbers

```python linenums="1"
class Calculator:
    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b
    
    def multiply(self, a, b):
        return a * b
    
    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
```

## Code with Highlighting

```python hl_lines="2 3"
def process_data(data):
    # This line is highlighted
    result = data.process()
    return result
```

## Different Languages

### JavaScript
```javascript
function fetchData() {
    return fetch('https://api.example.com/data')
        .then(response => response.json())
        .then(data => console.log(data));
}
```

### HTML
```html
<div class="container">
    <h1>Hello World</h1>
    <p>This is a paragraph.</p>
</div>
```

### CSS
```css
.container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 20px;
}
```

## Inline Code

You can use `inline code` within paragraphs.

## Code with Title

```python title="example.py"
def main():
    print("This is a code block with a title")

if __name__ == "__main__":
    main()
```
