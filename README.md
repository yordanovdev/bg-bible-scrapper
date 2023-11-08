# Bible Scraper

This Python script is designed to scrape Bible verses from the Bible.com website and store the data in a structured JSON format.

## Prerequisites
- Python 3
- Requests library
- Beautiful Soup library

## Installation
1. Clone the repository or download the script.
2. Install the required libraries using the following command:
   ```bash
   pip install -r requirements.txt 
   ```

## Usage
1. Create a JSON file named `books.json` containing the list of books and chapters you want to scrape. The structure should be as follows:
   ```json
   [
      {
         "usfm": "BookCode",
         "human": "BookName",
         "chapters": [
            {"usfm": "ChapterCode"},
            {"usfm": "ChapterCode"},
            ...
         ]
      },
      ...
   ]
   ```

2. Replace the value of the `version` variable with the desired Bible version code (e.g., "BG1940").

3. Run the script:
   ```bash
   python main.py
   ```

4. The script will output the progress as it scrapes each book and chapter.

5. The scraped data will be saved in a file named `data.json` in the same directory.

## Notes
- Ensure proper internet connectivity as the script fetches data from the Bible.com website.
- The script may take some time to run, depending on the number of books and chapters specified in the `books.json` file.

Feel free to customize the script according to your needs and contribute to its improvement!