from dynaconf import Dynaconf

settings = Dynaconf(
    envvar_pre="OUTOMAATTI",
    settings_files=['outomaatti.toml'],
)
