this is a reupload of the yolo neural network tsc manipulator,

to get this working we are going to need the alexab branch of yolo
NOT THE PJREDDIE VERSION

to begin pull and build that version using this link (https://github.com/AlexeyAB/darknet) and the instructions to build ie 

mkdir darknet
cd darknet 
git clone https://github.com/AlexeyAB/darknet.git
cd darknet
make
./darknet detect

this will build the cpu detection version of darknet

the settings in the make file are explained in the github link (https://github.com/AlexeyAB/darknet)

the next step is to unpack and configure the toilet seat cover files

the file darknetSingleImage.py needs to be copied to the darknet directory.

next the data file should be updated to the paths for the train.txt and test.txt for the machine darknet is being installed to

the text-gen.py is used to create these files
 
see the default values in the data files for an example of what it should look like

once all of the above are complete

darknetSingleImage.py can be run as a python script

the program also contains the options to not use input statements and hard code the paths

the performDetect function can also be modified with the following values:


    Convenience function to handle the detection and returns of objects.

    Displaying bounding boxes requires libraries scikit-image and numpy

    Parameters
    ----------------
    imagePath: str
        Path to the image to evaluate. Raises ValueError if not found

    thresh: float (default= 0.25)
        The detection threshold

    configPath: str
        Path to the configuration file. Raises ValueError if not found

    weightPath: str
        Path to the weights file. Raises ValueError if not found

    metaPath: str
        Path to the data file. Raises ValueError if not found

    showImage: bool (default= True)
        Compute (and show) bounding boxes. Changes return.

    makeImageOnly: bool (default= False)
        If showImage is True, this won't actually *show* the image, but will create the array and return it.

    initOnly: bool (default= False)
        Only initialize globals. Don't actually run a prediction.

    Returns
    ----------------------


    When showImage is False, list of tuples like
        ('obj_label', confidence, (bounding_box_x_px, bounding_box_y_px, bounding_box_width_px, bounding_box_height_px))
        The X and Y coordinates are from the center of the bounding box. Subtract half the width or height to get the lower corner.

    Otherwise, a dict with
        {
            "detections": as above
            "image": a numpy array representing an image, compatible with scikit-image
            "caption": an image caption
        }




