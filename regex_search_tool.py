
import re

def search_pattern(filename, pattern, search_type):
    """Search for a given pattern in a file and display results."""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        count = 0
        for i, line in enumerate(lines, start=1):
            matches = re.findall(pattern, line)
            if matches:
                count += len(matches)
                print(f"{search_type.capitalize()} found on line {i}: {matches}")
        
        print(f"\nTotal {search_type} found: {count}\n")

    except FileNotFoundError:
        print("Error: File not found. Please check the file path.")

# File path (modify as needed)
filename = "E:\\4TH SEMESTER\\TOA\\RegexText.txt"

# User Input
print("Choose search type: emails, date, urls, contactNo")
search_type = input("Enter search type: ").strip().lower()

# Define regex patterns for different searches
patterns = {
    "emails": r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",
    "date": r"\b\d{2,4}[./-]\d{1,2}[./-]\d{2,4}\b",
    "urls": r"https?://[\w.-]+(?:\.[\w.-]+)+(?:/[\w./?%&=-]*)?",
    "contactno": r"\b(?:\+?\d{1,3}[-.\s]?)?(?:\d{3}[-.\s]?\d{3}[-.\s]?\d{4})\b"
}

if search_type in patterns:
    search_pattern(filename, patterns[search_type], search_type)
else:
    print("Invalid search type! Please choose from emails, date, urls, contactNo.")

"""
### **Improvements Made**
✅ **Modularized Code:** Function `search_pattern()` handles all search operations.  
✅ **Better Regex Patterns:** Improved accuracy for emails, dates, URLs, and contact numbers.  
✅ **Proper File Handling:** Uses `with open()` to ensure files are properly closed.  
✅ **Formatted Output:** Displays line numbers and counts matches properly.  
✅ **User-Friendly Input:** Asks users to enter search type and provides guidance.  

This version is **more efficient, readable, and robust**.
"""
