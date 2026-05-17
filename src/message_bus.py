import blinker

restart_requested = blinker.signal("restart_requested")
snake_grow_requested = blinker.signal("snake_grow_requested")
spawn_new_apple_requested = blinker.signal("spawn_new_apple_requested")
