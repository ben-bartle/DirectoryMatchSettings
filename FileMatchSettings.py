import re
import sublime
import sublime_plugin

class FileMatchSettingsListener(sublime_plugin.EventListener):
	def on_load_async(self, view):
		view.run_command("file_match_settings")

class FileMatchSettingsCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		configs = sublime.load_settings('FileMatchSettings.sublime-settings').get("configs");
		filename = self.view.file_name()
		# search through all the config sections for a match
		for config in configs:
			if re.search(config['match'],filename):
				# if we find a matching config section, apply the settings
				for name, value in config['settings'].items():
					self.view.settings().set(name, value)
				# stop looking
				break;
