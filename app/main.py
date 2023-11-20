"""Greetings generator."""


def greeting(name: str) -> str:
    """Return greetings string.

    Args:
        name: Usernamecd app


    Returns:
        str: greetings string
    """
    capitalized_name = ' '.join([word.capitalize() for word in name.split()])
    return 'Greetings, {name}'.format(name=capitalized_name)
