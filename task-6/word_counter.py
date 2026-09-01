
# 1. SOURCE CODE: Task_6_Word_Count_Tool/word_counter.py


import os
import re
from collections import Counter


class TextAnalyzer:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.raw_text = ""
        self.lines_count = 0
        self.words_count = 0
        self.chars_count_with_spaces = 0
        self.chars_count_no_spaces = 0
        self.word_frequencies = Counter()

    def load_and_analyze(self):
        """Reads the target file and calculates text statistics and word frequencies."""
        if not os.path.exists(self.file_path):
            raise FileNotFoundError(f"File not found: '{self.file_path}'")

        try:
            with open(self.file_path, "r", encoding="utf-8") as file:
                lines = file.readlines()
        except UnicodeDecodeError:
            with open(self.file_path, "r", encoding="latin-1") as file:
                lines = file.readlines()

        self.lines_count = len(lines)
        self.raw_text = "".join(lines)
        self.chars_count_with_spaces = len(self.raw_text)
        self.chars_count_no_spaces = len(re.sub(r"\s+", "", self.raw_text))

        # Extract words using regex (ignoring punctuation and normalizing to lower case)
        words = re.findall(r"\b[a-zA-Z0-9_']+\b", self.raw_text.lower())
        self.words_count = len(words)
        self.word_frequencies = Counter(words)

    def generate_report(self, top_n: int = 10) -> str:
        """Generates a structured string report of the analysis metrics."""
        report = []
        report.append("==================================================")
        report.append("          TEXT FILE ANALYSIS REPORT               ")
        report.append("==================================================")
        report.append(f"Target File              : {os.path.basename(self.file_path)}")
        report.append(f"Total Lines              : {self.lines_count}")
        report.append(f"Total Words              : {self.words_count}")
        report.append(f"Characters (with spaces) : {self.chars_count_with_spaces}")
        report.append(f"Characters (no spaces)   : {self.chars_count_no_spaces}")
        report.append(f"Unique Words             : {len(self.word_frequencies)}")
        report.append("--------------------------------------------------")
        report.append(f"Top {top_n} Most Common Words:")
        report.append(f"{'Rank':<6}{'Word':<20}{'Frequency':<10}")
        report.append("-" * 36)

        for rank, (word, freq) in enumerate(self.word_frequencies.most_common(top_n), 1):
            report.append(f"{rank:<6}{word:<20}{freq:<10}")
        
        report.append("==================================================")
        return "\n".join(report)

    def save_report_to_file(self, output_path: str = "analysis_report.txt", top_n: int = 10):
        """Exports the generated report to a file."""
        report_text = self.generate_report(top_n)
        with open(output_path, "w", encoding="utf-8") as file:
            file.write(report_text)
        print(f"\nAnalysis report successfully saved to: '{output_path}'")


def main():
    print("\n==========================================")
    print("      WORD COUNT & TEXT ANALYSIS TOOL     ")
    print("==========================================")

    file_path = input("Enter path to text file: ").strip()
    if not file_path:
        print("[Error]: File path cannot be empty.")
        return

    analyzer = TextAnalyzer(file_path)

    try:
        analyzer.load_and_analyze()
        report = analyzer.generate_report(top_n=10)
        print("\n" + report)

        save_choice = input("\nDo you want to save this report to a file? (y/n): ").strip().lower()
        if save_choice in ("y", "yes"):
            out_name = input("Enter report output file name [Default: analysis_report.txt]: ").strip()
            if not out_name:
                out_name = "analysis_report.txt"
            analyzer.save_report_to_file(out_name)

    except Exception as e:
        print(f"\n[Analysis Error]: {e}")


if __name__ == "__main__":
    main()
