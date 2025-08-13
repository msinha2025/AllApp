#!/bin/bash

echo "Deleting temp files..."
rm -rf /tmp/*

echo "Emptying Trash..."
rm -rf ~/.local/share/Trash/files/*
rm -rf ~/.local/share/Trash/info/*

echo "Clearing Firefox cache..."
rm -rf ~/.cache/mozilla/firefox/*.default-release/cache2/*

echo "Clearing Chromium/Chrome cache..."
rm -rf ~/.cache/chromium/Default/Cache/*
rm -rf ~/.cache/google-chrome/Default/Cache/*

echo "Cleanup complete."