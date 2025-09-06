#!/usr/bin/env ruby
puts ARGV[0].scan(/From:\s*(.+?)\s+To:\s*(.+?)\s+Flags:\s*(.+)/).join(",")
