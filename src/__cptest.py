from cursesplus import *
from cursesplus import filedialog
import cursesplus
import cursesplus.messagebox
from time import sleep


message = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Vitae ultricies leo integer malesuada. Dui id ornare arcu odio ut. Massa placerat duis ultricies lacus sed. Eu nisl nunc mi ipsum faucibus. Vulputate ut pharetra sit amet aliquam id diam. Enim nulla aliquet porttitor lacus luctus accumsan tortor. Malesuada bibendum arcu vitae elementum curabitur vitae. Diam sit amet nisl suscipit adipiscing bibendum est. Ipsum consequat nisl vel pretium lectus quam id leo. Viverra nam libero justo laoreet sit amet cursus. Justo eget magna fermentum iaculis eu non diam. Sapien nec sagittis aliquam malesuada bibendum arcu. Blandit cursus risus at ultrices mi tempus imperdiet. Enim nunc faucibus a pellentesque sit amet porttitor. Ac odio tempor orci dapibus ultrices in iaculis. Bibendum enim facilisis gravida neque convallis a cras semper. Non consectetur a erat nam at lectus urna. Molestie a iaculis at erat pellentesque.









Pellentesque eu tincidunt tortor aliquam nulla facilisi. Faucibus turpis in eu mi. Vestibulum lectus mauris ultrices eros in cursus turpis massa. Duis ut diam quam nulla porttitor massa. Ac tincidunt vitae semper quis. Tincidunt arcu non sodales neque sodales ut. Egestas maecenas pharetra convallis posuere morbi leo urna molestie. Velit ut tortor pretium viverra suspendisse. Ut sem nulla pharetra diam sit amet nisl suscipit adipiscing. Et tortor consequat id porta nibh. Sagittis id consectetur purus ut faucibus. Tellus in metus vulputate eu scelerisque felis. Sollicitudin nibh sit amet commodo nulla facilisi nullam vehicula ipsum. Mi ipsum faucibus vitae aliquet nec ullamcorper. Risus viverra adipiscing at in tellus integer feugiat scelerisque.

Sed faucibus turpis in eu. Amet commodo nulla facilisi nullam vehicula ipsum a arcu. Egestas integer eget aliquet nibh praesent tristique. Consequat semper viverra nam libero justo laoreet sit amet cursus. A condimentum vitae sapien pellentesque habitant morbi tristique. Pharetra pharetra massa massa ultricies. Malesuada pellentesque elit eget gravida cum sociis natoque. Purus faucibus ornare suspendisse sed nisi. Urna porttitor rhoncus dolor purus. Et tortor at risus viverra. In arcu cursus euismod quis viverra nibh. Sed ullamcorper morbi tincidunt ornare massa eget egestas purus. Urna neque viverra justo nec. Maecenas accumsan lacus vel facilisis. Duis tristique sollicitudin nibh sit. Arcu dictum varius duis at consectetur lorem. Dolor morbi non arcu risus quis. Sed libero enim sed faucibus turpis in eu mi bibendum. Posuere urna nec tincidunt praesent semper feugiat nibh sed. Interdum varius sit amet mattis vulputate enim.

Nunc non blandit massa enim nec dui. Aliquam vestibulum morbi blandit cursus. Vulputate enim nulla aliquet porttitor lacus luctus accumsan tortor posuere. Sit amet nulla facilisi morbi tempus iaculis urna id. Eget aliquet nibh praesent tristique magna sit. Nulla aliquet enim tortor at auctor urna nunc. Id interdum velit laoreet id donec ultrices tincidunt arcu non. Mollis aliquam ut porttitor leo a. Elit ut aliquam purus sit amet luctus venenatis. Condimentum vitae sapien pellentesque habitant morbi. Aliquam sem et tortor consequat id porta. At auctor urna nunc id cursus. Gravida rutrum quisque non tellus orci ac. Amet aliquam id diam maecenas ultricies mi eget mauris pharetra. Malesuada fames ac turpis egestas sed tempus urna et. Tincidunt lobortis feugiat vivamus at augue eget arcu. Duis convallis convallis tellus id interdum velit laoreet id. Sagittis nisl rhoncus mattis rhoncus urna neque viverra justo nec. Dui vivamus arcu felis bibendum ut tristique et. Molestie at elementum eu facilisis sed odio morbi quis commodo.

Faucibus turpis in eu mi bibendum. Et magnis dis parturient montes nascetur ridiculus. Tempor commodo ullamcorper a lacus vestibulum. Turpis in eu mi bibendum neque egestas congue. Sollicitudin ac orci phasellus egestas tellus. Consectetur adipiscing elit pellentesque habitant. Nisi vitae suscipit tellus mauris. At lectus urna duis convallis. Euismod nisi porta lorem mollis aliquam ut porttitor leo. Elit at imperdiet dui accumsan sit amet nulla. Augue eget arcu dictum varius duis at consectetur lorem. Molestie ac feugiat sed lectus vestibulum mattis. Neque viverra justo nec ultrices dui sapien eget mi. Amet consectetur adipiscing elit ut aliquam purus. Consequat nisl vel pretium lectus quam id leo in. Turpis massa tincidunt dui ut ornare lectus. Tristique nulla aliquet enim tortor at auctor. Porttitor lacus luctus accumsan tortor.
"""
e = ""
def __test__(stdscr):
    global e
    cursesplus.textview(stdscr,file="src/cursesplus/cp.py",message="LICENSE",isagreement=True,requireyes=True)

if __name__ == "__main__":
    #Testing things
    curses.wrapper(__test__)
    print(e)