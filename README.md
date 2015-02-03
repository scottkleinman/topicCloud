#Topic Cloud Generator

This is a simple method of generating topic clouds from [Mallet](http://mallet.cs.umass.edu/index.php) topic-word-counts data based on the implementation at [https://de.dariah.eu/tatom/topic_model_visualization.html#visualizing-topic-word-associations](https://de.dariah.eu/tatom/topic_model_visualization.html#visualizing-topic-word-associations). It uses [d3.js](http://d3js.org/) and Jason Davies's [Word Cloud Layout](https://github.com/jasondavies/d3-cloud) to generate the clouds.

##Requirements:

* To convert the Mallet data to JSON format: Python with numpy and os modules.
* To display the topic clouds: An active internet connection (the webpage downloads JQuery and JQuery UI).

##Instructions:
1. Open topicClouds.py in an editor and configure it at the top. Supply the path to the folder containing your topic-word-counts file, the name of the file itself, and the number of top words you wish to display. Save the file.

2. In Python, run topicClouds.py. It should output the proportions for each of the top words in the topic. It will also write the data to a JavasScript file called dataset.js in the same folder as your input file.

  If you encounter an error in the zip function in line 50, you are probably running Python 2.7. Change it to "izip", and the re-run the script.

3. Go to your input folder and find the dataset.js file. Copy it into the topicClouds folder (replacing the sample dataset file provided).

4. Open the topicClouds.html in a browser and it should work. Note that the page requires JQuery, so you must have an active internet connection.

  It is possible to modify the size of the word cloud and the appearance of the characters. Open the topicClouds.html file in an editor and modify the configuration in lines 24-29 if necessary. Here are the defaults:

  ```JavaScript
    var width = 300;
    var height = 300;
    var magnify = 1000;
    var wordRotation = "off"; // Keep all words horizontal
    var fill = d3.scale.linear(); // Render in black and white
  ```
  
  Changing fill to d3.scale.category20() will render the cloud in colour.

  Save the topicClouds.html file and refresh the browser.

5. You can change any of the above settings from within the web page by clicking on the Settings button (with the gear icon). The colour scale menu offers a number of standard options in d3. Click the "?" button to see more information on the d3 website. Saving the settings will automatically regenerate the topic cloud with the new settings. However, if you wish to save these settings permanently, you must hard code them in the configuration section as described in step 4 above.

6. Layouts are generated on the fly and will therefore be different if the page is reloaded (even if the settings are the same). If you are happy with a particular layout, it may be worthwhile to take a screen shot to preserve the exact appearance. In some cases, you may wish to see a new layout. Clicking the Refresh button will automatically generate a new topic cloud without reloading the page.
