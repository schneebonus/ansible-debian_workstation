import json
import sys

def append_brightness(input):
	return input
	if input[-1] != "]":
		return input
	else:
		input = input[:-1]
		brightness = {
			"name":"brightness",
			"instance":"disp0",
			"color":"#00FF00",
			"markup":"none",
			"full_text": "100%"}
		brightness_json = json.dumps(brightness)
		return input + "," + brightness_json + "]"

if __name__ == '__main__':
	print(append_brightness(sys.argv[1]))
