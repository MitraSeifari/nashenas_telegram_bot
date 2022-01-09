from types import SimpleNamespace

from src.utils.keyboard import create_keyboard

keys = SimpleNamespace(
    random_connect=':bust_in_silhouette: Random Connect',
    settings=':gear: Settings',
    exit=':cross_mark: Exit',
)

keyboards = SimpleNamespace(
    main=create_keyboard(keys.random_connect, keys.settings),
    exit=create_keyboard(keys.exit),
)

states = SimpleNamespace(
    random_connect='RANDOM_CONNECT',
    main='MAIN',
    connected='CONNECTED'
)
