import math

from core_ext.object3d import Object3D


class MovementRig(Object3D):
    """
    Add moving forwards and backwards, left and right, up and down (all local translations),
    as well as turning left and right, and looking up and down
    """
    def __init__(self, units_per_second=1, degrees_per_second=60):
        # Initialize base Object3D.
        # Controls movement and turn left/right.
        super().__init__()
        # Initialize attached Object3D; controls look up/down
        self._look_attachment = Object3D()
        self.children_list = [self._look_attachment]
        self._look_attachment.parent = self
        # Control rate of movement
        self._units_per_second = units_per_second
        self._degrees_per_second = degrees_per_second
        self.initial = self._look_attachment.local_matrix
        self.save = 0

        # Customizable key mappings.
        # Defaults: W, A, S, D, R, F (move), I, J, K, l (move crosshair)
        self.KEY_MOVE_FORWARDS = "w"
        self.KEY_MOVE_BACKWARDS = "s"
        self.KEY_MOVE_LEFT = "a"
        self.KEY_MOVE_RIGHT = "d"
        self.KEY_TURN_LEFT = "left"
        self.KEY_TURN_RIGHT = "right"
        self.KEY_LOOK_UP = "up"
        self.KEY_LOOK_DOWN = "down"
        self.SHOOT = "space"
        self.shooting = False
        self.power = 0
        self.ready = True

    # Adding and removing objects applies to look attachment.
    # Override functions from the Object3D class.
    def add(self, child):
        self._look_attachment.add(child)

    def remove(self, child):
        self._look_attachment.remove(child)

    def isShooting(self):
        return self.shooting
        
    def setShooting(self, shoot):
        self.shooting = shoot

    def isReady(self):
        return self.ready

    def getPower(self):
        return self.power
    
    def setPower(self, power):
        self.power = power

    def getInitalMatrix(self):
        return self.initial
    
    def setInitialRotation(self, save):
        self.save = save

    def getInitialRotation(self):
        return self.save

    def update(self, input_object, delta_time):
        move_amount = self._units_per_second * delta_time
        rotate_amount = self._degrees_per_second * (math.pi / 180) * delta_time*0.4
        if input_object.is_key_pressed(self.KEY_MOVE_FORWARDS):
            self.translate(0, 0, -move_amount)
        if input_object.is_key_pressed(self.KEY_MOVE_BACKWARDS):
            self.translate(0, 0, move_amount)
        if input_object.is_key_pressed(self.KEY_MOVE_LEFT):
            self.translate(-move_amount, 0, 0)
        if input_object.is_key_pressed(self.KEY_MOVE_RIGHT):
            self.translate(move_amount, 0, 0)
        if input_object.is_key_pressed(self.KEY_TURN_RIGHT):
            self.rotate_y(-rotate_amount)
            self.save = self.save - rotate_amount
        if input_object.is_key_pressed(self.KEY_TURN_LEFT):
            self.rotate_y(rotate_amount)
            self.save = self.save + rotate_amount
        if input_object.is_key_pressed(self.KEY_LOOK_UP):
            self._look_attachment.rotate_x(rotate_amount)
        if input_object.is_key_pressed(self.KEY_LOOK_DOWN):
            self._look_attachment.rotate_x(-rotate_amount)
            #self._look_attachment.set_local_matrix(self.initial)
            #self.rotate_y(-self.save)
            #self.save = 0
        if input_object.is_key_pressed(self.SHOOT):
            self.power += 0.3
            if self.power > 100:
                self.power=100
        if input_object.is_key_up(self.SHOOT):
            self.shooting = True
            self.ready = False
