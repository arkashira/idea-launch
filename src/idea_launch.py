import argparse
import json
from dataclasses import dataclass
from typing import Optional

@dataclass
class Idea:
    title: str
    description: str
    mockup: Optional[str] = None

def validate_idea(idea: Idea) -> bool:
    if not idea.title or not idea.description:
        return False
    return True

def validate_mockup(mockup: str) -> bool:
    allowed_extensions = ['.png', '.jpg', '.sketch', '.xd']
    for extension in allowed_extensions:
        if mockup.endswith(extension):
            return True
    return False

def main():
    parser = argparse.ArgumentParser(description='Idea Launch')
    parser.add_argument('--title', required=True, help='Idea title')
    parser.add_argument('--description', required=True, help='Idea description')
    parser.add_argument('--mockup', help='Mockup file path')
    args = parser.parse_args()

    idea = Idea(title=args.title, description=args.description, mockup=args.mockup)

    if not validate_idea(idea):
        print('Error: Title and description are required')
        return

    if idea.mockup and not validate_mockup(idea.mockup):
        print('Error: Invalid mockup file type')
        return

    if idea.mockup and not validate_mockup_size(idea.mockup):
        print('Error: Mockup file size exceeds 5 MB')
        return

    print('Idea submitted successfully')

def validate_mockup_size(mockup: str) -> bool:
    import os
    size = os.path.getsize(mockup)
    return size <= 5 * 1024 * 1024

if __name__ == '__main__':
    main()
