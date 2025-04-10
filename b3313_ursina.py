from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import random

app = Ursina(borderless=False)

window.title = 'B3313 3 - Python Edition'
window.borderless = False
window.size = (600, 400)
window.color = color.black

# Player
player = FirstPersonController(model='cube', color=color.white)
player.gravity = 0.5
player.jump_height = 0.8

# Basic Ground
ground = Entity(model='plane', scale=(100,1,100), collider='box', color=color.gray)

# Area definitions (from B3313 Wiki-inspired names)
area_names = [
    'Castle Courtyard', 'Pink Void', 'Wet Dry Basement', 'Red Spiral Zone',
    'Rotated Halls', 'Sky Jail', 'Misty Forest', 'Dark Spiral Room', 'Mirror Maze'
]

# Colors and rotations for surreal feeling
area_colors = [color.pink, color.rgba(255,0,0,120), color.blue,
               color.rgba(255,255,0,90), color.green, color.cyan,
               color.rgba(100,0,255,180), color.rgba(200,0,0,200), color.rgba(150,150,255,120)]

def spawn_area(name, index):
    base_x = (index % 3) * 30 - 30
    base_z = (index // 3) * 30 - 30
    for i in range(5):
        x = base_x + random.randint(-5,5)
        z = base_z + random.randint(-5,5)
        size = random.uniform(3, 7)
        rot = random.randint(0, 360)
        Entity(model='cube', scale=(size, 2, size), position=(x, 1, z), color=area_colors[index % len(area_colors)], rotation_y=rot, collider='box')
    Text(text=name, position=Vec2(base_x/50, base_z/50), scale=1, color=color.white, background=True)

# Spawn all surreal areas
for i, area in enumerate(area_names):
    spawn_area(area, i)

# Weird Sky and Lighting
Sky()
directional_light = DirectionalLight()
directional_light.look_at(Vec3(1,-1,-1))
directional_light.color = color.rgba(255, 255, 255, 50)

fog_color = color.rgba(80, 60, 90, 90)
scene.fog_density = 0.03
scene.fog_color = fog_color

app.run()
