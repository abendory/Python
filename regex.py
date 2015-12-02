# Search a file for all instances where a string is NOT present
# Example usage: Search all services for NON-Apple daemons

import re
import subprocess

print "All non-Apple daemons running on the machine."

p = subprocess.Popen(['launchctl', 'list'], stdout=subprocess.PIPE)
output, err = p.communicate()
new_list = output.split('\n')

matched_indices = []
for index, line in enumerate(new_list):
	if re.search(r'^((?!com\.apple).)*$', line):
		matched_indices.append(index)

for element in matched_indices:
	print new_list[element]

