from django.core.exceptions import ValidationError


def valid_difficulty(n):
    if n > 5 or n < 1:
        raise ValidationError("商品分类在1到5之间")