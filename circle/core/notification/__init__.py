import pkgutil
import pathlib
import importlib

channels_dirs = pathlib.Path(__file__).parent / "channels"

for module in pkgutil.iter_modules([str(channels_dirs)]):
    importlib.import_module(f"{__package__}.channels.{module.name}")
