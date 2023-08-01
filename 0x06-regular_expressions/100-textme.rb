#!/usr/bin/env ruby
SENDER = ARGV[0].scan(/\[from:[+A-Za-z0-9]*\]/).join
RECEIVER = ARGV[0].scan(/\[to:[+A-Za-z0-9]*\]/).join
FLAGS = ARGV[0].scan(/\[flags:\d:\d:\d:\d:\d\]/).join
OUTPUT = "[" + SENDER + "]," "[" + RECEIVER + "]," "[" + FLAGS + "]"
puts OUTPUT
