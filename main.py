from playwright.sync_api import sync_playwright
from word_list_analyzer import WordListAnalyzer

with open("wordleans.txt", "r") as file:
    word_list = sorted([line.strip().lower() for line in file.readlines()])

with (sync_playwright() as p):
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://www.nytimes.com/games/wordle/index.html")

    try:
        page.get_by_role("button", name="Reject all").click(timeout=5000)
    except:
        pass

    try:
        page.get_by_role("button", name="Play").click(timeout=5000)
    except:
        pass
    page.mouse.wheel(0, 1000)

    analyzer = WordListAnalyzer()

    word = "crane"
    word = word.lower()

    print(f"Initial word list length: {len(word_list)}")

    rows = page.locator("div[class*='Row-module_row__']")
    for i in range(rows.count()):
        page.keyboard.type(word)
        page.keyboard.press("Enter")

        page.wait_for_timeout(2000)

        solved = False

        tiles_row = rows.nth(i).locator("div[data-state]")
        pattern = []
        for j in range(tiles_row.count()):
            status = tiles_row.nth(j).get_attribute("data-state")

            if status == "absent":
                pattern.append("absent")
            elif status == "present":
                pattern.append("present")
            else:
                pattern.append("correct")

        pattern = tuple(pattern)
        if pattern == ("correct", "correct", "correct", "correct", "correct"):
            solved = True

        new_word_list = []
        for candidate in word_list:
            if analyzer.get_pattern(word, candidate) == pattern:
                new_word_list.append(candidate)
        word_list = new_word_list

        print(f"Word list length (Row {i + 1}): {len(word_list)}")

        if solved:
            break
        if i == rows.count() - 1:
            print("\nI lost :(")
            break
        if len(word_list) == 0:
            print("\nNo more words")
            break

        word = analyzer.shannon_entropy_next_word(word_list)


    input("\nPress Enter to exit...")
    browser.close()