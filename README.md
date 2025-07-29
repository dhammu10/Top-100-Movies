
# 🎬 Top 100 Movies Scraper

This project is a simple Python web scraper that extracts the list of top 100 movies from a historical version of Empire Online’s website using `requests` and `BeautifulSoup`, then saves it to a `.txt` file.

## 🌐 Source URL

The scraper uses an archived snapshot of the page from the [Wayback Machine](https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/).

## 🛠️ Technologies Used

- Python 🐍
- requests 📡
- BeautifulSoup 🍲 (bs4)

## 📄 How It Works

1. Sends a GET request to the archived URL.
2. Parses the HTML content using BeautifulSoup.
3. Extracts movie titles from `<h3>` tags with class `title`.
4. Reverses the list to maintain rank order (1 to 100).
5. Writes the movie titles to a file named `movies.text`.

## 📁 Output

A plain text file `movies.text` containing the top 100 movies, one per line.

## 💻 How to Run

```bash
git clone https://github.com/your-username/movie-scraper.git
cd movie-scraper
pip install -r requirements.txt
python main.py
