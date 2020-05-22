import darknet as dn


if __name__ == "__main__":
#this main methood parses in the nn files from a user input and runs the object detection on an image
	
	#these lines read in the network files from the comandline but examples are comeented out below
	config = input('input the location of the config file \n')
	#config = "/home/spencer/darknet2/darknet/tsc3/tsc3.cfg" #nn config file

	weights = input('input the location of the weights file\n')
	#weights = "/home/spencer/darknet/tsc3/Backup/tsc3_50000.weights" #weights file

	data = input("input the location of the data file\n")
	#data = "/home/spencer/darknet2/darknet/tsc3/tsc3.data" #data file
	cont = True
	while(cont):
		path = input("input an image path\n")
		r = dn.performDetect(path,.25,config,weights,data) #perform the detection
		if r:
			print("detected toilet seat covers\n")
			print(r) #r is a list of tuples 
		else:
			print("no object found\n")


