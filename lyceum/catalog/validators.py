from django.forms import ValidationError


def validate_required_words(value: str):
    REQUIRED_WORDS = {'превосходно', 'роскошно'}
    for word in REQUIRED_WORDS:
        if word in value.lower():
            break
    else:
        raise ValidationError(f'Вы должны использовать слова {" или ".join(REQUIRED_WORDS)} в описании товара')


def validate_words_count(value: str):
    if len(value.split()) < 2:
        raise ValidationError('Необходимо минимум 2 слова. Убедитесь, что вы разделяете слова с помощью пробела " "')
