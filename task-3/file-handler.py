import os


class TextFileProcessor:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def read_content(self) -> str:
        """Reads and returns the content of the text file with error handling."""
        if not os.path.exists(self.file_path):
            raise FileNotFoundError(f"The file '{self.file_path}' does not exist.")
        
        try:
            with open(self.file_path, "r", encoding="utf-8") as file:
                return file.read()
        except PermissionError:
            raise PermissionError(f"Permission denied to read '{self.file_path}'.")
        except UnicodeDecodeError:
            raise UnicodeDecodeError("utf-8", b"", 0, 1, f"Failed to decode '{self.file_path}'. Ensure it is a valid text file.")

    def find_and_replace(self, target_word: str, replacement_word: str, output_path: str = None) -> int:
        """
        Finds occurrences of a target string, replaces them, and saves the result.
        Returns the total number of replacements made.
        """
        content = self.read_content()
        count = content.count(target_word)
        
        if count == 0:
            return 0
        
        updated_content = content.replace(target_word, replacement_word)
        save_target = output_path if output_path else self.file_path
        
        try:
            with open(save_target, "w", encoding="utf-8") as file:
                file.write(updated_content)
        except PermissionError:
            raise PermissionError(f"Permission denied to write to '{save_target}'.")
        
        return count


def main():
    print("\n==========================================")
    print("      BASIC FILE HANDLING UTILITY         ")
    print("==========================================")
    
    file_path = input("Enter the path to the text file: ").strip()
    processor = TextFileProcessor(file_path)

    try:
        content = processor.read_content()
        print("\n--- Original File Content ---")
        print(content)
        print("-----------------------------\n")
    except Exception as e:
        print(f"\n[Error]: {e}")
        return

    target_word = input("Enter the word/phrase to find: ")
    if not target_word:
        print("\n[Error]: Target word cannot be empty.")
        return

    replacement_word = input("Enter the replacement word/phrase: ")
    save_option = input("Save to a new file? (y/n, default 'n' overwrites original): ").strip().lower()
    
    output_path = None
    if save_option in ("y", "yes"):
        output_path = input("Enter output file name (e.g., modified_output.txt): ").strip()
        if not output_path:
            output_path = None

    try:
        replacements = processor.find_and_replace(target_word, replacement_word, output_path)
        if replacements > 0:
            destination = output_path if output_path else file_path
            print(f"\nSuccess: Made {replacements} replacement(s). Saved to '{destination}'.")
        else:
            print(f"\nTarget word '{target_word}' was not found in the file. No changes made.")
    except Exception as e:
        print(f"\n[Error]: {e}")


if __name__ == "__main__":
    main()