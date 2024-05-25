# Makefile for creating the book

# Default target
all: book.md book.html

# Target to create book.md
book.md: outline.py
	python outline.py > book.md

# Target to create book.html
book.html: outline.py
	python make_html.py > book.html



# Clean up generated files
clean:
	rm -f book.md book.html

.PHONY: all clean
