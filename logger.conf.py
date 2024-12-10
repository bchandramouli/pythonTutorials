#!/usr/bin/env python3 

#thanks to @patloeber's youtube channel


[handlers]
keys = consoleHandler

[formatters]
keys = simpleFormatter

[logger_root]
level = DEBUG
handlers = consoleHandler

[logger_simpleExample]
level = DEBUG
handler = consoleHandler
qualname = simpleExample
propogate = 0

[handler_consoleHandler]
class = StreamHandler
level = DEBUG
formatter = simpleFormatter
args = [sys, stdout,]


[formatter_simpleFormatter]
format=%(asctime)s - %(name)s - %(levelname)s - %(message)s