# You have an 8*8 matrix display that is controlled by an API
# set_led_state(X,Y,state) (where state=1 turns on a LED and state=0 turns an LED off)
# 0,0 is the top left of the display and 7,7 is the bottom right
# You have a font bitmap dictionary that maps an ascii character to a tuple of eight bytes, each byte represents one row of the display matrix from the top row (0), each bit of the byte maps to a column of the matrix, from left (0) to right (0),
# e.g.  bitmap = font['L']
# would return a tuple [ 0x80, 0x80, 0x80, 0x80, 0x80, 0x80, 0x80, 0xF8]

# Write a function that takes a string of ascii characters and displays them one at a time on the display, with a variable delay time, using the font dictionary and the set_led_state(X,Y,state) API call.

bitmap = font['L']22