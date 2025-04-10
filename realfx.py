from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import random

app = Ursina(borderless=False)
window.title = 'B3313 3 - Real Castle Grounds Start'
window.borderless = False
window.size = (600, 400)
window.color = color.black

# Player
player = FirstPersonController(model='cube', color=color.white)
player.gravity = 0.5
player.jump_height = 0.8
player.position = Vec3(0, 2, 0)

# Uneven terrain
for x in range(-50, 51, 10):
    for z in range(-50, 51, 10):
        y_offset = random.uniform(-2, 2)
        Entity(model='cube', scale=(10,1,10), position=(x, y_offset, z),
               color=color.rgb(70 + int(x % 50), 100, 60 + int(z % 50)), collider='box', rotation=(random.randint(-5,5),0,random.randint(-5,5)))

# Asymmetrical moat
for i in range(4):
    Entity(model='plane', scale=(20, 1, 6), position=(-30 + i*20, 0.05, -45), color=color.rgba(0, 100, 255, 100))

# Distant castle wall (you can't reach it yet)
Entity(model='cube', scale=(60, 20, 2), position=(0, 10, -80), color=color.rgb(140, 120, 110), collider=None)

# Fog and lighting
Sky()
directional_light = DirectionalLight()
directional_light.look_at(Vec3(1,-1,-1))
directional_light.color = color.rgba(255, 255, 255, 40)

scene.fog_density = 0.04
scene.fog_color = color.rgba(60, 60, 100, 90)

# Glitch objects
for _ in range(10):
    Entity(model='cube', scale=(random.randint(2,5), 1, random.randint(2,5)),
           position=(random.randint(-40,40), 1.5, random.randint(-40,40)),
           color=color.rgba(255, 0, 255, 80), rotation=(0, random.randint(0,360), 0), collider='box')

# Placeholder secret door
door = Entity(model='cube', scale=(2, 4, 0.2), position=(15, 2, -20), color=color.rgba(255,255,255,100), collider='box')
door_trigger = Entity(model='cube', scale=(2,4,1), position=door.position + Vec3(0,0,1), collider='box', visible=False)

def update():
    if distance(player.position, door_trigger.position) < 2:
        print("🌀 You feel a strange pull... (door warp here in future)")

Text(text='Real Castle Grounds (B3313 Style)', position=Vec2(-0.3,0.45), scale=1.5, color=color.white, background=True)

app.run()
