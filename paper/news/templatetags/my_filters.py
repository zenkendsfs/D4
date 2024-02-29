from django import template

register = template.Library()

@register.filter()
def censor(text):
    file_path = 'news/templatetags/bad_words.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        bad_words = file.read().replace(' ', '').split(',')
    censored_text = text
    for word in bad_words:
        censored_text = censored_text.replace(word[1:], '*'*(len(word)-1))
    return censored_text


