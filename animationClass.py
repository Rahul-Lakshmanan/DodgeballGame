class Animation:
    def __init__(self, frame_coordinates, frames):
        self.frame_coordinates = frame_coordinates
        self.right_animation = []
        self.left_animation = []
        self.frames = frames

    def Set_Frames(self, direction, frame_list):
        if direction == 'RIGHT': self.right_animation = frame_list
        else: self.left_animation = frame_list

    def Append_Frame(self, direction, frame):
        if direction == "RIGHT": self.right_animation.append(frame)
        else: self.left_animation.append(frame)
        
    def Get_Frame(self, direction, frame):
        if direction == 'RIGHT': return self.right_animation[frame]
        else: return self.left_animation[frame]   

    def Get_Start_Frame_Point(self, frame_number, coordinate):
        if coordinate == 'x': return self.frame_coordinates[frame_number][0][0]
        else: return self.frame_coordinates[frame_number][0][1]
    
    def Get_End_Frame_Point(self, frame_number, coordinate):
        if coordinate == 'x': return self.frame_coordinates[frame_number][1][0]
        else: return self.frame_coordinates[frame_number][1][1]
    
    def Num_Frames(self):
        return self.frames