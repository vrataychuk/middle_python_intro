"""Генератор приветствий."""
# import pprint


def greeting(name: str) -> str:
    """Возвращает текст приветствия.

      Args:
          name: Имя пользователя

      Returns:
          str: Текст приветствия
      """
    return f'Привет, {" ".join([word.capitalize() for word in name.split()])}'
