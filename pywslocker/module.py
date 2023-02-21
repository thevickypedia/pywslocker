import platform


class Settings:
    """Wrapper for settings.

    >>> Settings

    """

    os: str = platform.system()
    if os not in ("Linux", "Darwin", "Windows"):
        raise OSError(
            "Package is unsupported in %s" % os
        )


settings = Settings()
