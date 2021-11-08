"""Helper for add_training script"""

def check_inp(inp, quit_key="quit", none_key="none"):
	"""Get user input, return it if not command"""
	if inp == quit_key: exit()		
	elif inp == none_key or inp.strip() == "": return None
	else: return inp

add_next_dict = {
	"yes": True,
	"y": True,

	"no": False,
	"n": False,
	"": False
}