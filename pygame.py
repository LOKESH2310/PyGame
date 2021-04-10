import pgzrun
from random import  randint
HEIGHT= 580
WIDTH=1000
brown = 138, 53, 17
player = Actor("hero")
player.y = HEIGHT//2
player_speed = 10
weapons = []
enemies = []
game_over = False
score = 0

def draw():
  screen.fill("brown")
  screen.blit("city",(0,0))
  player.draw()
  draw_weapons()
  draw_enemies()
  draw_score()
  if game_over  :
    virus_attack()
 

def update():
  if not game_over:
    move_player()
    move_weapons()
    move_enemies()
    check_weapon_collision()
    check_player_collision()
    check_player_boun()

def on_key_down(key):
  if not game_over:
    if key == keys.SPACE:
      create_weapon()

def create_weapon():
    weapon = Actor("weapon")
    weapon.pos = player.pos
    weapons.append(weapon)

def create_enemy():
  enemy = Actor ("enemy")
  enemy.y = randint(100, HEIGHT-100)
  enemy.x = 750
  enemies.append(enemy)

def draw_weapons():
    for weapon in weapons:
        weapon.draw()

def draw_enemies():
  for enemy in enemies:
    enemy.draw()

def move_weapons():
  for weapon in weapons:
    weapon.x += 5

def move_enemies():
  for enemy in enemies:
    enemy.x -= 1




def move_player():
  if keyboard.left:
    player.x -= player_speed
  elif keyboard.right:
    player.x += player_speed
  elif keyboard.up:
    player.y -= player_speed
  elif keyboard.down:
    player.y += player_speed

def check_player_boun():
  if player.top <0 :
    player.top = 0
  if player.bottom > HEIGHT:
    player.bottom = HEIGHT
  if player.left < 0 :
    player.left = 0

def check_weapon_collision():
  global score
  for enemy in enemies:
    for weapon in weapons:
      if weapon.colliderect(enemy):
        enemies.remove(enemy)
        weapons.remove(weapon)
        score += 2
        create_enemy()

def check_player_collision():
  global game_over
  for enemy in enemies:
        if player.colliderect(enemy):
            player.image = "attack"
            game_over = True
        if enemy.left <0 :
          player.image = "attack"
          game_over = True

def virus_attack():
  position = ((WIDTH//2 - 400), HEIGHT-100)
  screen.draw.text("VIRUS ATTACKED!!!", position, fontsize=100,    color =(153, 61, 184)
)

def draw_score():
    screen.draw.text("Score: "+str(score), (700,10), fontsize=30, color="blue")

create_enemy()
pgzrun.go()
