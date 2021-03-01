# Manimation

[Manim](https://github.com/3b1b/manim) os an engine for precise programatic animations, designed for creating explanatory math videos. The original work is done by Grant [3Blue1Brown](https://www.youtube.com/channel/UCYO_jab_esuFRV4b17AJtAw) Sanderson. But here I am using the [community edition](https://github.com/ManimCommunity/manim/) . 

### Installation

Manim installation is pretty easy if done with Choco. It requires shit ton of dependencies and will take ages to figure our perfectly. So I'll suggest to follow the [Installation Guide](https://docs.manim.community/en/latest/installation.html) .

### Target

I'll try to create some tutorial and explanatory animation for our DS course. 
Here is one simple example of manim and how cute it is

```python
from manim import *

class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()                    
        circle.set_fill(PINK, opacity=0.5)   
        square = Square()                   
        square.flip(RIGHT)                  
        square.rotate(-3 * TAU / 8)          
        self.play(ShowCreation(square))
        self.play(Transform(square, circle))
        self.play(FadeOut(square))      
```

![Manim](https://raw.githubusercontent.com/TamimEhsan/Manim_ation/master/Assets/SquareToCircle.gif)

Here is another one 

![Manim](https://raw.githubusercontent.com/TamimEhsan/Manim_ation/master/Assets/Shapes.gif)