from dataclasses import dataclass
import re
from typing import List


@dataclass
class Body:
    x: int
    y: int
    z: int

    vx: int
    vy: int
    vz: int

    def potential_energy(self) -> int:
        return abs(self.x) + abs(self.y) + abs(self.z)

    def kinetic_energy(self) -> int:
        return abs(self.vx) + abs(self.vy) + abs(self.vz)

    def total_energy(self) -> int:
        return self.potential_energy() * self.kinetic_energy()


class Simulation:
    def __init__(self, bodies: List[Body]):
        self.bodies = bodies

    def simulate_step(self):
        for attracted in self.bodies:
            for attractor in self.bodies:
                if attracted.x < attractor.x:
                    attracted.vx += 1
                elif attracted.x > attractor.x:
                    attracted.vx -= 1
                if attracted.y < attractor.y:
                    attracted.vy += 1
                elif attracted.y > attractor.y:
                    attracted.vy -= 1
                if attracted.z < attractor.z:
                    attracted.vz += 1
                elif attracted.z > attractor.z:
                    attracted.vz -= 1

        for body in self.bodies:
            body.x += body.vx
            body.y += body.vy
            body.z += body.vz

    def simulate_n_steps(self, n: int):
        for _ in range(n):
            self.simulate_step()

    def total_energy(self) -> int:
        return sum(b.total_energy() for b in self.bodies)


def body_from_data_line(data_line: str) -> Body:
    pattern = re.compile(r"^<x=(?P<x>-?\d+), y=(?P<y>-?\d+), z=(?P<z>-?\d+)>$")
    match = pattern.match(data_line)
    return Body(int(match.group("x")), int(match.group("y")), int(match.group("z")), 0, 0, 0)


def simulation_from_data(data: str) -> Simulation:
    bodies = []
    for line in data.split("\n"):
        bodies.append(body_from_data_line(line))
    return Simulation(bodies)


def run(data):
    simulation = simulation_from_data(data)
    simulation.simulate_n_steps(1000)
    return simulation.total_energy()
