__all__ = ("seconds_to_str",)


def seconds_to_str(seconds: int) -> str:
    """Реализует текстовое представление времени.

    Example:
        >> seconds_to_str(20)
        20s
        >> seconds_to_str(60)
        01m00s
        >> seconds_to_str(65)
        01m05s
        >> seconds_to_str(3700)
        01h01m40s
        >> seconds_to_str(93600)
        01d02h00m00s
    """
    days, seconds = divmod(seconds, 86400)
    hours, seconds = divmod(seconds, 3600)
    minutes, seconds = divmod(seconds, 60)

    result = []
    if days > 0:
        result.append(f"{days:02d}d")
    if hours > 0 or days > 0:
        result.append(f"{hours:02d}h")
    if minutes > 0 or hours > 0 or days > 0:
        result.append(f"{minutes:02d}m")
    result.append(f"{seconds:02d}s")

    return "".join(result)
