#!/usr/bin/env python

import os
import shutil

os_folder_structures = {
  "os x": ["~",
           "Library",
           "Application Support",
           "discord"],
  "linux": ["~",
            ".config",
            "discord"],
  "windows": [r"%APPDATA%",
              "discord"],
}

discord_dir = None
for os_name in os_folder_structures:
  _discord_dir = os_folder_structures[os_name]
  _discord_dir = os.path.join(*_discord_dir)
  _discord_dir = os.path.expanduser(_discord_dir)
  _discord_dir = os.path.expandvars(_discord_dir)
  if os.path.exists(_discord_dir):
    discord_dir = _discord_dir

if discord_dir is None:
  print("No Discord cache exists on this device.")
else:
  cache_dir = os.path.join(discord_dir, "Cache")
  revealed_dir = os.path.join(discord_dir, "CacheRevealed")

  if not os.path.exists(cache_dir):
    print("No Discord cache exists on this device.")
  else:
    try:
      os.makedirs(revealed_dir)
    except FileExistsError:
      pass
    for image_file in os.listdir(cache_dir):
      if os.path.isfile(os.path.join(cache_dir, image_file)):
        print(image_file)
    selection = input("Select an image to reveal: ").strip()
    shutil.copy(
      os.path.join(cache_dir, selection),
      os.path.join(revealed_dir, selection + ".png"),
    )
