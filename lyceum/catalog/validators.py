from django.forms import ValidationError


def validate_required_words(value: str):
    REQUIRED_WORDS = {'превосходн', 'роскошн', 'замечательн'}
    for word in REQUIRED_WORDS:
        if word in value.lower():
            break
    else:
        raise ValidationError(f'Вы должны использовать слова {" или ".join(REQUIRED_WORDS)} в описании товара')


def validate_words_count(value: str):
    if len(value.split()) < 2:
        raise ValidationError('Необходимо минимум 2 слова. Убедитесь, что вы разделяете слова с помощью пробела " "')


def validate_weight(value: int):
    if value >= 32767:
        raise ValidationError('Максимальное возможное значение - 32766')

