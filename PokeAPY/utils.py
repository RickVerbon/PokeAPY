def format_name(name: str) -> str:
    if '-' in name:
        parts = name.split('-')
        formatted_name = ' '.join(part.capitalize() for part in parts)
        return formatted_name
    else:
        return name.capitalize()
