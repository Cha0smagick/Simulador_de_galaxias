import pygame
import random
import math

# Inicializar Pygame
pygame.init()

# Configuración de la ventana
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simulador Espacial")

# Colores
BLACK = (0, 0, 0)  # Color de fondo

# Clase para las estrellas
class Star:
    def __init__(self):
        self.angle = random.uniform(0, 2 * math.pi)  # Ángulo aleatorio
        self.distance = 50  # Distancia fija desde el centro (borde del círculo)
        self.size = random.randint(1, 3)  # Tamaño aleatorio de la estrella
        self.speed = random.uniform(1, 3)  # Velocidad aleatoria

    def update(self):
        # Mover la estrella hacia afuera desde el borde
        self.distance += self.speed

        # Reposicionar si la estrella se aleja demasiado
        if self.distance > 500:  # Limitar la distancia
            self.distance = 50  # Resetear a la distancia del borde
            self.angle = random.uniform(0, 2 * math.pi)  # Nuevo ángulo

    def draw(self, surface):
        # Calcular posición X e Y
        x = WIDTH / 2 + self.distance * math.cos(self.angle)
        y = HEIGHT / 2 + self.distance * math.sin(self.angle)
        pygame.draw.circle(surface, (255, 255, 0), (int(x), int(y)), self.size)

# Clase para las galaxias de dos brazos
class Galaxy:
    def __init__(self):
        self.x = random.uniform(0, WIDTH)
        self.y = random.uniform(0, HEIGHT)
        self.size = random.randint(30, 60)  # Tamaño de la galaxia
        self.angle = random.uniform(0, 2 * math.pi)  # Ángulo inicial
        self.rotation_speed = random.uniform(0.01, 0.05)  # Velocidad de rotación
        self.color = (random.randint(100, 255), random.randint(100, 255), random.randint(100, 255))  # Color aleatorio

    def update(self):
        # Actualizar el ángulo de rotación
        self.angle += self.rotation_speed
        if self.angle >= 2 * math.pi:
            self.angle -= 2 * math.pi

    def draw(self, surface):
        # Dibujar la galaxia en forma de dos brazos
        points = []
        for i in range(0, 360, 10):  # Crear puntos en ángulos de 10 grados
            rad = math.radians(i)
            # Calcular el radio para los brazos de la galaxia
            radius = self.size + 10 * math.sin(2 * rad + self.angle)  # Forma de dos brazos
            x = self.x + radius * math.cos(rad)
            y = self.y + radius * math.sin(rad)
            points.append((x, y))

        # Dibujar la galaxia
        pygame.draw.polygon(surface, self.color, points)

# Función para generar estrellas
def generate_stars(num_stars):
    return [Star() for _ in range(num_stars)]

# Función para generar galaxias
def generate_galaxies(num_galaxies):
    return [Galaxy() for _ in range(num_galaxies)]

# Crear estrellas y galaxias
stars = generate_stars(200)  # Ajusta el número de estrellas
galaxies = generate_galaxies(5)  # Ajusta el número de galaxias

# Bucle principal
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Actualizar estrellas y galaxias
    for star in stars:
        star.update()
    for galaxy in galaxies:
        galaxy.update()

    # Dibujar en la pantalla
    screen.fill(BLACK)  # Limpiar la pantalla
    for galaxy in galaxies:
        galaxy.draw(screen)  # Dibujar galaxias
    for star in stars:
        star.draw(screen)  # Dibujar estrellas

    # Actualizar la pantalla
    pygame.display.flip()
    clock.tick(60)  # Limitar a 60 FPS

pygame.quit()
