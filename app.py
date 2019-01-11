from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")
def index():

   position = request.args.get("position")
   print(position)

   left_class = "timeline-item_left"
   right_class = "timeline-item_right"

   if position == 'right':
       left_class =  "timeline-item_right"
       right_class = "timeline-item_left"

    # open file for reading, 'r'
   # file is saved to variable
   index_file = open('index.html', 'r')
   # read contents of the file
   my_html = index_file.read()

   #     # add use input back into the html
   my_html = my_html.replace("{{timeline-item_left}}", left_class)
   my_html = my_html.replace("{{timeline-item_right}}", right_class)

   # close the file out when you're done
   index_file.close()

   return my_html