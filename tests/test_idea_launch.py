import pytest
from idea_launch import Idea, validate_idea, validate_mockup, validate_mockup_size

def test_validate_idea():
    idea = Idea(title='Test Idea', description='This is a test idea')
    assert validate_idea(idea)

def test_validate_idea_empty_title():
    idea = Idea(title='', description='This is a test idea')
    assert not validate_idea(idea)

def test_validate_idea_empty_description():
    idea = Idea(title='Test Idea', description='')
    assert not validate_idea(idea)

def test_validate_mockup():
    mockup = 'test.png'
    assert validate_mockup(mockup)

def test_validate_mockup_invalid_extension():
    mockup = 'test.txt'
    assert not validate_mockup(mockup)

def test_validate_mockup_size():
    mockup = 'test.png'
    with open(mockup, 'w') as f:
        f.write('a' * 1024 * 1024)  # 1 MB
    assert validate_mockup_size(mockup)

def test_validate_mockup_size_exceeds_limit():
    mockup = 'test.png'
    with open(mockup, 'w') as f:
        f.write('a' * 6 * 1024 * 1024)  # 6 MB
    assert not validate_mockup_size(mockup)
