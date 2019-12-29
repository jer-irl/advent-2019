from sols.sol12a import Body, Simulation


def test_movement():
    bodies = [
        Body(-1, 0, 2, 0, 0, 0),
        Body(2, -10, -7, 0, 0, 0),
        Body(4, -8, 8, 0, 0, 0),
        Body(3, 5, -1, 0, 0, 0),
    ]
    simulation = Simulation(bodies)
    simulation.simulate_n_steps(10)

    assert simulation.bodies[0].x == 2
    assert simulation.bodies[0].y == 1
    assert simulation.bodies[0].z == -3
    assert simulation.bodies[0].vx == -3
    assert simulation.bodies[0].vy == -2
    assert simulation.bodies[0].vz == 1

    assert simulation.bodies[1].x == 1
    assert simulation.bodies[1].y == -8
    assert simulation.bodies[1].z == 0
    assert simulation.bodies[1].vx == -1
    assert simulation.bodies[1].vy == 1
    assert simulation.bodies[1].vz == 3

    assert simulation.bodies[2].x == 3
    assert simulation.bodies[2].y == -6
    assert simulation.bodies[2].z == 1
    assert simulation.bodies[2].vx == 3
    assert simulation.bodies[2].vy == 2
    assert simulation.bodies[2].vz == -3

    assert simulation.bodies[3].x == 2
    assert simulation.bodies[3].y == 0
    assert simulation.bodies[3].z == 4
    assert simulation.bodies[3].vx == 1
    assert simulation.bodies[3].vy == -1
    assert simulation.bodies[3].vz == -1


def test_energy():
    bodies = [
        Body(-8, -10, 0, 0, 0, 0),
        Body(5, 5, 10, 0, 0, 0),
        Body(2, -7, 3, 0, 0, 0),
        Body(9, -8, -3, 0, 0, 0),
    ]
    simulation = Simulation(bodies)
    simulation.simulate_n_steps(100)

    assert simulation.total_energy() == 1940
