"""Greetings generator."""


def greeting(name: str) -> str:
    """Returns greetings string.

      Args:
          name: Username

      Returns:
          str: greetings string
      """
    capitalized_name = ' '.join([word.capitalize() for word in name.split()])
    return f"Greetings, {capitalized_name}"
