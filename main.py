"""
Two-Sentence Horror entry: 236 characters, exactly two sentences.
Writes the story to $MAKEFUN_OUTPUT_DIR/entry.txt and stdout.
"""
import os
import sys

STORY = (
    "I keep my spare key tucked inside a fake plastic rock among the succulents "
    "on my third-floor apartment balcony. I woke up this morning to the metallic "
    "taste of brass on my tongue and the rock sitting on my chest, cracked neatly in half."
)

def main():
    output_dir = os.getenv("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)
    
    content = STORY.strip() + "\n"
    output_path = os.path.join(output_dir, "entry.txt")
    
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(content)
    
    sys.stdout.write(content)

if __name__ == "__main__":
    main()
