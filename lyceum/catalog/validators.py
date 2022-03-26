from django.forms import ValidationError


def validate_required_words(value: str):
    REQUIRED_WORDS = {'превосходно', 'роскошно'}
    for word in REQUIRED_WORDS:
        if word in value.lower():
            break
    else:
        raise ValidationError(f'Вы должны использовать слова {" или ".join(REQUIRED_WORDS)} в описании товара')


def validate_words_count(value: str):
    if value.count(' ') < 1:
        raise ValidationError('В описании товара должно быть как минимум 2 слова')
