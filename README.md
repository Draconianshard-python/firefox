# firefox
# Python Web Browser

A web-based browser interface that uses PyScript to run Python code directly in the browser. This implementation allows for URL fetching, history tracking, and response caching without requiring a backend server.

## Features

- Fetch and display web pages
- Track browsing history
- Cache responses for faster loading
- Clear cache functionality
- Modern UI with loading indicators

## How it Works

This browser interface uses:
- PyScript for running Python code in the browser
- Python's `pyfetch` for making HTTP requests
- Browser's localStorage for caching
- Modern HTML/CSS for the user interface

## Usage

1. Enter a URL in the input field
2. Click "Fetch URL" to load the page
3. View browsing history with "Show History"
4. Clear the cache with "Clear Cache"

## Note

Due to browser security restrictions (CORS), some websites may not allow direct fetching of their content. This is a limitation of browser security policies, not the implementation.
