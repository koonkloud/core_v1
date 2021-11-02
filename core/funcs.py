funcs = {
	"add": {
		"logic": lambda l, r: l + r,
		"reverse": "sub"
	},
	"sub": {
		"logic": lambda l, r: l - r,
		"reverse": "add"
	},
	"concat": {
		"logic": lambda l, r: l + " " + r,
	}
}
