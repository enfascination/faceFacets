## `faceFacets`
![A split face image](output/resize_IMG_8725.png?raw=true "Split face image")
A simple script for revealing the asymmetry in faces. It is mostly automated with a manual step for finding the middle of a face in the photo, its middle pixel.  Take a well lit, straight on photo of a face, put it in the example/ folder, open the photo in a photoviewer with coordinates to pick the pixel closest to the middle of the face, modify `halves_sample.csv` data file with one line per photo, and the x-coordinate of the halfway point you found, install the dependences, run the script, and get dual portraits.

## Getting it right
The examples folder gives examples of good and bad (head with tilt, yaw, or roll;bad light; bad facial expression) source photos. Most of the success of this is getting the photos right, so take several of each subject. During shooting pay attention to the eyes (are they level?), ears (are they level and the same distance from the head?), and especially the nose (is it pointing straight at you?). Good cues are to imagine a string pulling the top of the head straight up into the air, and a laser coming out of the nose point right into the middle of the lens (or lenses on a phone).  

During the manual step of finding the middle of the face in the photograph, I tend to find a compromise position based on the gap in the front teeth and the center of the bridge of the nose, also paying attention to the center of the bulb of the nose, the center of the chin, and the break in the middle of the lip. both GIMP and Preview.app show you coordinates when you are making rectangular selections: the first number is the x coordinate.

After processing, you know that you found a good split if the neck is equally thick in both facets. If it is thinner in one half than the other, there is a chance that the subject wasn't facing 12 o'clock to the camera, or, better, wasn't aligned on top of their neck.

## Manifest:
* `process.py`
  * the main script. In shell run `python process.py`.  Place files into input, enter each into the `halves.csv` datafile, and run. You possibly have to run `pip install Pillow` first as a one-time thing.
* `README.md`
  * This file  
* `input/`
  * where to put files to be transformed
* `output/`
  * where transformed files end up
* `halves_sample.csv`
  * data file for entering the one human-computed component of this pipeline, the x coordinate of pixels on the vertical halfway point of the face. This could be automated with face key-point recognition but I kept things simple, since this part goes fast enough for fewer than hundreds of images.
* `demo.xcf`
  * a GIMP project file with layers composing the halves of a face to illustrate the concept visually. Turn them on an off to see the variations. GIMP is the free open Photoshop alternative, easy to install and pull up.
