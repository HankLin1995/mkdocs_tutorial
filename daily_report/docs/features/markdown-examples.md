# Markdown Examples

This page demonstrates various Markdown features supported by MkDocs.

## Basic Formatting

**Bold text** and *italic text*

***Bold and italic text***

~~Strikethrough text~~

## Lists

Unordered list:

* Item 1
* Item 2
    * Subitem 2.1
    * Subitem 2.2
* Item 3

Ordered list:

1. First item
2. Second item
3. Third item

Task list:

- [x] Completed task
- [ ] Incomplete task
- [ ] Another task

## Tables

| Header 1 | Header 2 | Header 3 |
|----------|----------|----------|
| Cell 1   | Cell 2   | Cell 3   |
| Cell 4   | Cell 5   | Cell 6   |

## Blockquotes

> This is a blockquote
> 
> It can span multiple lines
>> And can be nested

## Code

Inline code: `print("Hello, World!")`

Code block with syntax highlighting:

```python
def hello_world():
    print("Hello, World!")
    return True

# Function call
hello_world()
```

## Links and Images

[Link to Google](https://www.google.com)

![Image Alt Text](https://via.placeholder.com/150)

## Images with Width

Default image:
![Default Image](https://via.placeholder.com/800x400)

Image with pixel width:
![300px Width Image](https://via.placeholder.com/800x400){ width="300" }

Image with percentage width:
![50% Width Image](https://via.placeholder.com/800x400){ width="50%" }

Image with auto width and max-width:
![Auto Width Image](https://via.placeholder.com/800x400){ .width-auto }

## Footnotes

Here's a sentence with a footnote[^1].

[^1]: This is the footnote content.

## Definition Lists

Term 1
:   Definition 1

Term 2
:   Definition 2
:   Definition 2.1
